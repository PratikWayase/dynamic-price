
# 1. Library imports
import uvicorn
from fastapi import FastAPI
import numpy as np
import pickle
import pandas as pd

# 2. Create the app object
app = FastAPI()
pickle_in = open("model2.pkl","rb")
model2=pickle.load(pickle_in)  

class InputData(BaseModel):
    Number_of_Riders: int
    Number_of_Drivers: int
    Expected_Ride_Duration: int

@app.post("/predict")
async def predict(input_data: InputData):
    # Convert input data to NumPy array
    input_array = np.array([[input_data.Number_of_Riders, input_data.Number_of_Drivers, input_data.Expected_Ride_Duration]])

    # Make prediction using the loaded model
    prediction = model.predict(input_array).tolist()

    return {"prediction": prediction}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)


