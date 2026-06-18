
from pydantic import BaseModel
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
        #RESPONSE DATA ARE IN OBJECT FROM SO THIS CONVERT THE DATA IN DICTIONARY SO THAT PYTHON CAN UNDERSTAND
        from_attribute =True
