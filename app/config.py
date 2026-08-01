import os
from dotenv import load_dotenv

load_dotenv()

# Поддержка PostgreSQL (Production) или SQLite (Development)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./college_is.db")

# Если используете SQLite, уберем префикс для SQLAlchemy engine creation в разных версиях
# Но для простоты оставим как есть, SQLAlchemy сам разберется
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}
else:
    connect_args = {}

DATABASE_CONFIG = {
    "url": DATABASE_URL,
    "connect_args": connect_args
}