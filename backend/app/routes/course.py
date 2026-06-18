from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db

from app.schemas.course import CourseCreate, CourseResponse
from app.services import course_service

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_course(course_add:CourseCreate,  db:Session = Depends(get_db)):
    return course_service.create_course(db, course_add)