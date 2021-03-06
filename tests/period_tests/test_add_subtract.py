# -*- coding: utf-8 -*-

import pendulum


def test_dst_add():
    start = pendulum.create(2017, 3, 7, tz='America/Toronto')
    end = start.add(days=6)
    period = end - start
    new_end = start + period

    assert new_end == end


def test_dst_add_non_variable_units():
    start = pendulum.create(2013, 3, 31, 1, 30, tz='Europe/Paris')
    end = start.add(hours=1)
    period = end - start
    new_end = start + period

    assert new_end == end


def test_dst_subtract():
    start = pendulum.create(2017, 3, 7, tz='America/Toronto')
    end = start.add(days=6)
    period = end - start
    new_start = end - period

    assert new_start == start
