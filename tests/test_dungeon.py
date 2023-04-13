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
    pathways = chamber.get_pathways()
    assert set(pathways.keys()) == set(["North", "East", "South", "West"])
    for path in pathways.values():
        assert isinstance(path, list)


def test_chamber_num_pathways():
    chamber = Chamber(helpers.CardinalDirection.NORTH)
    num_pathways = chamber.get_num_pathways()
    assert isinstance(num_pathways, int)
    assert 0 <= num_pathways <= 4
