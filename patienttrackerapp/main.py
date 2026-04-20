from fastapi import FastAPI, Path, HTTPException, Query
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
    # return {'error':'patient not found'}   # Displays error code 200 instead of 404

    raise HTTPException(status_code=404,detail='Patient Not Found')

@app.get("/sort")
def sort_patients(sort_by:str = Query(..., description='Field to sort by height, weight, age etc'), order:str = Query('asc',description='Sort order: asc or desc')):
    data = load_data()
    if sort_by not in ['height', 'weight', 'age']:
        raise HTTPException(status_code=400, detail='Invalid sort field')
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid sort order')
    
    
    sorted_data = sorted(data.items(), key=lambda x: x[1].get(sort_by, 0), reverse=(order=='desc'))
    return {k: v for k, v in sorted_data}
# Create an endpoint view to enable client vieew all patient data
# To load data from the json file we nee to create a function to load the data.
