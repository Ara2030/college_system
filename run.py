import uvicorn

if __name__ == "__main__":
    # Запуск сервера разработки
    # host="0.0.0.0" - доступно из сети
    # port=8000 - стандартный порт
    # reload=True - автоматическая перезагрузка при изменении кода
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)