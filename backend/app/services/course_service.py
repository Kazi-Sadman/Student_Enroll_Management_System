from fastapi import HTTPException,status
from sqlalchemy.orm import Session

from app.models.course import Course # Department is the model database class
from app.schemas.course import CourseCreate

def get_course_or_404(db:Session, course_id :int):

    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        raise HTTPException(
           status_code = status.HTTP_404_NOT_FOUND,
            detail= "course not found"
        )
    return course

# add course we need all infomation of course so course_data type is CourseCreate
def create_course(db:Session, course_data: CourseCreate):

    # at first we check the course is exist or not
    existing_course = db.query(Course).filter(Course.title == course_data.title).first()
    # if already exist the course
    if  existing_course:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail="This course is already Exist"
        )
    # if course is already not exist then add the courese

    new_course = Course(
        title = course_data.title,
        code = course_data.code,
       # give same column name you give in models
        department_id = course_data.department_id
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course



