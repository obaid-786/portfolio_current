"""
REST API routes.

Currently exposes the contact-form endpoint. Returns JSON so the frontend
can show inline success/error feedback without a full page reload.
"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, Field

from ..email_service import EmailError, send_contact_email
from ..logger import logger

router = APIRouter(prefix="/api", tags=["api"])


class ContactPayload(BaseModel):
    """Validated contact-form submission payload."""

    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    subject: str = Field(..., min_length=1, max_length=150)
    message: str = Field(..., min_length=1, max_length=5000)


@router.post("/contact")
async def contact(payload: ContactPayload):
    """Handle a contact-form submission and email it to the site owner."""
    try:
        send_contact_email(
            name=payload.name,
            email=payload.email,
            subject=payload.subject,
            message=payload.message,
        )
        return JSONResponse(
            status_code=200,
            content={"success": True, "message": "Thanks! Your message has been sent."},
        )
    except EmailError as exc:
        # Known, user-safe failure (e.g. SMTP misconfiguration).
        logger.warning("Contact form email error: %s", exc)
        return JSONResponse(
            status_code=502,
            content={"success": False, "message": str(exc)},
        )
    except Exception as exc:  # noqa: BLE001 - last-resort guard
        logger.exception("Unexpected error in contact endpoint: %s", exc)
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "Something went wrong. Please try later."},
        )


@router.get("/health")
async def health():
    """Lightweight health check for Render uptime monitoring."""
    return {"status": "ok"}
