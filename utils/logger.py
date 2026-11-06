
import logging
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOG_DIR / "automation.log"

logger = logging.getLogger("automation")
logger.setLevel(logging.DEBUG)

# Prevent duplicate messages
logger.propagate = False

# Avoid adding handlers multiple times
if not logger.handlers:
    # Write logs to the file
    file_handler = logging.FileHandler(
        LOG_FILE, mode="a", encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)

    # Display logs in terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

logger.info("Logger initialized")
