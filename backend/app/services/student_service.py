
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.department import Department
from app.models.student import Student 
from app.schemas.student import StudentCreate


def get_student_or_404(db:Session, student_id:int)->Student:
    #here we check student exit or not
    students = (db.query(Student).filter(Student.student_id == student_id).first())
    if not students:
        raise HTTPException(
            status_code= 404,
            detail="Student not found"
        )
    return students

def add_student(db:Session, student_add:StudentCreate):
    # before add student in a department , here we check department exist or not
    #if department is exist then store it in a variable
    department = db.query(Department).filter(Department.department_id == student_add.department_id).first()
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
        
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
    studentBy_id = get_student_or_404(db, student_id)
    return studentBy_id


def update_student_by_id(db:Session, student_id:int, student_update: StudentCreate):

    student = get_student_or_404(db, student_id)
    student.name = student_update.name
    student.email = student_update.email
    student.department_id = student_update.department_id
    db.commit()
    db.refresh(student)
    return student

def delete_student_by_id(db:Session, student_id:int):

        student = get_student_or_404(db, student_id)
        db.delete(student)
        db.commit()
        return {"message": "Student deleted successfully"}

