from fastapi import FastAPI
from app.database import engine, Base
from app.routes import department,student,course,enrollment

#here create the database
Base.metadata.create_all(bind=engine)

app = FastAPI(title="University Course Enrollment System")

app.include_router(department.router)
app.include_router(student.router)
app.include_router(course.router)
app.include_router(enrollment.router) 
