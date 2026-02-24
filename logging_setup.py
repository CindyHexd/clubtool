from __future__ import annotations

import logging
import os


def configure_logging(default_level: str = "INFO") -> None:
    level_name = os.getenv("CLUBTOOL_LOG_LEVEL", default_level).upper()
    level = getattr(logging, level_name, logging.INFO)

    logging.basicConfig(
        level=level,
        format="%(levelname)s %(name)s: %(message)s",
    )
    