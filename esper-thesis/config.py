"""
Configuration and database location resolution for ESPER-THESIS.

Implements four-level priority cascade:
1. Explicit CLI argument (--database)
2. Environment variable (ESPER_THESIS_DB)
3. Config file (~/.esper_thesis/config.json)
4. Default (./research_db.json)
"""

import json
import os
from pathlib import Path
from typing import Optional

__version__ = "1.0.0"

DEFAULT_DATABASE = "research_db.json"
CONFIG_DIR = Path.home() / ".esper_thesis"
CONFIG_FILE = CONFIG_DIR / "config.json"
ENV_VAR = "ESPER_THESIS_DB"


def get_database_path(
    cli_path: Optional[str] = None,
    project: Optional[str] = None
) -> Path:
    """
    Resolve database path using priority cascade.
    
    Priority order:
    1. Explicit CLI argument (highest)
    2. Environment variable
    3. Config file (default or project-specific)
    4. Default: ./research_db.json
    
    Args:
        cli_path: Path from --database CLI argument
        project: Project name from --project CLI argument
    
    Returns:
        Resolved Path object
    
    Examples:
        # Explicit path
        >>> get_database_path(cli_path="~/research/main.json")
        PosixPath('/home/user/research/main.json')
        
        # Environment variable
        >>> os.environ['ESPER_THESIS_DB'] = '~/global.json'
        >>> get_database_path()
        PosixPath('/home/user/global.json')
        
        # Config file project
        >>> get_database_path(project='literacy')
        PosixPath('/home/user/projects/literacy/research.json')
        
        # Default
        >>> get_database_path()
        PosixPath('research_db.json')
    """
    
    # 1. Explicit CLI argument (highest priority)
    if cli_path:
        return Path(cli_path).expanduser().resolve()
    
    # 2. Environment variable
    if env_path := os.getenv(ENV_VAR):
        return Path(env_path).expanduser().resolve()
    
    # 3. Config file
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
            
            # 3a. Project-specific database
            if project and 'projects' in config:
                if project in config['projects']:
                    project_path = config['projects'][project]
                    return Path(project_path).expanduser().resolve()
                else:
                    # Project specified but not found - list available
                    available = ', '.join(config['projects'].keys())
                    raise ValueError(
                        f"Project '{project}' not found in config. "
                        f"Available projects: {available}"
                    )
            
            # 3b. Default database from config
            if 'default_database' in config:
                default_path = config['default_database']
                return Path(default_path).expanduser().resolve()
        
        except json.JSONDecodeError:
            # Config file exists but invalid - warn and fall through
            import warnings
            warnings.warn(
                f"Config file {CONFIG_FILE} is invalid JSON. Using default database."
            )
    
    # 4. Default: local file
    return Path(DEFAULT_DATABASE)


def create_config_template():
    """
    Create template config file if it doesn't exist.
    
    Creates ~/.esper_thesis/config.json with example structure.
    """
    
    if CONFIG_FILE.exists():
        print(f"Config file already exists: {CONFIG_FILE}")
        return
    
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    
    template = {
        "default_database": None,  # null = use local ./research_db.json
        "projects": {
            "example": "~/research/example-project.json"
        }
    }
    
    with open(CONFIG_FILE, 'w') as f:
        json.dump(template, f, indent=2)
    
    print(f"Created config template: {CONFIG_FILE}")
    print("\nEdit this file to configure:")
    print("  - default_database: Global research database path")
    print("  - projects: Named project-specific databases")


def show_config():
    """Display current configuration and resolution behavior."""
    
    print("=" * 60)
    print("ESPER-THESIS Configuration")
    print("=" * 60)
    print()
    
    # Show resolution order
    print("Database Resolution Order:")
    print("  1. CLI argument:    --database <path>")
    print(f"  2. Environment var: {ENV_VAR}")
    print(f"  3. Config file:     {CONFIG_FILE}")
    print(f"  4. Default:         {DEFAULT_DATABASE}")
    print()
    
    # Show current environment
    print("Current Environment:")
    env_value = os.getenv(ENV_VAR)
    print(f"  {ENV_VAR} = {env_value if env_value else '(not set)'}")
    print()
    
    # Show config file
    print("Config File:")
    if CONFIG_FILE.exists():
        print(f"  Location: {CONFIG_FILE}")
        print(f"  Status:   Exists")
        
        try:
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
            
            print(f"  Default:  {config.get('default_database', '(not set)')}")
            
            if projects := config.get('projects', {}):
                print(f"  Projects: {len(projects)} configured")
                for name, path in projects.items():
                    print(f"    - {name}: {path}")
            else:
                print("  Projects: None configured")
        
        except json.JSONDecodeError:
            print("  Status:   INVALID JSON")
    else:
        print(f"  Location: {CONFIG_FILE}")
        print("  Status:   Not found")
        print("\n  Run 'esper-thesis config init' to create template")
    print()
    
    # Show what would be used
    print("Current Resolution:")
    path = get_database_path()
    print(f"  Database: {path}")
    print(f"  Absolute: {path.resolve()}")
    print(f"  Exists:   {path.exists()}")
    print()
    
    print("=" * 60)


def get_version() -> str:
    """Return ESPER-THESIS version string."""
    return __version__
