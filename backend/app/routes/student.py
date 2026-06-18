from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.student import StudentCreate 
from app.services import student_service

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_student(student_add: StudentCreate, db: Session = Depends(get_db)):
   
    return student_service.add_student(db, student_add)

@router.get("/")
def read_all_students(db: Session = Depends(get_db)):
    
    return student_service.get_all_students(db)

@router.get("/{student_id}")
def read_student_by_id(student_id: int, db: Session = Depends(get_db)):
   
    return student_service.get_student_by_id(db, student_id)

@router.put("/{student_id}")
def update_student(student_id: int, student_update: StudentCreate, db: Session = Depends(get_db)):
    
    return student_service.update_student_by_id(db, student_id, student_update)

@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return student_service.delete_student_by_id(db, student_id)