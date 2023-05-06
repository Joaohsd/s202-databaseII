from pymongo import MongoClient
from bson.objectid import ObjectId

from threading import Thread

import time
import random

#######################################################
# Function that will be executed when the Thread start
#######################################################
def sampleGenerator(id: str, name:str, min:float, max:float, samplingRate:int, durationInSeconds:float):
    # Connection
    client = MongoClient('mongodb://localhost:27017')
    db = client['bancoiot']
    sensors = db.sensores
    # Compute time to generate samples
    start = time.time() * 1000
    end = start + durationInSeconds * 1000
    now = time.time() * 1000
    # Flag
    broken = False
    # Gerating samples
    while end > now:
        # Not broken
        if not broken:
            sample = min + (max - min) * random.random()
            sensors.update_one({"_id": ObjectId(id)}, {"$set":{"valorSensor":sample, "sensorAlarmado":(sample > 38)}})
            print('Generated sample', sample, 'for sensor', name)
        # Broken
        if sample > 38:
            broken = True
            print('Warning! Temperature is so high! Verify the sensor', name, "!")
        time.sleep(1.0/samplingRate)
        now = time.time() * 1000
    time.sleep(0.01)

###########################################################################################
# The number of threads depends on the number of parameters registered on bancoiot database
###########################################################################################
def main():
    # Connection
    client = MongoClient('mongodb://localhost:27017')
    db = client['bancoiot']
    sensors = db.sensores

    # Variables
    durationInSeconds = 10
    minTemperature = 30
    maxTemperature = 40
    samplingRate = 10

    # Get all parameters registered
    parameters = sensors.find()

    # Start thread for each parameter
    for parameter in parameters:
        sensor = Thread(target=sampleGenerator, args=(parameter['_id'], parameter['nomeSensor'], minTemperature, maxTemperature, samplingRate, durationInSeconds))
        sensor.start()

if __name__ == "__main__":
    main()
        
