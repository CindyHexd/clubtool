from __future__ import annotations

from clubtool.config import load_settings


def main() -> int:
    settings = load_settings()
    print(settings.message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
