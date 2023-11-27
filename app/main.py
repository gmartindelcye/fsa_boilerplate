import uvicorn
from fastapi import FastAPI

from app import settings
from app.core.models import HealthCheck
from app.router.api_v1.endpoints import api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
    debug=settings.DEBUG
)


@app.get("/", response_model=HealthCheck, tags=["status"])
async def health_check():
    return {
        "name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "description": settings.DESCRIPTION
    }

app.include_router(api_router, prefix=settings.API_V1_PREFIX)

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, host="0.0.0.0", reload=True)
