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

@router.get("/", response_model = list[CourseResponse], status_code=status.HTTP_201_CREATED)
def get_courses(db:Session = Depends(get_db)):
    return course_service.get_all_courses(db)


# below path{id} and get_course_by_id function parameter id  name always same
@router.get("/{id}",response_model= CourseResponse, status_code=status.HTTP_201_CREATED)
def get_course_by_id(id:int,db:Session = Depends(get_db) ):
    return course_service.get_specificCourse(db, id)


@router.delete("/{cs_id}",
               status_code=status.HTTP_204_NO_CONTENT)
def delete_course_by_id(cs_id: int, db: Session = Depends(get_db)):
    course_service.delete_specific_course(db, cs_id)


@router.put("/{course_id}", response_model=CourseResponse)
def update_course(course_id: int, course_update: CourseCreate, db: Session = Depends(get_db)):
    
    return course_service.update_course_by_id(db, course_id, course_update)