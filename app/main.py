from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"Message": "Hello World!"}

@app.get("/about")
def about():
    return {"Sandesh": "This is my first route!"}