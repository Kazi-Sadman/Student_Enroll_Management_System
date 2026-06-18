from pydantic import BaseModel
from typing import List
from datetime import datetime

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int
    semester:int

class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    course_id: int
    semester :int
    enrolled_at: datetime

    class Config:
        # Tells Pydantic to read attributes directly from SQLAlchemy objects
        from_attributes = True

# Minimal Student details schema for relationship nesting
class StudentMinResponse(BaseModel):
    student_id: int
    name: str
    email: str
    
    class Config:
        from_attributes = True

class CourseMinResponse(BaseModel):
    id: int
    title: str
    code: str
    
    class Config:
        from_attributes = True