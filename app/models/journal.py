from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.models.base import Base

class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))
    date = Column(Date)
    grade = Column(Integer)
    lesson_type = Column(String(20))   # текущий, практическая, контрольная и т.д.

    student = relationship("Student", back_populates="grades")