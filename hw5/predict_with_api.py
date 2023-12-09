from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI()
classifire = pipeline("sentiment-analysis")

@app.get("/")
def root():
    """Тестовое сообщение для проверки работоспособности"""
    return {"message": "Wellcome to app!"}

@app.post("/predict")
def predict(item: Item):
    """Предсказание настроения текста"""
    return classifire(item.text)[0]