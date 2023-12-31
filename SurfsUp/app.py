# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import MetaData

app = Flask(__name__)

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# Reflect an existing database into a new model
Base = automap_base()
# Reflect the tables
Base.prepare(engine, reflect=True)

# Check the table names to ensure correct reflection
metadata = MetaData()
metadata.reflect(engine)
print("Tables in the database:", metadata.tables.keys())

if ('measurement' not in Base.classes.keys() or 'station' not in Base.classes.keys()):
    raise Exception("Tables 'measurement' or 'station' not found")

Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return (
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of all precipitation data"""
    # Query all precipitation data
    results = session.query(Measurement.date, Measurement.prcp).all()
    # Create a dictionary from the row data and append to a list of all_precipitations
    all_precipitations = {date: prcp for date, prcp in results}
    return jsonify(all_precipitations)

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations"""
    # Query all stations
    results = session.query(Station.station).all()
    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return a list of temperature observations (TOBS) for the last year"""
    # Query the last year of temperature observation data for the most active station
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def start(start):
    """Return TMIN, TAVG, TMAX for all dates greater than and equal to the start date"""
    
    return jsonify(results)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    """Return TMIN, TAVG, TMAX for dates between the start and end date inclusive"""
    
    return jsonify(results)

# Define main behavior
if __name__ == '__main__':
    app.run(debug=True)