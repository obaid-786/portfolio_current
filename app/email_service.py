"""
Email service for the contact form.

Uses Python's built-in smtplib so there are no heavy external dependencies.
Designed to fail gracefully: if SMTP is misconfigured or sending fails,
the error is logged and surfaced to the caller without crashing the app.
"""

import smtplib
import ssl
from email.message import EmailMessage

from .config import get_settings
from .logger import logger


class EmailError(Exception):
    """Raised when an email fails to send."""


def send_contact_email(name: str, email: str, subject: str, message: str) -> None:
    """Send a contact-form submission to the configured recipient.

    Args:
        name: Sender's name.
        email: Sender's reply-to email address.
        subject: Message subject.
        message: Message body.

    Raises:
        EmailError: If sending fails or email is misconfigured.
    """
    settings = get_settings()

    # In dev you can disable sending entirely.
    if not settings.email_enabled:
        logger.info("Email disabled — skipping send. From=%s Subject=%s", email, subject)
        return

    if not (settings.smtp_user and settings.smtp_password):
        raise EmailError("SMTP credentials are not configured.")

    from_addr = settings.smtp_from or settings.smtp_user

    # Build a well-formed email message.
    msg = EmailMessage()
    msg["Subject"] = f"[Portfolio Contact] {subject}"
    msg["From"] = from_addr
    msg["To"] = settings.contact_recipient
    msg["Reply-To"] = email
    msg.set_content(
        f"You received a new message from your portfolio contact form.\n\n"
        f"Name:    {name}\n"
        f"Email:   {email}\n"
        f"Subject: {subject}\n\n"
        f"Message:\n{message}\n"
    )

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=20) as server:
            server.starttls(context=context)
            server.login(settings.smtp_user, settings.smtp_password)
            server.send_message(msg)
        logger.info("Contact email sent successfully from %s", email)
    except Exception as exc:  # noqa: BLE001 - surface a clean error to caller
        logger.error("Failed to send contact email: %s", exc)
        raise EmailError("Could not send email. Please try again later.") from exc
