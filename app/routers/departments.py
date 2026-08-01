from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, models
from app.database import get_db

router = APIRouter(prefix="/departments", tags=["Departments"])

@router.post("/", response_model=schemas.DepartmentOut)
def create_department(dep: schemas.DepartmentCreate, db: Session = Depends(get_db)):
    db_dep = models.Department(**dep.model_dump())
    db.add(db_dep)
    db.commit()
    db.refresh(db_dep)
    return db_dep

@router.get("/", response_model=List[schemas.DepartmentOut])
def get_departments(db: Session = Depends(get_db)):
    return db.query(models.Department).all()