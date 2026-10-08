from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to my API"}


@app.get("/student") #it directly don't give link to print we do it by the /stydent and about like that
def get_student():
    return {
        "name": "Tejas",
        "course": "Computer Engineering"
    }


@app.get("/about")
def about():
    return {
        "technology": "FastAPI",
        "language": "Python"
    }