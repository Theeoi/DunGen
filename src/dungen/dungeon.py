#!/usr/bin/env python
"""
The dungeon.py file for the DunGen package.

Defines dungeon structures such as chambers, passages and doors.
"""

from dataclasses import dataclass


@dataclass
class Passage:
    "Class of a dungeon passage"


@dataclass
class Door:
    "Class of a dungeon door"


@dataclass
class Chamber:
    "Class of a dungeon chamber"
    start: bool = False  # determines which table to roll from
    dimensions: dict  # describes the shape and size of the chamber
    pathways: dict  # mapping cardinal direction to doors and passages if any.
