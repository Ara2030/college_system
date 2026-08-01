from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))
    classroom = Column(String(20))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    lesson_type = Column(String(30))   # лекция, практика, лабораторная

    group = relationship("Group", back_populates="lessons")