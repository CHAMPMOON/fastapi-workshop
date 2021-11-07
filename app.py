from fastapi import FastAPI

from .api import router 


tags_metadata = [
    {
        "name": "auth",
        "description": "authorization and registration"
    },
    {
        "name": "operations",
        "description": "work with operations"
    },
    {
        "name": "reports",
        "description": "import and export of reports"
    },
]

app = FastAPI(
    title="workshop",
    description="service for recording personal income and outcome",
    version="1.0.0",
    openapi_tags=tags_metadata
)
app.include_router(router)