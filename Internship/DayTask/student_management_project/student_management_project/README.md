# Student Management System

A small student CRUD project made with FastAPI, a JSON file, HTML, CSS and JavaScript.

## Project files

- `main.py` — API routes and the page entry point.
- `schema.py` — checks the student data sent to the backend.
- `student_data.json` — stores the student records.
- `static/index.html` — page layout.
- `static/style.css` — page design.
- `static/app.js` — connects the page to the API.
- `requirements.txt` — Python packages needed for the project.

## Run the project

1. Install Python 3.10 or newer.
2. Open a terminal inside this project folder.
3. (Optional but recommended) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows:

   ```bash
   .venv\\Scripts\\activate
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

4. Install the packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the server:

   ```bash
   uvicorn main:app --reload
   ```

6. Open `http://127.0.0.1:8000` in your browser.

You can also open `http://127.0.0.1:8000/docs` to test the API routes.

## What you can do

- View all students and their placement status.
- Add a student with a unique roll number.
- Edit the details of an existing student.
- Delete a student record.
- See helpful messages if a roll number is already used or a record does not exist.

The records are saved in `student_data.json`. Keep the server running while using the page.
