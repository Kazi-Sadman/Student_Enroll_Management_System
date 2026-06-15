from fastapi import HTTPException 
from sqlalchemy.orm import Session

from app.models.department import Department # Department is the model database class
from app.schemas.department import DepartmentCreate

def create_department(db: Session, department:DepartmentCreate):

    new_department = Department(
        name = department.name
    )
    db.add(new_department)
    db.commit()
    db.refresh(new_department)

    return new_department

