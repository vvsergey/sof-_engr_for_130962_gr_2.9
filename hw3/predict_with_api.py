from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text = "text"

app = FastAPI()
classifire = pipeline("sentiment-analisys")

@app.get("/")
def root():
    return {"message": "Wellcome to app!"}

@app.post ("/predict")
def predict(item):
    return classifire(item.text)[0]