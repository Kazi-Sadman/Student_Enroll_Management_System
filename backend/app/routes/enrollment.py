from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.enrollment import EnrollmentCreate, EnrollmentResponse, StudentMinResponse, CourseMinResponse
from app.services import enrollment_service

router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)


@router.post("/", response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED)
def enroll_student(enrollment_data: EnrollmentCreate, db: Session = Depends(get_db)):
    return enrollment_service.create_enrollment(db, enrollment_data)

@router.get("/", response_model=List[EnrollmentResponse])
def read_all_enrollments(db: Session = Depends(get_db)):
    return enrollment_service.get_all_enrollments(db)

# Endpoint 3: GET /students/{id}/courses (Declared outside standard prefix using full override path)
@router.get("/students/{student_id}/courses", response_model=List[CourseMinResponse], tags=["Students"])
def read_courses_by_student(student_id: int, db: Session = Depends(get_db)):
    return enrollment_service.get_courses_by_student(db, student_id)

# Endpoint 4: GET /courses/{id}/students (Declared outside standard prefix using full override path)
@router.get("/courses/{course_id}/students", response_model=List[StudentMinResponse], tags=["Courses"])
def read_students_by_course(course_id: int, db: Session = Depends(get_db)):
    return enrollment_service.get_students_by_course(db, course_id)


@router.delete("/{enrollment_id}")
def cancel_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    return enrollment_service.delete_enrollment(db, enrollment_id)