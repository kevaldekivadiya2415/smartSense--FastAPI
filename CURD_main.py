from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

students = {
    1 : {  
            "name" : "keval",
            "age" : 21,
            "year" : "year 4"
    }
}

class Student(BaseModel):
    name : str
    age : int
    year : str

class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None 


@app.get("/get-student/{student_id}")
def get_student(student_id :int):
    if student_id in students.keys():
        return students[student_id]
    return {"Data" : "Not Found"}

'''#Query Parameter 
@app.get("/get-by-name")
def get_student(name : Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data" : "Not found"} '''


@app.post("/create-student/{student_id}")
def create_student(student_id : int ,student : Student):
    if student_id in students:
        return {"Error" : "Student exists"}

    students[student_id] = student
    return students[student_id]

@app.put("/student-update/{student_id}")
def update_student(student_id : int , student : UpdateStudent):
    if student_id not in students:
        return {"Error" : "Student does not exist"}
    

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year
        
    return students[student_id]

@app.delete("/student-delete/{student_id}")
def student_delete(student_id : int):
    if student_id in students.keys():
        del students[student_id]
        return {"Message" : "Student deleted successfully"}
    else:
        return {"Error" : "Student does not exist"}



