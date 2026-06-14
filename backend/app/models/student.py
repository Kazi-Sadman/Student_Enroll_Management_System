from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index = True)
    name = Column(String, nullable=True)
    email = Column(String, unique =True, nullable=True)
    department_id = Column(Integer, ForeignKey("departments.department_id"))

    department = relationship("Department")