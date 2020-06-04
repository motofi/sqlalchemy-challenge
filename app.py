# IP: 127.0.0.1
# Port: 5000
# endpoint (but not yet defined): /
# localhost:5000
# or
# 127.0.0.1:5000
# in browser should take me to the page

# 1. import Flask
from flask import Flask, jsonify

# Set up Flask
# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# 3. Home Page
# Define what to do when a user hits the index route
@app.route("/")
def welcome():
    "List all available api routes."
    return (
    f"Available Routes:<br/>"
    f"/api/v1.0/precipitation<br/>"
    f"/api/v1.0/stations<br/>"
    f"/api/v1.0/tobs<br/>"
    f"/api/v1.0/<start><br/>"
    f"/api/v1.0/<start>/<end><br/>"
    )

# List all the routes that are available
#
# @app.route("/api/v1.0/precipitation")
# Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
#
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


if __name__ == "__main__":
    app.run(debug=True)
