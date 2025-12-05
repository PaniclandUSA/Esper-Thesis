# esper_thesis/config.py

import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

__all__ = ["__version__", "get_config_dir", "load_config", "get_database_path"]

__version__ = "1.0.0"  # keep your version here

CONFIG_DIR_NAME = ".esper_thesis"
CONFIG_FILE_NAME = "config.json"
ENV_DB_VAR = "ESPER_THESIS_DB"
DEFAULT_DB_NAME = "research_db.json"


def get_config_dir() -> Path:
    """Return the user-level config directory (~/.esper_thesis)."""
    return Path.home() / CONFIG_DIR_NAME


def load_config() -> Dict[str, Any]:
    """Load config JSON from ~/.esper_thesis/config.json if present."""
    config_path = get_config_dir() / CONFIG_FILE_NAME
    if not config_path.exists():
        return {}
    try:
        return json.loads(config_path.read_text(encoding="utf-8"))
    except Exception:
        # Fail closed: if config is malformed, ignore it
        return {}


def get_database_path(args) -> Path:
    """
    Resolve database path with priority cascade:

    1. CLI argument: --database /path/to/db.json
    2. Environment variable: ESPER_THESIS_DB
    3. Config file (~/.esper_thesis/config.json):
       - project mapping via --project
       - default_database
    4. Default: ./research_db.json (current directory)
    """
    # 1. CLI argument
    if getattr(args, "database", None):
        return Path(args.database).expanduser()

    # 2. Environment variable
    env_db = os.getenv(ENV_DB_VAR)
    if env_db:
        return Path(env_db).expanduser()

    # 3. Config file
    config = load_config()
    project = getattr(args, "project", None)

    # Project mapping
    if project and "projects" in config:
        project_map = config.get("projects", {})
        if project in project_map:
            return Path(project_map[project]).expanduser()

    # Default database in config
    default_db = config.get("default_database")
    if default_db:
        return Path(default_db).expanduser()

    # 4. Default: local JSON in current directory
    return Path(DEFAULT_DB_NAME)
