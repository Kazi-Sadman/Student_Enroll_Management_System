# import for data validation
from pydantic import BaseModel
from app.models.course import Course
class CourseCreate(BaseModel):
    
    title : str
    code : str
    department_id : int


class CourseResponse(BaseModel):

    id:int
    title:str
    code:str
    department_id:int

    class config:
       from_attributes = True