import uvicorn

from .settings import settings

uvicorn.run(
    "workshop.app:app",
    host=settings.SERVER_HOST,
    port=settings.SERVER_PORT,
    reload=True
)