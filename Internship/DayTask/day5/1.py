from fastapi import FastAPI

app = FastAPI()

stud = []

#create student
@app.post("/student")
def add_student(student : dict):
    stud.append(student)
    return student

#read

@app.get("/student")
def get_student():
    return stud

#update
@app.put("/student/{stud_id}")
def update_stud(stud_id : int, student : dict):
    
    for s in stud:
        if s["id"] == stud_id:
            s["name"] = student['name']
            return s
    return {"message":"student is not found for this id"}

#delete

@app.delete("/student/{stud_id}")
def del_stud(stud_id : int):
    for s in stud:
        if s["id"] == stud_id:
            stud.remove(s)
            return {"msg" : "deleted"}
        
    return {"msg" : "No key element found"}
            
    
    
