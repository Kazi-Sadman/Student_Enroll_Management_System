from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.department import Department
from app.schemas.department import DepartmentCreate

def get_department_or_404(db: Session, department_id:int)-> Department:
    department = db.query(Department).filter(Department.department_id == department_id).first()

    if not department:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail = detail="Department not found"
        )
    return department

def create_department(db:Session, department_data: DepartmentCreate):

    new_dept = Department(name = department_data.name)
    db.add(new_dept)
    db.commit()
    db.refresh(new_dept)
    return new_dept

def get_all_departments(db:Session):
    return db.query(Department).all()

def get_department_by_id(db:Session, department_id: int):
    return get_department_or_404(db, department_id)
    
def delete_department(db:Session, department_id:int):
    department = get_department_or_404(db, department_id)
    db.delete(department)
    db.commit()

    return {"message": "Department deleted successfully"}