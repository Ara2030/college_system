from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.models.base import Base

class Attestation(Base):
    __tablename__ = "attestations"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    exam_date = Column(Date)
    grade = Column(Integer)
    has_debt = Column(Boolean, default=False)
    student = relationship("Student", back_populates="attestations")
    subject = relationship("Subject") 