"""Starter tests for the weather module.

These tests deliberately cover only ordinary examples. They show how pytest works,
but they are not a sufficient test suite for the specification in SPECIFICATION.md.
"""

from weather import (
    average_temperature,
    filter_by_temperature,
    hottest_measurement,
    parse_measurement,
    parse_time,
)
import pytest


def test_parse_time_regular_time():
    assert parse_time("14:21") == 861
    assert parse_time("00:00") == 0
    assert parse_time ("012:00") == 720
    assert parse_time ("01:1") == 61

    with pytest.raises(ValueError):
        assert parse_time("00:00:00") 
        assert parse_time("00.00")
        assert parse_time("24:00")
        assert parse_time("2,1:00")


def test_parse_measurement_regular_line():
    assert parse_measurement("Köln;14:21;21.7") == ("Köln", 861, 21.7)
    assert parse_measurement("Köln;14:21;-21.7") == ("Köln", 861, -21.7)

    with pytest.raises(ValueError):
        assert parse_measurement("Köln;14:21;21.7;4")
        assert parse_measurement("Köln;14:21")
        assert parse_measurement("Köln,14:21,21.7")
        assert parse_measurement("Köln;-14:21;-21.7")
        assert parse_measurement("Köln;21.7;14:21")
        

def test_filter_by_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
    ]

    assert filter_by_temperature(measurements, 15.0, 20.0) == [
        ("Düsseldorf", 720, 18.5)
    ]
    assert len(filter_by_temperature(measurements, 0.0, 100.0)) == len(measurements)

    # with pytest.raises(ValueError):
    #   assert(measurements, 20.0, 15,0)

def test_average_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Köln", 720, 20.0),
        ("köln", 720, 30.0),
    ]

    assert average_temperature(measurements, "Köln") == 15.0
    assert average_temperature(measurements, "Köln") != average_temperature(measurements, "köln") 


def test_hottest_measurement_with_unique_maximum():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 25.0),
        ("Bonn", 900, 20.0),
    ]

    assert hottest_measurement(measurements) == ("Düsseldorf", 720, 25.0)
