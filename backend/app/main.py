from fastapi import FastAPI
from app.database import engine, Base
from app.routes import department
from app.routes import student
from app.routes import course
#here create the database
Base.metadata.create_all(bind=engine)

app = FastAPI(title="University Course Enrollment System")

app.include_router(department.router)
app.include_router(student.router)
app.include_router(course.router)