from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmarker

from .settings import settings


engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False}
)

Session = sessionmarker(
    engine,
    autocommit=False,
    autoflush=False
)


