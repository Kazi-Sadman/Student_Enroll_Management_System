from fastapi import HTTPException,status
from sqlalchemy.orm import Session

from app.models.course import Course # Department is the model database class
from app.schemas.course import CourseCreate
from app.models.department import Department
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

def get_all_courses(db:Session):
    return db.query(Course).all()


def get_specificCourse(db:Session, Course_Id:int):
    course = get_course_or_404(db, Course_Id)
    return course

def delete_specific_course(db:Session, course_id:int):
    course = get_course_or_404(db, course_id)
    db.delete(course)
    db.commit()
    return {"message": "Course deleted successfully"}
    

def update_course_by_id(db:Session, course_id: int, course_update: CourseCreate):
    #check the course is exist in database or not
    course  = get_course_or_404(db, course_id)

    #validate foreignkey , check is this department_exist 
    department = db.query(Department).filter(Department.department_id == course_update.department_id).first()
    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Target Department not found. Cannot assign course to a non-existing department."
        )

    course.title = course_update.title
    course.code = course_update.code
    course.department_id = course_update.department_id
      
    db.commit()           
    db.refresh(course)   
    return course