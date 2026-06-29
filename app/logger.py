"""
Centralized logging configuration.

Produces structured, timestamped logs that work cleanly with Render's
log streaming (stdout). Import `logger` anywhere you need to log.
"""

import logging
import sys

# Create a named logger for the application.
logger = logging.getLogger("portfolio")


def configure_logging(debug: bool = False) -> None:
    """Configure root logging handlers and format.

    Args:
        debug: When True, sets log level to DEBUG, otherwise INFO.
    """
    level = logging.DEBUG if debug else logging.INFO

    # Stream handler writes to stdout so Render captures it.
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)

    # Avoid duplicate handlers on reload.
    logger.handlers.clear()
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.propagate = False
