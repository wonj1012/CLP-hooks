from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.routers import account_router, clp_router, redis_router, swap_router
from common.config import settings

app = FastAPI()


api_router_config = {"prefix": "/api"}
ws_router_config = {"prefix": "/ws"}

app.include_router(account_router, **api_router_config)  # type: ignore
app.include_router(swap_router, **api_router_config)  # type: ignore
app.include_router(redis_router, **api_router_config)  # type: ignore
app.include_router(clp_router, **api_router_config)  # type: ignore


@app.get("/")
async def read_root(request: Request) -> JSONResponse:
    """
    Root endpoint for the API.
    """
    base_url = str(request.base_url)

    return JSONResponse(
        status_code=200,
        content={
            "name": settings.PROJECT_NAME,
            "version": settings.API_VERSION,
            "description": "API for XRPL-Swap",
            "contact": {
                "email": "jjaa1012@gmail.com",
                "github": "https://github.com/Helix-Organization/xrpl-swap",
            },
            "docs": f"{base_url}docs",
            "redoc": f"{base_url}redoc",
        },
    )