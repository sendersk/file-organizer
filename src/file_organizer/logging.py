import logging
import json
from pathlib import Path
from datetime import datetime, UTC


class JsonFormatter(logging.Formatter):
    """Formats logs as JSON lines for structured logging."""

    def format(self, record: logging.LogRecord) -> str:
        log_record = {
            "timestamp": datetime.now(UTC).isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.name,
        }

        return json.dumps(log_record, ensure_ascii=False)


def setup_logging(log_file: Path | None = None) -> logging.Logger:
    """
    Configure application logging.

    - Console output (human readable)
    - Optional JSON file logging
    """

    logger = logging.getLogger("file_organizer")
    logger.setLevel(logging.INFO)

    # Avoid duplicate logs
    logger.handlers.clear()

    # Console handler
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter("[%(levelname)s] %(message)s")
    console_handler.setFormatter(console_formatter)

    logger.addHandler(console_handler)

    # File handler (JSON logs)
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)

        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setFormatter(JsonFormatter())

        logger.addHandler(file_handler)

    return logger