# Student Final Exam Score Prediction API

A simple FastAPI REST API that predicts a student's final examination score using Multiple Linear Regression.

## Files

- `student_performance_dataset.csv` — dataset used for training
- `train_model.py` — trains and evaluates the model
- `student_model.joblib` — saved trained model, columns, and metrics
- `main.py` — FastAPI endpoints
- `requirements.txt` — required Python libraries
- `evidence/` — save your API testing screenshots here

## 1. Install packages

```bash
pip install -r requirements.txt
```

## 2. Train the model

```bash
python train_model.py
```

This prints MAE, MSE, RMSE, and R², and creates `student_model.joblib`.

## 3. Start the API

```bash
uvicorn main:app --reload
```

## 4. Test with Swagger UI

Open http://127.0.0.1:8000/docs

### GET /

Checks whether the API is running.

### POST /predict

Example request body:

```json
{
  "age": 20,
  "gender": "Male",
  "study_hours_per_day": 4.0,
  "attendance_percentage": 80.0,
  "previous_exam_score": 65.0,
  "assignments_completed_percentage": 85.0,
  "sleep_hours": 7.0,
  "social_media_hours": 2.0,
  "practice_tests_completed": 5
}
```

The API returns the predicted final exam score.

### GET /model-info

Returns the model algorithm, features, and evaluation metrics.

## Input validation

Pydantic checks field types and ranges. Invalid inputs receive a validation error (HTTP 422).

The numerical ranges are based on the values in the supplied dataset; they are for this project demo and not universal student limits.

## Evaluation metrics

- MAE: Mean Absolute Error
- MSE: Mean Squared Error
- RMSE: Root Mean Squared Error
- R²: R-squared score

Actual metric values are printed when `train_model.py` runs.

## API testing evidence

Run the API and take screenshots from Swagger UI:
1. `GET /` successful response
2. `POST /predict` request and response
3. `GET /model-info` metrics
4. Invalid request showing validation error

Save the screenshots in the `evidence` folder.
