from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LessonBase(BaseModel):
    group_id: int
    subject_id: int
    employee_id: int
    classroom: str
    start_time: datetime
    end_time: datetime
    lesson_type: Optional[str] = "лекция"

class LessonCreate(LessonBase):
    pass

class LessonOut(LessonBase):
    id: int

    class Config:
        from_attributes = True