from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return {"Hello": "World"}

@app.get('/gettemperatures')
def hello():
    return {"gettemmain.pyperatures": "tralala  "}