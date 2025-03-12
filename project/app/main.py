from fastapi import FastAPI
from app.api.v1.endpoints import auth, roles, users
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

# Подключаем маршруты
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(roles.router, prefix="/api/v1/roles", tags=["roles"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])