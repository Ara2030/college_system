from pydantic import BaseModel
from datetime import date
from typing import Optional

class OrderBase(BaseModel):
    order_number: str
    order_date: date
    order_type: str
    content: Optional[str] = None
    student_id: Optional[int] = None

class OrderCreate(OrderBase):
    pass

class OrderOut(OrderBase):
    id: int

    class Config:
        from_attributes = True