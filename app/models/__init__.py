from .base import Base

# Явно импортируем все модели
from .department import Department
from .group import Group
from .student import Student, StudentStatus
from .employee import Employee
from .subject import Subject
from .journal import Grade
from .schedule import Lesson
from .attestation import Attestation
from .order import Order

# Экспорт
__all__ = [
    "Base",
    "Group",
    "Student",
    "StudentStatus",
    "Employee",
    "Subject",
    "Grade",
    "Lesson",
    "Attestation",
    "Order",
]