from utils.loggerFactory import LoggerFactory
from fastapi import FastAPI, Request
from utils.health_utils import calculate_bmi, calculate_bmr
from utils.payload import BMIRequest, BMRRequest
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Configure logging
logger = LoggerFactory.getLogger('Health API', "INFO")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})


@app.post('/bmi',
          status_code=200,
          tags=["BMI"],
          summary="Calculate Body Mass Index",
          description="Calculate Body Mass Index (BMI) using height (cm) and weight (kg).",
          responses={
              200: {
                  "description": "Successful Response",
                  "content": {
                      "application/json": {
                          "example": {
                              "bmi": 22.86
                          }
                      }
                  }
              },
              400: {
                  "description": "Bad Request",
                  "content": {
                      "application/json": {
                          "example": {
                              "error": "Height and weight are required"
                          }
                      }
                  }
              },
              422: {
                  "description": "Unprocessable Entity",
                  "content": {
                      "application/json": {
                          "example": {
                              "error": "Missing data"
                          }
                      }
                  }
              },
              500: {
                  "description": "Internal Server Error",
                  "content": {
                      "application/json": {
                          "example": {
                              "error": "Internal Server Error"
                          }
                      }
                  }
              }
          }
          )
async def bmi(payload: BMIRequest):
  logger.info("Received BMI request with payload: %s", payload)
  try:
    print("cc")
    bmi_value = calculate_bmi(payload.height, payload.weight)
  except ZeroDivisionError:
    logger.error("Height cannot be zero")
    return {"error": "Height cannot be zero"}, 400
  except Exception as e:
    logger.exception("An error occurred while calculating BMI")
    return {"error": str(e)}, 500

  logger.info("Calculated BMI: %f", bmi_value)
  return {"bmi": bmi_value}


@app.post('/bmr',
          status_code=200,
          tags=["BMR"],
          summary="Calculate Basal Metabolic Rate",
          description="Calculate Basal Metabolic Rate (BMR), or energy your body needs to perform basic functions, using height (cm), weight (kg), age (years) and gender (male/female).",
          responses={
              200: {
                  "description": "Successful Response",
                  "content": {
                      "application/json": {
                          "example": {
                              "bmr": 1500
                          }
                      }
                  }
              },
              400: {
                  "description": "Bad Request",
                  "content": {
                      "application/json": {
                          "example": {
                              "error": "Height, weight, age and gender are required"
                          }
                      }
                  }
              },
              422: {
                  "description": "Unprocessable Entity",
                  "content": {
                      "application/json": {
                          "example": {
                              "error": "Height cannot be zero"
                          }
                      }
                  }
              },
              500: {
                  "description": "Internal Server Error",
                  "content": {
                      "application/json": {
                          "example": {
                              "error": "Internal Server Error"
                          }
                      }
                  }
              }
          }
          )
async def bmr(payload: BMRRequest):
  logger.info("Received BMR request with payload: %s", payload)
  try:
    bmr_value = calculate_bmr(payload.height, payload.weight, payload.age, payload.gender)
  except ValueError as e:
    logger.error("ValueError: %s", str(e))
    return {"error": str(e)}, 400
  except Exception as e:
    logger.exception("An error occurred while calculating BMR")
    return {"error": str(e)}, 500

  logger.info("Calculated BMR: %f", bmr_value)
  return {"bmr": bmr_value}

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=9000)
