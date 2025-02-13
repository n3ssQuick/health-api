from enum import Enum
from pydantic import BaseModel, field_validator, ValidationError
from utils.loggerFactory import LoggerFactory

# Create a logger instance
logger = LoggerFactory.getLogger('Payload', "INFO")


class Gender(str, Enum):
  male = "male"
  female = "female"


class BMIRequest(BaseModel):
  height: float
  weight: float

  @field_validator('height', 'weight', mode='after')
  @classmethod
  def check_positive(cls, value, info):
    if value <= 0:
      logger.error(f'Validation error: {info.field_name} must be greater than 0')
      raise ValueError(f'{info.field_name} must be greater than 0')
    logger.debug(f'{info.field_name} is valid: {value}')
    return value

  model_config = {
      "json_schema_extra": {
          "examples": [
              {
                  "height": 175,
                  "weight": 70
              }
          ]
      }
  }


class BMRRequest(BaseModel):
  height: float
  weight: float
  age: float
  gender: Gender

  @field_validator('height', 'weight', 'age', mode='after')
  @classmethod
  def check_positive(cls, value, info):
    if value <= 0:
      logger.error(f'Validation error: {info.field_name} must be greater than 0')
      raise ValueError(f'{info.field_name} must be greater than 0')
    logger.debug(f'{info.field_name} is valid: {value}')
    return value

  model_config = {
      "json_schema_extra": {
          "examples": [
              {
                  "height": 175,
                  "weight": 70,
                  "age": 25,
                  "gender": "female"
              }
          ]
      }
  }
