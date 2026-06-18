from sqlalchemy import Column , Integer, String, ForeignKey
from sqlalchemy.orm import relationship
#all class inherit deraivative_bas() class and it is store in Base
from app.database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key= True, nullable= False)
    title = Column(String, nullable= False)
    code = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
