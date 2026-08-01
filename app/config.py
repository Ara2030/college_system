import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL не установлен! Проверь docker-compose.yml")

# Для SQLite (если хочется локально без докера, закомментируй блок выше и раскомментируй строку ниже)
# DATABASE_URL = "sqlite:///./college_is.db"

if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}
else:
    connect_args = {}

DATABASE_CONFIG = {
    "url": DATABASE_URL,
    "connect_args": connect_args
}