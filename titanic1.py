from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

# Loading saved model
model = joblib.load('titanic_random_forest.pkl')

# Loading the columns list to ensure alignment
model_columns = joblib.load('model_columns.pkl')

#i'm defining what user must send
class PassengerData(BaseModel):
    Pclass: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Sex: str        # e.g., 'male' or 'female'
    Embarked: str   # e.g., 'S', 'C', or 'Q'
    Title: str      # e.g., 'Mr', 'Miss', 'Mrs'

#turning user input into a dataframe and making prediction
@app.post("/predict")
def predict(data: PassengerData):
    # 1. Convert the Pydantic object to a dictionary, then a DataFrame
    input_df = pd.DataFrame([data.model_dump()])

    # 2. Apply One-Hot Encoding (same as you did in training)
    input_df = pd.get_dummies(input_df, columns=['Sex', 'Embarked', 'Title'])

    # 3. THE CRITICAL STEP: Re-index
    # This adds missing columns as 0 and removes extra ones to match the model
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    # 4. Make the Prediction
    prediction = model.predict(input_df)
    
    # Convert result to a human-readable format
    result = "Survived" if prediction[0] == 1 else "Did Not Survive"

    return {"prediction": result, "status_code": 1 if prediction[0] == 1 else 0}

