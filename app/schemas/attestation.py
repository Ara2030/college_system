from pydantic import BaseModel
from datetime import date
from typing import Optional

class AttestationBase(BaseModel):
    student_id: int
    subject_id: int
    exam_date: date
    grade: Optional[int] = None
    has_debt: bool = False

class AttestationCreate(AttestationBase):
    pass

class AttestationOut(AttestationBase):
    id: int

    class Config:
        from_attributes = True