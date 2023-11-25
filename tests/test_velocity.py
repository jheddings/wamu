"""Unit tests for velocity units."""

from conftest import isclose

import wamu


def test_one_mps():
    """Confirm simple MetersPerSecond conversions."""
    mps = wamu.MetersPerSecond(1)

    assert mps == 1.0

    assert float(mps) == 1.0
    assert int(mps) == 1

    assert mps.kilometers_per_hr == 3.6

    assert isclose(mps.miles_per_hr, 2.23694)
    assert isclose(mps.feet_per_sec, 3.28084)
    assert isclose(mps.knots, 1.94384449)

    assert str(mps) == "1 m/s"
    assert repr(mps) == "MetersPerSecond(1)"


def test_one_kph():
    """Confirm simple KilometersPerHour conversions."""
    kph = wamu.KilometersPerHour(1)

    assert kph == 1.0

    assert float(kph) == 1.0
    assert int(kph) == 1

    assert isclose(kph.meters_per_sec, 0.27777778)
    assert isclose(kph.miles_per_hr, 0.62137119)
    assert isclose(kph.feet_per_sec, 0.91134442)
    assert isclose(kph.knots, 0.5399568)

    assert str(kph) == "1 km/h"
    assert repr(kph) == "KilometersPerHour(1)"


def test_one_mph():
    """Confirm simple MilesPerHour conversions."""
    mph = wamu.MilesPerHour(1)

    assert mph == 1.0

    assert float(mph) == 1.0
    assert int(mph) == 1

    assert isclose(mph.feet_per_sec, 1.466667)
    assert isclose(mph.meters_per_sec, 0.44704)
    assert isclose(mph.kilometers_per_hr, 1.609344)
    assert isclose(mph.knots, 0.8689762419)

    assert str(mph) == "1 mph"
    assert repr(mph) == "MilesPerHour(1)"


def test_one_fps():
    """Confirm simple FeetPerSecond conversions."""
    fps = wamu.FeetPerSecond(1)

    assert fps == 1.0

    assert float(fps) == 1.0
    assert int(fps) == 1

    assert isclose(fps.meters_per_sec, 0.3048)
    assert isclose(fps.kilometers_per_hr, 1.09728)
    assert isclose(fps.miles_per_hr, 0.68181818)
    assert isclose(fps.knots, 0.5924838)

    assert str(fps) == "1 fps"
    assert repr(fps) == "FeetPerSecond(1)"
