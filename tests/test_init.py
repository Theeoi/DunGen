#!/usr/bin/env python

import dungen


def test_version():
    assert isinstance(dungen.__version__, str)


def test_max_chambers():
    assert isinstance(dungen.MAX_CHAMBERS, int)
    assert dungen.MAX_CHAMBERS > 0


def test_multilevel():
    assert isinstance(dungen.MULTILEVEL, bool)
