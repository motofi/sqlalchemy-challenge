
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
from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Station = Base.classes.station
Measurement = Base.classes.measurement

session = Session(engine)

app = Flask(__name__)


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


@app.route("/api/v1.0/precipitation")
def precipitation():
    f"The last twelve months of Hawaii precipitation data."
    last_twelve_mos = dt.datetime(2017, 8, 23) - dt.timedelta(days = 365)
    twelve_mos_precip = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= last_twelve_mos).all()
    precip = {date: prcp for date, prcp in twelve_mos_precip}
    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    f"Return a JSON list of stations from the dataset."
    station_list = session.query(Station.station).all()
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def active_st_tobs():
    f"Query the dates and temperature observations of the most active station \
    for the last year of data. Return a JSON list of temperature observations \
    (TOBS) for the previous year."
    last_twelve_mos = dt.datetime(2017, 8, 23) - dt.timedelta(days = 365)
    twelve_mos_temps = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= last_twelve_mos).all()
    return jsonify(twelve_mos_temps)

if __name__ == "__main__":
    app.run(debug=True)
