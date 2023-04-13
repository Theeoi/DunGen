#!/usr/bin/env python

import dungen


def test_version():
    assert isinstance(dungen.__version__, str)


def test_num_rooms():
    assert isinstance(dungen.NUM_ROOMS, int)
    assert dungen.NUM_ROOMS > 0


def test_multilevel():
    assert isinstance(dungen.MULTILEVEL, bool)
