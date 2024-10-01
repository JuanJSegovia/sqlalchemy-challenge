# SQLAlchemy Climate Analysis and Flask API
Project Overview
This project focuses on conducting a climate analysis of Honolulu, Hawaii, using a SQLite database containing historical weather data. The analysis is performed using SQLAlchemy ORM, Pandas, and Matplotlib. Additionally, a Flask API is developed to provide access to the analyzed data through various endpoints.

The project is divided into two main parts:

Climate Data Exploration and Analysis: Analyze historical precipitation and temperature data.
Flask API: Create an API to allow users to access specific climate data.

# Project Structure
Resources: Contains the SQLite database (hawaii.sqlite) with climate data.

## Part 1: Climate Data Analysis
Precipitation Analysis
Retrieve and analyze the precipitation data for the last 12 months.
Visualize the results using a time-series plot.
Provide summary statistics for the precipitation data.
Station Analysis
Identify the number of weather stations in the dataset.
Determine the most active station based on the number of observations.
Retrieve the temperature observations (TOBS) for the most active station over the last 12 months.
Visualize the temperature data using a histogram.

## Part 2: Flask API
A Flask API is built to provide access to the climate data. The following API routes are available:

/: The homepage that lists all available API routes.
/api/v1.0/precipitation: Returns a JSON dictionary of the last 12 months of precipitation data, where the date is the key and the precipitation value is the corresponding value.
/api/v1.0/stations: Returns a JSON list of all weather stations.
/api/v1.0/tobs: Returns a JSON list of temperature observations for the most active station over the last 12 months.
/api/v1.0/<start>: Returns the minimum, average, and maximum temperatures for all dates greater than or equal to the provided start date.
/api/v1.0/<start>/<end>: Returns the minimum, average, and maximum temperatures for a specified start-end date range.

Summary
This project provides both an analysis of climate data in Honolulu, Hawaii, and a user-friendly API to query that data. The Flask API can be used to access key weather insights, such as precipitation levels and temperature trends, to assist with trip planning or other research purposes.

