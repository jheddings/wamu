"""Unit tests for temperature units."""

import wamu


def assert_is_freezing(temp: wamu.temperature.Temperature):
    """Assert all values match expected levels for freezing."""
    assert temp.celcius == 0.0
    assert temp.fahrenheit == 32.0
    assert temp.kelvin == 273.15


def test_convert_none():
    """Make sure that conversions with None are also None."""
    tempC = wamu.Celsius(None)

    assert tempC.celcius is None
    assert tempC.fahrenheit is None
    assert tempC.kelvin is None


def test_degC_freezing():
    """Confirm Celsius conversions for freezing."""
    tempC = wamu.Celsius(0)

    assert tempC == 0.0

    assert int(tempC) == 0
    assert float(tempC) == 0.0

    assert str(tempC) == "0 °C"
    assert repr(tempC) == "Celsius(0)"

    assert_is_freezing(tempC)


def test_degF_freezing():
    """Confirm Fahrenheit conversions for freezing."""
    tempF = wamu.Fahrenheit(32)

    assert tempF == 32.0

    assert int(tempF) == 32
    assert float(tempF) == 32.0

    assert str(tempF) == "32 °F"
    assert repr(tempF) == "Fahrenheit(32)"

    assert_is_freezing(tempF)


def test_degK_freezing():
    """Confirm Kelvin conversions for freezing."""
    tempK = wamu.Kelvin(273.15)

    assert tempK == 273.15

    assert int(tempK) == 273
    assert float(tempK) == 273.15

    assert str(tempK) == "273.15 K"
    assert repr(tempK) == "Kelvin(273.15)"

    assert_is_freezing(tempK)


def test_boiling_temps():
    """Confirm conversions for boiling temperatures."""
    tempF = wamu.Fahrenheit(212.0)
    assert tempF.celcius == 100.0
    assert tempF.kelvin == 373.15

    tempC = wamu.Celsius(100.0)
    assert tempC.fahrenheit == 212.0
    assert tempF.kelvin == 373.15

    tempK = wamu.Kelvin(373.15)
    assert tempK.celcius == 100.0
    assert tempK.fahrenheit == 212.0
