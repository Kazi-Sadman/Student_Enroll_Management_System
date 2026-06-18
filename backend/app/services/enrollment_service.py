from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.enrollment import Enrollment
from app.models.student import Student
from app.models.course import Course
from app.schemas.enrollment import EnrollmentCreate
from sqlalchemy.orm import joinedload

def get_enrollment_or_404(db: Session, enrollment_id: int) -> Enrollment:
    enrollment = db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()
    if not enrollment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Enrollment record not found"
        )
    return enrollment

# 1. Core Logic: POST /enrollments
def create_enrollment(db: Session, enrollment_data: EnrollmentCreate):
    # Step A: Validate  foreign key if the Student actually exists in the system
    student = db.query(Student).filter(Student.student_id == enrollment_data.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
        
    # Step B: Validate Foreign key if the Course actually exists in the system
    course = db.query(Course).filter(Course.id == enrollment_data.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    #3 check duplicate , is the student already entered the course
    existing_enrollment = db.query(Enrollment).filter(
        Enrollment.student_id == enrollment_data.student_id,
        Enrollment.course_id == enrollment_data.course_id
    ).first()
    if existing_enrollment:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student is already enrolled in this course"
        )

    # Step D: Save transaction to database
    new_enrollment = Enrollment(
        student_id=enrollment_data.student_id,
        course_id=enrollment_data.course_id,
        semester = enrollment_data.semester
    )
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    return new_enrollment

def get_all_enrollments(db:Session):
    return db.query(Enrollment).all()

# 3. Core Logic: GET /students/{id}/courses
# means get all courses that is enroll by student 1 or 2----
def get_courses_by_student(db:Session, student_id:int):

    #1 verify student exist or not by that id
    student = db.query(Student).filter(Student.student_id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    #We are retrieving all Course objects that are linked to a specific student through the Enrollment table.

    #get all courses that enroll by student 1--2--3 from 
    #join two table in many to many relationship
    enrollments = db.query(Enrollment).filter(Enrollment.student_id == student_id).all()
    #List comprehension
    return [enrollment.course for enrollment in enrollments]


# 4. Core Logic: GET /courses/{id}/students
#means give me all students that enroll in course 1
def get_students_by_course(db: Session, course_id: int):
    # Verify course exists first
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
        
    # Query all enrollments for this course and extract the linked Student objects
    enrollments = db.query(Enrollment).filter(Enrollment.course_id == course_id).all()
    return [enrollment.student for enrollment in enrollments]

# 5. Core Logic: DELETE /enrollments/{id}
def delete_enrollment(db: Session, enrollment_id: int):
    enrollment = get_enrollment_or_404(db, enrollment_id)
    db.delete(enrollment)
    db.commit()
    return {"message": "Student un-enrolled from course successfully"}