from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open("patienttrackerapp\patients.json", "r") as file:
        data= json.load(file)
        return data

@app.get("/")
def hello():
    return {"Message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"Message": "A fully functional API to manage your patient records!"}

@app.get("/view")
def view():
    data = load_data()
    return data

# Create an endpoint view to enable client vieew all patient data
# To load data from the json file we nee to create a function to load the data.
