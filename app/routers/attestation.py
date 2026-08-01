from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app import schemas, models
from app.database import get_db

router = APIRouter(prefix="/attestation", tags=["Attestation"])

@router.post("/", response_model=schemas.AttestationOut)
def create_attestation(record: schemas.AttestationCreate, db: Session = Depends(get_db)):
    db_record = models.Attestation(**record.model_dump())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

@router.get("/", response_model=List[schemas.AttestationOut])
def get_attestations(student_id: Optional[int] = None, db: Session = Depends(get_db)):
    query = db.query(models.Attestation)
    if student_id:
        query = query.filter(models.Attestation.student_id == student_id)
    return query.all()