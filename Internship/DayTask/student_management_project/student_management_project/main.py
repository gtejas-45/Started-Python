from pathlib import Path
import json

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from schema import Student

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "student_data.json"
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(title="Student Management System")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


# Open the front-end when the project starts.
@app.get("/")
def home():
    return FileResponse(STATIC_DIR / "index.html")


# These two helpers keep the JSON file handling in one place.
def read_students():
    with DATA_FILE.open("r", encoding="utf-8-sig") as file:
        return json.load(file)


def save_students(data):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


@app.get("/get_student")
def index():
    return read_students()


@app.get("/get_student/{roll}")
def get_student_record(roll: int):
    db = read_students()
    record = db.get(str(roll))
    if record is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return record


@app.post("/add_student", status_code=201)
def add_student(obj: Student):
    db = read_students()
    roll = str(obj.roll)

    if roll in db:
        raise HTTPException(status_code=409, detail="Roll number already exists")

    db[roll] = {
        "Name": obj.name,
        "Marks": obj.marks,
        "Address": obj.address,
        "Placed": obj.placed,
    }
    save_students(db)
    return {"message": "Student added successfully", "student": db[roll]}


@app.delete("/delete_student/{roll}")
def delete_student(roll: int):
    db = read_students()
    record = db.pop(str(roll), None)

    if record is None:
        raise HTTPException(status_code=404, detail="Student not found")

    save_students(db)
    return {"message": "Student deleted successfully", "Deleted Record": record}


@app.put("/edit_student/{roll}")
def edit_student(roll: int, obj: Student):
    db = read_students()
    key = str(roll)

    if key not in db:
        raise HTTPException(status_code=404, detail="Student not found")

    # The roll number in the URL decides which student is updated.
    db[key] = {
        "Name": obj.name,
        "Marks": obj.marks,
        "Address": obj.address,
        "Placed": obj.placed,
    }
    save_students(db)
    return {"message": "Student updated successfully", "student": db[key]}
