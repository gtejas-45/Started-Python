import joblib
import pandas as pd

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal

# Load the trained model
try:
    saved_data = joblib.load("student_model.joblib")
    model = saved_data["model"]
    model_columns = saved_data["columns"]
    metrics = saved_data["metrics"]
except FileNotFoundError as exc:
    raise RuntimeError(
        "Model file not found. Run: python train_model.py"
    ) from exc

app = FastAPI(title="Student Final Exam Score Prediction API")


# Validate the data received from the user
class StudentDetails(BaseModel):
    age: int = Field(ge=17, le=24)
    gender: Literal["Male", "Female", "Other"]
    study_hours_per_day: float = Field(ge=0.5, le=8)
    attendance_percentage: float = Field(ge=42.5, le=100)
    previous_exam_score: float = Field(ge=20, le=98)
    assignments_completed_percentage: float = Field(ge=29, le=100)
    sleep_hours: float = Field(ge=4, le=10)
    social_media_hours: float = Field(ge=0, le=6.5)
    practice_tests_completed: int = Field(ge=0, le=14)


@app.get("/")
def home():
    return {"message": "Student Score Prediction API is running"}


@app.post("/predict")
def predict(student: StudentDetails):
    try:
        # Convert input into a one-row DataFrame
        data = pd.DataFrame([student.model_dump()])

        # Encode gender the same way as during training
        data = pd.get_dummies(data, columns=["gender"], dtype=int)

        # Match the training columns and their order
        data = data.reindex(columns=model_columns, fill_value=0)

        # Predict the final examination score
        prediction = float(model.predict(data)[0])

        return {"predicted_final_exam_score": round(prediction, 2)}

    except (ValueError, TypeError, KeyError) as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.get("/model-info")
def model_info():
    return {
        "algorithm": "Multiple Linear Regression",
        "target": "final_exam_score",
        "features": model_columns,
        "metrics": metrics
    }
