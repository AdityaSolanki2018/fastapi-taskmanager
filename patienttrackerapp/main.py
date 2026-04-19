from fastapi import FastAPI, Path, HTTPException
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

@app.get("/patient/{patient_id}")
def view_patient(patient_id:str = Path(..., description='ID of Patient', example='P001')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    # return {'error':'patient not found'}
    raise HTTPException(status_code=404,detail='Patient Not Found')


# Create an endpoint view to enable client vieew all patient data
# To load data from the json file we nee to create a function to load the data.
