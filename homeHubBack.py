from fastapi import FastAPI
from os import listdir
from os.path import isfile, join


app = FastAPI()

@app.get('/')
def hello():
    return {"Hello": "World"}

@app.get('/gettemperatures')
def getTemperatures():
    mypath = "/var/www/html/data"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return {"sensors.count": len(onlyfiles)}