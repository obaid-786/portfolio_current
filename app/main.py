"""
FastAPI application entry point.

Wires together routing, static files, templates, logging, error handling,
and security middleware. Designed to run under Uvicorn on Render.
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.gzip import GZipMiddleware

from .config import get_settings
from .logger import configure_logging, logger
from .routes import api, pages

# Load settings and configure logging before anything else.
settings = get_settings()
configure_logging(debug=settings.debug)

# Create the FastAPI instance. Docs are disabled in production for a clean site.
app = FastAPI(
    title=settings.app_name,
    docs_url="/docs" if settings.debug else None,
    redoc_url=None,
)

# GZip responses for faster loading of HTML/CSS/JS.
app.add_middleware(GZipMiddleware, minimum_size=500)

# Serve static assets (CSS, JS, images, resume, favicon).
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates instance used by the custom 404 handler.
templates = Jinja2Templates(directory="templates")

# Register routers.
app.include_router(pages.router)
app.include_router(api.router)


@app.on_event("startup")
async def on_startup() -> None:
    """Log a startup banner so deployments are easy to trace in Render logs."""
    logger.info("Starting %s (env=%s)", settings.app_name, settings.environment)


@app.exception_handler(404)
async def not_found_handler(request: Request, exc) -> HTMLResponse:
    """Render a friendly custom 404 page for missing routes."""
    return templates.TemplateResponse(
        "404.html",
        {"request": request, "site_url": settings.site_url},
        status_code=404,
    )


@app.exception_handler(500)
async def server_error_handler(request: Request, exc) -> HTMLResponse:
    """Catch unhandled errors and return the 404 template with a 500 status.

    We log the full traceback but never expose internals to the client.
    """
    logger.exception("Unhandled server error: %s", exc)
    return templates.TemplateResponse(
        "404.html",
        {"request": request, "site_url": settings.site_url, "is_error": True},
        status_code=500,
    )
