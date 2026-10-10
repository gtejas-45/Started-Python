
import pickle
from pathlib import Path

import pandas as pd
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

# 1. Get the folder where main.py is saved
BASE_DIR = Path(__file__).resolve().parent

# 2. Create the FastAPI application
app = FastAPI()

# 3. Load the saved ML model
MODEL_PATH = BASE_DIR / "HI_pickle.pkl"

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

# 4. Find the HTML templates folder
templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


# 5. Display the HTML page
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"prediction": None}
    )


# 6. Receive the HTML form and predict
@app.post("/predict")
def predict(
    request: Request,
    age: int = Form(...),
    sex: str = Form(...),
    bmi: float = Form(...),
    children: int = Form(...),
    smoker: str = Form(...)
):
    # 7. Convert text values to the same numbers
    # used in your notebook
    sex_enc = 1 if sex == "female" else 0
    smoke_enc = 1 if smoker == "yes" else 0

    # 8. Create input with the exact training columns
    input_data = pd.DataFrame(
        [[age, sex_enc, bmi, children, smoke_enc]],
        columns=[
            "age",
            "sex_enc",
            "bmi",
            "children",
            "smoke_enc"
        ]
    )

    # 9. Ask the trained model for a prediction
    prediction = model.predict(input_data)[0]

    # 10. Display the result on the same HTML page
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "prediction": round(float(prediction), 2)
        }
    )