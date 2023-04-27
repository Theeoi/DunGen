#!/usr/bin/env python

import dungen.helpers as helpers
from dungen.dungeon import Chamber


def test_chamber_init():
    chamber = Chamber(helpers.CardinalDirection.NORTH)
    assert chamber.origin_direction == helpers.CardinalDirection.NORTH


def test_chamber_dimensions():
    chamber = Chamber(helpers.CardinalDirection.NORTH)
    dimensions = chamber.get_dimensions()
    assert dimensions["shape"] in ["square", "rectangle", "circle", "octagon"]
    assert isinstance(dimensions["size"], tuple)
    assert len(dimensions["size"]) == 2
    assert all(isinstance(i, int) for i in dimensions["size"])


def test_chamber_pathways():
    chamber = Chamber(helpers.CardinalDirection.NORTH)
    exits = chamber.get_exits()
    assert set(exits.keys()) == set(["North", "East", "South", "West"])
    for exit in exits.values():
        assert isinstance(exit, list)


def test_chamber_num_pathways():
    chamber = Chamber(helpers.CardinalDirection.NORTH)
    num_exits = chamber.get_num_exits()
    assert isinstance(num_exits, int)
    assert 0 <= num_exits <= 4
