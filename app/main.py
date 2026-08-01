import sys
import os

# Добавляем корневую директорию в path, чтобы работали абсолютные импорты
# Это нужно, если запускаешь скрипт из любой папки
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Импортируем БД
from app.database import engine, init_db
from app.models.base import Base
# ВАЖНО: Явно импортируем все модели, чтобы SQLAlchemy знал о них при создании таблиц
from app.models import (
    Student, Group, Employee, Subject, Grade, Lesson, Attestation, Order, StudentStatus
)

# Импортируем роутеры
from app.routers import students, groups, journal, schedule, attestation, orders

app = FastAPI(
    title="ИС Колледжа СПО",
    description="Информационная система для автоматизации деятельности СПО",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Обработчик ошибок на уровне всего приложения (полезно для отладки)
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    print(f"Global Error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": f"Внутренняя ошибка сервера: {str(exc)}"}
    )

# Инициализация БД при старте
@app.on_event("startup")
def startup_event():
    try:
        print("Инициализация базы данных...")
        # Создаем таблицы. Если они уже есть, create_all не удалит их, но и не создаст дубликаты
        Base.metadata.create_all(bind=engine)
        print("База данных успешно инициализирована.")
    except Exception as e:
        print(f"Ошибка при инициализации БД: {e}")
        # Не прерываем запуск полностью, чтобы API заработал, но логируем ошибку
        # Для продакшена тут стоит остановиться, но для диплома оставим работу API

# Подключаем роутеры
app.include_router(students.router)
app.include_router(groups.router)
app.include_router(journal.router)
app.include_router(schedule.router)
app.include_router(attestation.router)
app.include_router(orders.router)

@app.get("/", tags=["Root"])
def root():
    return {"message": "API работает"}