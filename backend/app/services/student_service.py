from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.department import Department
from app.models.student import Student 
from app.schemas.student import StudentCreate

def add_student(db:Session, student_add:StudentCreate):
    #write query for department id 
    department = (db.query(Department).filter(Department.department_id == student_add.department_id).first())
    
    #Department, Student is class/table that we create in models
    #Check the logic  if department not exist
    if not department:
        raise HTTPException(
            status_code= 404,
            detail="department not found"
        )
    
    #if department is exist then store it in a variable
    new_student = Student(
        name = student_add.name,
        email = student_add.email,
        department_id = student_add.department_id
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student

#get or retrieve all student
def get_all_students(db:Session):
    students = (db.query(Student).all())
    return students

def get_student_by_id(db:Session, student_id:int):

    #get student by id from model file class schema Student
    studentBy_id = (db.query(Student).filter(Student.student_id == student_id).first())

    if not studentBy_id:
        raise HTTPException(
            status_code = 404,
            detail = "studnet not found"
        )
    return studentBy_id


def update_student_by_id(db:Session, student_id:int):

    student = (db.query(Student).filter(Student.student_id == student_id).first())
    if not student:
        raise HTTPException(
            status_code = 404,
            detail = "Student not found"
        )
    
    student.name = name
    student.email = email
    db.commit()
    db.refresh(student)
    return student

def delete_student_by_id(db:Session, student_id:int):

        student = (db.query(Student).filter(Student.student_id == student_id).first())

        if not student:
            raise HTTPException(
                status_code=404,
                detail="student not found"
            )
        db.delete(student)
        db.commit()
        return {"message": "Student deleted successfully"}

            