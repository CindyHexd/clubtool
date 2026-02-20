from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    message: str
    log_level: str = "INFO"


def load_settings() -> Settings:
    # Loads variables from a local .env into os.environ if present.
    # In other contexts (CI, Docker), environment variables may be provided directly.
    load_dotenv()

    message = os.getenv("CLUBTOOL_MESSAGE")
    if not message:
        raise RuntimeError(
            "Missing required environment variable CLUBTOOL_MESSAGE. "
            "Create a .env file from .env.example or set it in the environment."
        )

    log_level = os.getenv("CLUBTOOL_LOG_LEVEL", "INFO")
    return Settings(message=message, log_level=log_level)
