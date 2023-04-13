#!/usr/bin/env python
"""
The __init__.py for the DunGen package
"""
from importlib import resources
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


# Version of the DunGen package
__version__ = "0.0.1"

# Load configuration variables
_cfg = tomllib.loads(resources.read_text("dungen", "config.toml"))

NUM_ROOMS: int = _cfg["generation"]["rooms"]
MULTILEVEL: bool = _cfg["generation"]["multilevel"]
