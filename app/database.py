from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_CONFIG

# Создаем движок
engine = create_engine(
    DATABASE_CONFIG["url"],
    connect_args=DATABASE_CONFIG["connect_args"]
)

# Создаем фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Генератор сессии для Dependency Injection"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Функция создания таблиц. Вызывается из main.py, но модели там уже импортированы."""
    from app.models.base import Base
    # Эта функция теперь просто дублирует логику, но может быть вызвана отдельно
    Base.metadata.create_all(bind=engine)