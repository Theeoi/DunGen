#!/usr/bin/env python
"""
The helpers.py file of the DunGen package.

Contains helper classes and functions not directly linked to the idea of
DunGen.
"""
from __future__ import annotations
from enum import Enum
import random


class CardinalDirection(Enum):
    NORTH = 0
    EAST = 90
    SOUTH = 180
    WEST = 270

    def __str__(self):
        return self.name.title()

    def turn(self, angle) -> CardinalDirection:
        new_direction = (self.value + angle) % 360
        return CardinalDirection(new_direction)


def rolldice(max) -> int:
    "Returns an integer between 1 and {max}."
    return random.randint(1, max)
