from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[1]


def load_project_env() -> None:
    """Load environment variables from the repository root .env file."""
    load_dotenv(ROOT_DIR.parent / ".env")


def get_project_root() -> Path:
    return ROOT_DIR.parent


def get_data_dir() -> Path:
    return get_project_root() / "data" / "raw"


def get_env(name: str, default: str | None = None) -> str | None:
    return os.getenv(name, default)
