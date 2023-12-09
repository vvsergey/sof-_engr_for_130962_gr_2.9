from fastapi.testclient import TestClient
from predict_with_api import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wellcome to app!"}

def test_read_predict_positive():
    response = client.post("/predict/",
        json={"text": "I helped a grateful grandmother cross the road"}
    )
    json_data = response.json() 
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'

def test_read_predict_negative():
    response = client.post("/predict/",
        json={"text": "This nasty upstart ruined my whole mood"}
    )
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'