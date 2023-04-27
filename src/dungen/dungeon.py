#!/usr/bin/env python
"""
The dungeon.py file for the DunGen package.

Defines dungeon structures such as chambers, passages and doors.
"""

import dungen.helpers as helpers


class Passage:
    "Class of a dungeon passage"


class Door:
    "Class of a dungeon door"


class Chamber:
    """
    Class of a dungeon chamber.

    Takes an origin CardinalDirection and generates a chamber with a dimension
    and pathways to other chambers or passages.
    """

    def __init__(self, origin_direction: helpers.CardinalDirection):
        self.origin_direction = origin_direction
        self.dimensions: dict = self.get_dimensions()
        self.exits: dict[list] = self.get_exits()

    def __repr__(self):
        return f"Chamber({self.origin_direction})"

    def __str__(self):
        return ("Chamber:\n"
                f"\t{self.origin_direction=}\n"
                f"\t{self.dimensions=}\n"
                f"\t{self.exits=}\n"
                )

    def get_dimensions(self) -> dict:
        """
        Method returning the shape and size of a chamber.
        The size return format depends on the shape.
        """
        dimensions = {
            "shape": None,
            "size": None
        }
        rand: int = helpers.rolldice(19)
        if rand in helpers.rangeroll(1, 2):
            dimensions["shape"] = "square"
            dimensions["size"] = (20, 20)
        elif rand in helpers.rangeroll(3, 4):
            dimensions["shape"] = "square"
            dimensions["size"] = (30, 30)
        elif rand in helpers.rangeroll(5, 6):
            dimensions["shape"] = "square"
            dimensions["size"] = (40, 40)
        elif rand in helpers.rangeroll(7, 9):
            dimensions["shape"] = "rectangle"
            dimensions["size"] = (20, 30)
        elif rand in helpers.rangeroll(10, 12):
            dimensions["shape"] = "rectangle"
            dimensions["size"] = (30, 40)
        elif rand in helpers.rangeroll(13, 14):
            dimensions["shape"] = "rectangle"
            dimensions["size"] = (40, 50)
        elif rand in helpers.rangeroll(15, 15):
            dimensions["shape"] = "rectangle"
            dimensions["size"] = (50, 80)
        elif rand in helpers.rangeroll(16, 16):
            dimensions["shape"] = "circle"
            dimensions["size"] = (30, 30)
        elif rand in helpers.rangeroll(17, 17):
            dimensions["shape"] = "circle"
            dimensions["size"] = (50, 50)
        elif rand in helpers.rangeroll(18, 18):
            dimensions["shape"] = "octagon"
            dimensions["size"] = (40, 40)
        elif rand in helpers.rangeroll(19, 19):
            dimensions["shape"] = "octagon"
            dimensions["size"] = (60, 60)
        else:
            raise ValueError(f"Invalid diceroll: {rand}")

        return dimensions

    def get_exits(self) -> dict[list]:
        """
        Method returning a dictionary mapping each cordinal direction to a list
        of exits.
        """
        exits = {
            "North": [],
            "East": [],
            "South": [],
            "West": []
        }

        # There is always an origin pathway entering a chamber.
        exits[str(self.origin_direction.turn(180))].append("origin")

        # Generate a random number of pathways in each cordinal direction
        num_exits = self.get_num_exits()
        for _ in range(num_exits):
            rand = helpers.rolldice(20)
            if rand in helpers.rangeroll(1, 7):
                direction = self.origin_direction
                exits[str(direction)].append(self.get_exit_type(direction))
            elif rand in helpers.rangeroll(8, 12):
                direction = self.origin_direction.turn(-90)
                exits[str(direction)].append(self.get_exit_type(direction))
            elif rand in helpers.rangeroll(13, 17):
                direction = self.origin_direction.turn(90)
                exits[str(direction)].append(self.get_exit_type(direction))
            elif rand in helpers.rangeroll(18, 20):
                direction = self.origin_direction.turn(180)
                exits[str(direction)].append(self.get_exit_type(direction))
            else:
                raise ValueError(f"Invalid diceroll: {rand}")
        return exits

    def get_num_exits(self) -> int:
        """
        Method for obtaining the number of exits in a chamber.
        Can be zero since the origin pathway is added elsewhere.
        """
        rand = helpers.rolldice(20)
        if rand in helpers.rangeroll(1, 5):
            num_exits = 0
        elif rand in helpers.rangeroll(6, 11):
            num_exits = 1
        elif rand in helpers.rangeroll(12, 15):
            num_exits = 2
        elif rand in helpers.rangeroll(16, 18):
            num_exits = 3
        elif rand in helpers.rangeroll(19, 20):
            num_exits = 4
        else:
            raise ValueError(f"Invalid diceroll: {rand}")
        return num_exits

    def get_exit_type(self, direction) -> Passage | Door:
        """
        Method returning the type of exit leading from a Chamber.
        Can either be a Passage or a Door object.
        """
        rand = helpers.rolldice(20)
        if rand in helpers.rangeroll(1, 10):
            return Door(direction)
        elif rand in helpers.rangeroll(11, 20):
            return Passage()
        else:
            raise ValueError(f"Invalid diceroll: {rand}")
