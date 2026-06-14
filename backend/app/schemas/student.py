from pydantic import BaseModel
from app.database import get_db

class StudentCreate(BaseModel):
    name:str
    email:str
    department_id:int

class StudentResponse(BaseModel):
    student_id:int
    name:str
    email:str
    department_id:int

    class Config:
        from_attribute =True