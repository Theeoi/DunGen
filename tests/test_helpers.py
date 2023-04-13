#!/usr/bin/env python

from dungen.helpers import CardinalDirection, rolldice


def test_direction_str():
    assert str(CardinalDirection.NORTH) == "North"
    assert str(CardinalDirection.EAST) == "East"
    assert str(CardinalDirection.SOUTH) == "South"
    assert str(CardinalDirection.WEST) == "West"


def test_direction_turn_clockwise():
    assert CardinalDirection.NORTH.turn(90) == CardinalDirection.EAST
    assert CardinalDirection.EAST.turn(90) == CardinalDirection.SOUTH
    assert CardinalDirection.SOUTH.turn(90) == CardinalDirection.WEST
    assert CardinalDirection.WEST.turn(90) == CardinalDirection.NORTH


def test_direction_turn_counterclockwise():
    assert CardinalDirection.NORTH.turn(-90) == CardinalDirection.WEST
    assert CardinalDirection.EAST.turn(-90) == CardinalDirection.NORTH
    assert CardinalDirection.SOUTH.turn(-90) == CardinalDirection.EAST
    assert CardinalDirection.WEST.turn(-90) == CardinalDirection.SOUTH


def test_rolldice():
    for max_value in [4, 6, 8, 10, 12, 20]:
        for _ in range(1000):
            result = rolldice(max_value)
            assert isinstance(result, int)
            assert result >= 1 and result <= max_value
