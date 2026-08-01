from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from app.models.base import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    order_number = Column(String(30), unique=True)
    order_date = Column(Date)
    order_type = Column(String(50))      # зачисление, отчисление, перевод и т.д.
    content = Column(Text)
    student_id = Column(Integer, ForeignKey("students.id"))