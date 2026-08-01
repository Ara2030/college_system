from pydantic import BaseModel
from datetime import date
from typing import Optional
from enum import Enum

class StudentStatus(str, Enum):
    studying = "обучается"
    expelled = "отчислен"
    academic = "академический отпуск"
    graduated = "выпущен"

class StudentBase(BaseModel):
    full_name: str
    birth_date: Optional[date] = None
    snils: Optional[str] = None
    group_id: Optional[int] = None
    status: StudentStatus = StudentStatus.studying

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    full_name: Optional[str] = None
    group_id: Optional[int] = None
    status: Optional[StudentStatus] = None

class StudentOut(StudentBase):
    id: int

    class Config:
        from_attributes = True