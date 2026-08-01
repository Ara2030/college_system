from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base
from app.models.department import Department

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)      # Например: "ПИ-31"
    speciality = Column(String(100))
    course = Column(Integer)

    # Добавлена связь с отделением
    department_id = Column(Integer, ForeignKey("departments.id"))

    # Добавлены back_populates для согласованности
    students = relationship("Student", back_populates="group")
    lessons = relationship("Lesson", back_populates="group")
    department = relationship("Department", back_populates="groups")