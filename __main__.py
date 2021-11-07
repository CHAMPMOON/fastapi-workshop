import uvicorn

from .settings import settings

uvicorn.run(
    "fastapi-workshop.app:app",
    host=settings.SERVER_HOST,
    port=settings.SERVER_PORT,
    reload=True
)