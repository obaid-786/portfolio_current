"""
HTML page routes (server-side rendered via Jinja2).
"""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from .. import data
from ..config import get_settings

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the single-page portfolio."""
    settings = get_settings()
    context = {
        "request": request,
        "site_url": settings.site_url,
        "hero": data.HERO,
        "about": data.ABOUT,
        "skills": data.SKILLS,
        "experience": data.EXPERIENCE,
        "education": data.EDUCATION,
        "projects": data.PROJECTS,
        "project_categories": data.PROJECT_CATEGORIES,
        "certifications": data.CERTIFICATIONS,
        "achievements": data.ACHIEVEMENTS,
        "contact": data.CONTACT,
    }
    return templates.TemplateResponse("index.html", context)
