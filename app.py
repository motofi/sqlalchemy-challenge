# IP: 127.0.0.1
# Port: 5000
# endpoint (but not yet defined): /
# localhost:5000
# or
# 127.0.0.1:5000
# in browser should take me to the page
# %matplotlib inline
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
# 1. import Flask - says that we're creating a Flask app, differentiating it from a Python app
from flask import Flask, jsonify

# Set up database
# 1- connect to sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# 2- relect the db
Base = automap_base()
# 3 - reflect the tables
Base.prepare(engine, reflect=True)
# 4 - name the classes for reference
Station = Base.classes.station
Measurement = Base.classes.measurement
# 5 - Create a session
session = Session(engine)

# Set up Flask
# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# 3. Home Page
# Define what to do when a user hits the index route
# List all the routes that are available
@app.route("/")
def index():
    "List all available api routes."
    return (
    f"Available Routes:<br/>"
    f"/api/v1.0/precipitation<br/>"
    f"/api/v1.0/stations<br/>"
    f"/api/v1.0/tobs<br/>"
    f"/api/v1.0/<start><br/>"
    f"/api/v1.0/<start>/<end><br/>"
    )


# @app.route("/api/v1.0/precipitation")
# Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
last_date = dt.datetime(2017, 8, 23)
last_twelve_mos = last_date - dt.timedelta(days = 365)
twelve_mos_precip = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= last_twelve_mos).all()



# Return the JSON representation of your dictionary.

# @app.route("/api/v1.0/stations")
# Return a JSON list of stations from the dataset.

# @app.route("/api/v1.0/tobs")
# Query the dates and temperature observations of the most active station for the last year of data.
#
# Return a JSON list of temperature observations (TOBS) for the previous year.

# @app.route("/api/v1.0/<start>")
#  Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#
#  When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.


# @app.route("/api/v1.0/<start>/<end>")
# When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.




# 4. Define what to do when a user hits the /api/v1.0/precipitation route
@app.route("/api/v1.0/precipitation")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

# Keeps the Flask app running
if __name__ == "__main__":
    app.run(debug=True)
