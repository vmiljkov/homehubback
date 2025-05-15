from fastapi import FastAPI
import glob

from Constants import Constants

app = FastAPI()
sensorNames = None
@app.get('/')
def hello():
    return {"Hello": "World"}

@app.get('/gettemperatures')
def getTemperatures():
    mypath = Constants.datafolder
    sensorNames = glob.glob(mypath+"/*.data")
    return {"sensors.count": len(sensorNames)}

@app.get('/cputemp')
def getSensorValue():
    file = open(sensorNames[0])
    return {"cputemp.value": file.read()}