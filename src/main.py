import os
from fastapi import FastAPI
from dotenv import load_dotenv
from src.inference import load_model, predict
from pydantic import BaseModel

load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH")

model = load_model(MODEL_PATH)

app = FastAPI(
    title="Production ML API",
    version="1.0.0"
)

class PredictionRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
       
class PredictionResponse(BaseModel):
    prediction: int
    probability: float

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictionResponse)
def make_prediction(request: PredictionRequest):
    features = {
        "sepal length (cm)": request.sepal_length,
        "sepal width (cm)": request.sepal_width,
        "petal length (cm)": request.petal_length,
        "petal width (cm)": request.petal_width,
    }

    return predict(model, features)

