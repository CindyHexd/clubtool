from __future__ import annotations

import logging

from clubtool.config import load_settings
from clubtool.logging_setup import configure_logging

log = logging.getLogger(__name__)


def main() -> int:
    configure_logging()
    settings = load_settings()

    log.info("Starting clubtool")
    print(settings.message)
    log.info("Completed successfully")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
