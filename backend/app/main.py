from fastapi import FastAPI
from app.database import engine, Base
from app.routes import department


Base.metadata.create_all(bind=engine)

app = FastAPI(title="University Course Enrollment System")

app.include_router(department.router)