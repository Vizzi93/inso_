from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Startup / Shutdown-Logik."""
    # Startup
    print(f"[startup] PrivatInsolvenz-Manager — Umgebung: {settings.environment}")
    yield
    # Shutdown
    print("[shutdown] Server wird beendet")


app = FastAPI(
    title="PrivatInsolvenz-Manager API",
    description="Digitale Begleitung des Verbraucherinsolvenzverfahrens (§§ 304 ff. InsO)",
    version="0.1.0",
    docs_url="/docs" if not settings.is_production else None,  # Swagger in Prod deaktiviert
    redoc_url="/redoc" if not settings.is_production else None,
    lifespan=lifespan,
)

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(o) for o in settings.allowed_origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Router einbinden ---
# from app.api.v1 import router as api_v1_router
# app.include_router(api_v1_router, prefix="/api/v1")


# --- Health Check ---
@app.get("/api/health", tags=["System"])
async def health_check() -> dict[str, str]:
    """
    Wird vom CI/CD-Deployment und Monitoring geprüft.
    Gibt 200 zurück wenn der Server läuft.
    """
    return {"status": "ok", "environment": settings.environment}
