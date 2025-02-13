import pytest
from utils.payload import BMIRequest, BMRRequest, Gender
from utils.health_utils import calculate_bmi, calculate_bmr
from utils.payload import BMIRequest, BMRRequest
from utils.loggerFactory import LoggerFactory

logger = LoggerFactory.getLogger('Test Health Utils', "INFO")


def test_health_functions():
  assert calculate_bmi(175, 70) == 22.86
  assert calculate_bmr(175, 70, 25, 'male') == 1724.05
  assert calculate_bmr(175, 70, 25, 'female') == 1528.78
  logger.info("Health functions test passed")


def test_bmi_valid():
  payload = BMIRequest(height=175, weight=70)
  assert payload.height == 175
  assert payload.weight == 70
  logger.info("BMIRequest Payload test passed")


def test_bmi_invalid_height():
  with pytest.raises(ValueError) as excinfo:
    BMIRequest(height=-175, weight=70)
  assert "height must be greater than 0" in str(excinfo.value)
  logger.info("BMIRequest variable height test passed")


def test_bmi_invalid_weight():
  with pytest.raises(ValueError) as excinfo:
    BMIRequest(height=175, weight=0)
  assert "weight must be greater than 0" in str(excinfo.value)
  logger.info("BMIRequest variable weight test passed")


def test_bmr_valid():
  payload = BMRRequest(height=175, weight=70, age=25, gender=Gender.male)
  assert payload.height == 175
  assert payload.weight == 70
  assert payload.age == 25
  assert payload.gender == Gender.male
  logger.info("BMRRequest Payload test passed")


def test_bmr_invalid_height():
  with pytest.raises(ValueError) as excinfo:
    BMRRequest(height=0, weight=70, age=25, gender=Gender.female)
  assert "height must be greater than 0" in str(excinfo.value)
  logger.info("BMRRequest variable height test passed")


def test_bmr_invalid_weight():
  with pytest.raises(ValueError) as excinfo:
    BMRRequest(height=175, weight=-70, age=25, gender=Gender.female)
  assert "weight must be greater than 0" in str(excinfo.value)
  logger.info("BMRRequest variable weight test passed")


def test_bmr_invalid_age():
  with pytest.raises(ValueError) as excinfo:
    BMRRequest(height=175, weight=70, age=-1, gender=Gender.female)
  assert "age must be greater than 0" in str(excinfo.value)
  logger.info("BMRRequest variable age test passed")
