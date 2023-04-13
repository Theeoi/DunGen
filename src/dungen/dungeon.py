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
        self.pathways: dict[list] = self.get_pathways()

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
        if rand in list(range(1, 3)):
            dimensions["shape"] = "square"
            dimensions["size"] = (20, 20)
        elif rand in list(range(3, 5)):
            dimensions["shape"] = "square"
            dimensions["size"] = (30, 30)
        elif rand in list(range(5, 7)):
            dimensions["shape"] = "square"
            dimensions["size"] = (40, 40)
        elif rand in list(range(7, 10)):
            dimensions["shape"] = "rectangle"
            dimensions["size"] = (20, 30)
        elif rand in list(range(10, 13)):
            dimensions["shape"] = "rectangle"
            dimensions["size"] = (30, 40)
        elif rand in list(range(13, 15)):
            dimensions["shape"] = "rectangle"
            dimensions["size"] = (40, 50)
        elif rand in list(range(15, 16)):
            dimensions["shape"] = "rectangle"
            dimensions["size"] = (50, 80)
        elif rand in list(range(16, 17)):
            dimensions["shape"] = "circle"
            dimensions["size"] = (30, 30)
        elif rand in list(range(17, 18)):
            dimensions["shape"] = "circle"
            dimensions["size"] = (50, 50)
        elif rand in list(range(18, 19)):
            dimensions["shape"] = "octagon"
            dimensions["size"] = (40, 40)
        elif rand in list(range(19, 20)):
            dimensions["shape"] = "octagon"
            dimensions["size"] = (60, 60)
        else:
            raise ValueError(f"Invalid diceroll: {rand}")

        return dimensions

    def get_pathways(self) -> dict[list]:
        """
        Method returning a dictionary mapping each cordinal direction to a list
        of pathways.
        """
        pathways = {
            "North": [],
            "East": [],
            "South": [],
            "West": []
        }
        # TODO: Append Door objects not strings

        # There is always an origin pathway entering a chamber.
        pathways[str(self.origin_direction.turn(180))].append("origin")

        # Generate a random number of pathways in each cordinal direction
        num_pathways = self.get_num_pathways()
        for _ in range(num_pathways):
            rand = helpers.rolldice(20)
            if rand in list(range(1, 8)):
                direction: str = str(self.origin_direction)
                pathways[direction].append("door")
            elif rand in list(range(8, 13)):
                direction: str = str(self.origin_direction.turn(-90))
                pathways[direction].append("door")
            elif rand in list(range(13, 18)):
                direction: str = str(self.origin_direction.turn(90))
                pathways[direction].append("door")
            elif rand in list(range(18, 21)):
                direction: str = str(self.origin_direction.turn(180))
                pathways[direction].append("door")
            else:
                raise ValueError(f"Invalid diceroll: {rand}")
        return pathways

    def get_num_pathways(self) -> int:
        """
        Method for obtaining the number of pathways in a chamber.
        Can be zero since the origin pathway is added elsewhere.
        """
        rand = helpers.rolldice(20)
        if rand in list(range(1, 6)):
            num_pathways = 0
        elif rand in list(range(6, 12)):
            num_pathways = 1
        elif rand in list(range(12, 16)):
            num_pathways = 2
        elif rand in list(range(16, 19)):
            num_pathways = 3
        elif rand in list(range(19, 21)):
            num_pathways = 4
        else:
            raise ValueError(f"Invalid diceroll: {rand}")
        return num_pathways
