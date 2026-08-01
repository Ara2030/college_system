from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, models
from app.database import get_db

router = APIRouter(prefix="/journal", tags=["Journal"])

@router.post("/grades", response_model=schemas.GradeOut)
def create_grade(grade: schemas.GradeCreate, db: Session = Depends(get_db)):
    db_grade = models.Grade(**grade.model_dump())
    db.add(db_grade)
    db.commit()
    db.refresh(db_grade)
    return db_grade

@router.get("/grades", response_model=List[schemas.GradeOut])
def get_grades(db: Session = Depends(get_db)):
    return db.query(models.Grade).all()