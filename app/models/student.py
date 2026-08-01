from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.models.base import Base
import enum

class StudentStatus(str, enum.Enum):
    studying = "обучается"
    expelled = "отчислен"
    academic = "академический отпуск"
    graduated = "выпущен"

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), nullable=False)
    birth_date = Column(Date)
    gender = Column(String(10))
    snils = Column(String(14), unique=True)
    passport = Column(String(20))
    address = Column(String(200))
    phone = Column(String(20))
    email = Column(String(100))
    education_doc = Column(String(150))
    group_id = Column(Integer, ForeignKey("groups.id"))
    status = Column(Enum(StudentStatus), default=StudentStatus.studying)

    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student")
    attestations = relationship("Attestation", back_populates="student")