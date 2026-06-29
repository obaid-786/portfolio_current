"""
Application configuration.

Loads settings from environment variables using pydantic-settings.
Provides a single cached `get_settings()` accessor used across the app.
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Central application settings loaded from environment / .env file."""

    # --- General ---
    app_name: str = "Obaidullah Siddiqui — Portfolio"
    environment: str = "production"
    debug: bool = False

    # Base URL used for canonical links / Open Graph tags.
    site_url: str = "https://your-app.onrender.com"

    # --- SMTP / Email configuration (contact form) ---
    # Configure these in Render's environment variables dashboard.
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_user: str = ""           # e.g. your gmail address
    smtp_password: str = ""       # app password (NOT your normal password)
    smtp_from: str = ""           # "From" address (defaults to smtp_user)
    contact_recipient: str = "obaidsid0@gmail.com"  # where messages are delivered

    # Toggle to disable actual sending (useful in local/dev).
    email_enabled: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance."""
    return Settings()
