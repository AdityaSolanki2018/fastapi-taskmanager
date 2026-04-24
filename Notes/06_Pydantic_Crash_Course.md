# Pydantic

## Why?

When we are working on Production Grade code, we require type validation.
Pydantic solves 2 major problems: -

lets say we have a funtion to handle patient data and enter it to DB

'''
def insert_patient_data(name,age):
print(name)
print(age)
print("inserted to database")

insert_patient_data('nitish','thirty')
'''
If we requre age as int but we are given age as string - how can we enforce this?
we can use if else and raise TypeError but it is not scalable for large number of parameters and many functions.

The second problem is that if we want to make sure that the age is always non-negative then what we will do? Again use if else for each variable.

so pydantic solves these type and data validation problems

## How pydantic works?

1. Define a Pydantic model that represents the ideal schema of the data/
   -> This includes the expected fields, their types, and any validation constraints(eg gt=0 for age)

2. Instantiate the model with eaw input data (usually a dictionary or a JSON-like structure)
   -> Pydantic will automatically validate the data and coerce it into the correct Python types (if possible)

-> If data dosent meet the model's requirements, Pydantic raises a ValidationError.

3. Pass the validated model object to functions or use it throughout your codebase.
   -> This ensures that every part of your program works with clean, type-safe, and logically validate data.
