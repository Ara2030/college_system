from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.models.base import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(150), nullable=False)
    position = Column(String(100))
    # department - это просто строка (например, "Учебная часть"), 
    # так как в модели Department нет ссылок на сотрудников
    department = Column(String(100)) 
    phone = Column(String(20))
    email = Column(String(100))
    employment_date = Column(Date)

    # Если нужно, чтобы у сотрудника были нагрузки (workload), можно оставить эту связь,
    # но модель Workload должна существовать. 
    # Для простоты диплома пока закомментируем или убедись, что модель Workload есть.
    # workload = relationship("Workload", back_populates="employee")