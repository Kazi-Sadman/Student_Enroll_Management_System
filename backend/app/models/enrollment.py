from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Enrollment(Base):

    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)
   
    student_id = Column(Integer, ForeignKey("students.student_id"), nullable=False)
    
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    
    semester = Column(Integer, nullable= False)
    enrolled_at = Column(DateTime, default=datetime.utcnow)
    
    student = relationship("Student")
    course = relationship("Course")