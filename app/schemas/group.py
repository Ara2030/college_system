from pydantic import BaseModel
from typing import Optional

class GroupBase(BaseModel):
    name: str
    speciality: Optional[str] = None
    course: Optional[int] = None

class GroupCreate(GroupBase):
    pass

class GroupOut(GroupBase):
    id: int

    class Config:
        from_attributes = True