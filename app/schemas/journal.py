from pydantic import BaseModel
from datetime import date
from typing import Optional

class GradeBase(BaseModel):
    student_id: int
    subject_id: int
    employee_id: int
    date: date
    grade: int
    lesson_type: Optional[str] = "текущий"

class GradeCreate(GradeBase):
    pass

class GradeOut(GradeBase):
    id: int

    class Config:
        from_attributes = True