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
    start: bool = False
    shape: str
    size: tuple[int]
    door: Door
    passage: Passage
