from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_bmi_success():
  payload = {"height": 170, "weight": 70}
  response = client.post("/bmi", json=payload)
  assert response.status_code == 200
  data = response.json()
  assert "bmi" in data
  print("BMI test réussi avec la valeur :", data["bmi"])


def test_bmr_success():
  payload = {"height": 170, "weight": 70, "age": 30, "gender": "male"}
  response = client.post("/bmr", json=payload)
  assert response.status_code == 200
  data = response.json()
  assert "bmr" in data
  print("BMR test réussi avec la valeur :", data["bmr"])
