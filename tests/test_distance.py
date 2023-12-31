"""Unit tests for distance units."""

from conftest import isclose

from wamu.distance import (
    Foot,
    Inch,
    Kilometer,
    LightYear,
    Meter,
    Mile,
    Millimeter,
    NauticalMile,
    Parsec,
    Yard,
)


def test_one_meter():
    """Confirm simple Meter conversions."""
    meter = Meter(1)

    assert meter == 1.0

    assert float(meter) == 1.0
    assert int(meter) == 1

    assert meter.kilometers == 0.001
    assert meter.centimeters == 100.0
    assert meter.millimeters == 1000.0

    assert isclose(meter.feet, 3.28084)
    assert isclose(meter.yards, 1.09361)
    assert isclose(meter.inches, 39.3701)

    assert str(meter) == "1 m"
    assert repr(meter) == "Meter(1)"


def test_one_kilometer():
    """Confirm simple Kilometer conversions."""
    kilo = Kilometer(1)

    assert kilo == 1.0

    assert float(kilo) == 1.0
    assert int(kilo) == 1

    assert kilo.meters == 1000.0

    assert isclose(kilo.miles, 0.62137119)
    assert isclose(kilo.feet, 3280.8399)

    assert str(kilo) == "1 km"
    assert repr(kilo) == "Kilometer(1)"


def test_one_millimeter():
    """Confirm simple Millimeter conversions."""
    mm = Millimeter(1)

    assert mm == 1.0

    assert float(mm) == 1.0
    assert int(mm) == 1

    assert mm.meters == 0.001
    assert mm.centimeters == 0.1
    assert mm.kilometers == 1e-6

    assert isclose(mm.inches, 0.03937)
    assert isclose(mm.feet, 0.00328084)

    assert str(mm) == "1 mm"
    assert repr(mm) == "Millimeter(1)"


def test_one_mile():
    """Confirm simple Mile conversions."""
    mile = Mile(1)

    assert mile == 1.0

    assert float(mile) == 1.0
    assert int(mile) == 1

    assert mile.feet == 5280.0
    assert mile.yards == 1760.0
    assert mile.inches == 63360.0

    assert mile.meters == 1609.344
    assert mile.kilometers == 1.609344

    assert str(mile) == "1 mi"
    assert repr(mile) == "Mile(1)"


def test_one_yard():
    """Confirm simple Yard conversions."""
    yard = Yard(1)

    assert yard == 1.0

    assert float(yard) == 1.0
    assert int(yard) == 1

    assert yard.inches == 36.0
    assert isclose(yard.miles, 0.00056818)

    assert isclose(yard.meters, 0.9144)
    assert isclose(yard.centimeters, 91.44)

    assert str(yard) == "1 yd"
    assert repr(yard) == "Yard(1)"


def test_one_foot():
    """Confirm simple Feet conversions."""
    foot = Foot(1)

    assert foot == 1.0

    assert float(foot) == 1.0
    assert int(foot) == 1

    assert foot.inches == 12.0
    assert foot.centimeters == 30.48

    assert str(foot) == "1 ft"
    assert repr(foot) == "Foot(1)"


def test_one_inch():
    """Confirm simple Inch conversions."""
    inch = Inch(1)

    assert inch == 1.0

    assert float(inch) == 1.0
    assert int(inch) == 1

    assert isclose(inch.feet, 0.08333333)
    assert isclose(inch.yards, 0.02777778)
    assert isclose(inch.miles, 1.5782828e-5)

    assert inch.centimeters == 2.54
    assert inch.millimeters == 25.4

    assert str(inch) == "1 in"
    assert repr(inch) == "Inch(1)"


def test_one_nautical_mile():
    """Confirm simple Nautical Mile conversions."""
    nm = NauticalMile(1)

    assert nm == 1.0

    assert float(nm) == 1.0
    assert int(nm) == 1

    assert nm.meters == 1852.0
    assert nm.kilometers == 1.852

    assert isclose(nm.feet, 6076.1155)
    assert isclose(nm.yards, 2025.3718)
    assert isclose(nm.miles, 1.1507794)

    assert str(nm) == "1 NM"
    assert repr(nm) == "NauticalMile(1)"


def test_one_parsec():
    """Confirm simple Parsec conversions."""
    pc = Parsec(1)

    assert pc == 1.0

    assert float(pc) == 1.0
    assert int(pc) == 1

    assert isclose(pc.miles, 19173513289161)
    assert isclose(pc.kilometers, 30856778570831)
    assert isclose(pc.light_years, 3.261563777)

    assert str(pc) == "1 pc"
    assert repr(pc) == "Parsec(1)"


def test_one_light_year():
    """Confirm simple Light Year conversions."""
    ly = LightYear(1)

    assert ly == 1.0

    assert float(ly) == 1.0
    assert int(ly) == 1

    assert ly.kilometers == 9460730472580.8

    assert isclose(ly.miles, 5878625373183)
    assert isclose(ly.parsecs, 0.30660139)

    assert str(ly) == "1 ly"
    assert repr(ly) == "LightYear(1)"
