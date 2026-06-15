from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.department import DepartmentCreate, DepartmentResponse
from app.services import department_service

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)

#add means post
@router.post("/", response_model=DepartmentResponse, status_code=status.HTTP_201_CREATED)
def add_department(department: DepartmentCreate, db: Session = Depends(get_db)):
    return department_service.create_department(db, department)

@router.get("/", response_model=list[DepartmentResponse])
def get_departments(db: Session = Depends(get_db)):
    return department_service.get_all_departments(db)

@router.get("/{department_id}", response_model=DepartmentResponse)
def get_department(department_id: int, db: Session = Depends(get_db)):
    return department_service.get_department_by_id(db, department_id)
@router.delete("/{department_id}")
def remove_department(department_id: int, db: Session = Depends(get_db)):
    return department_service.delete_department(db, department_id)