# Import the dependencies.
from flask import Flask
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Base.classes.keys

Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)



#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )
    


@app.route("/api/v1.0/precipitation")
def precipitation():

    session=Session.(engine)

last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    one_year_ago = dt.datetime.strptime(last_date, "%Y-%m-%d") - dt.timedelta(days=365)
    
    # Query precipitation data
    results = session.query(Measurement.date, Measurement.prcp).\
              filter(Measurement.date >= one_year_ago).all()
    
    session.close()

    # Convert query results to dictionary (date: prcp)
    precipitation_data = {date: prcp for date, prcp in results}
    
    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():

    """Return a JSON list of stations."""
    session = Session(engine)
    
    # Query all stations
    results = session.query(Station.station).all()
    
    session.close()

    # Convert the list of tuples into a normal list
    stations = list(np.ravel(results))
    
    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def tabs():

     """Return the temperature observations for the most-active station in the last year"""
    session = Session(engine)
    
    # Get the last date and calculate the date one year ago
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    one_year_ago = dt.datetime.strptime(last_date, "%Y-%m-%d") - dt.timedelta(days=365)
    
    # Find the most active station
    most_active_station = session.query(Measurement.station).\
                          group_by(Measurement.station).\
                          order_by(func.count(Measurement.station).desc()).first()[0]
    
    # Query temperature data for the most-active station for the last year
    results = session.query(Measurement.date, Measurement.tobs).\
              filter(Measurement.station == most_active_station).\
              filter(Measurement.date >= one_year_ago).all()
    
    session.close()

    # Convert the list of tuples into a normal list
    temps = list(np.ravel(results))
    
    return jsonify(temps)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temp_stats(start, end=None):
    """Return TMIN, TAVG, TMAX for all dates greater than start, or between start and end"""
    session = Session(engine)
    
    # If no end date is provided, query data from the start date onwards
    if end is None:
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                  filter(Measurement.date >= start).all()
    # If both start and end dates are provided, query data between the two
    else:
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                  filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    session.close()

    # Extract the results and return as JSON
    temp_data = list(np.ravel(results))
    
    return jsonify(temp_data)

if __name__ == "__main__":
    app.run(debug=True)




