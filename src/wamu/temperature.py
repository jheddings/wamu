"""Working with temperature quantities."""

from abc import ABC, abstractproperty

from .quantity import Quantity, UnitSymbol


class TemperatureUnit(UnitSymbol):
    """Symbols for temperature units."""

    CELCIUS = "°C"
    DEGREES_CELCIUS = "°C"
    C = "°C"
    DEGREES_C = "°C"

    FAHRENHEIT = "°F"
    DEGREES_FAHRENHEIT = "°F"
    F = "°F"
    DEGREES_F = "°F"

    KELVIN = "K"
    DEGREES_KELVIN = "K"
    K = "K"
    DEGREES_K = "K"


class Temperature(Quantity, ABC):
    """Base for all temperature unit types."""

    @abstractproperty
    def degrees_celcius(self):
        """Return the value of this quantity as Celsius."""

    @abstractproperty
    def degrees_fahrenheit(self):
        """Return the value of this quantity as Fahrenheit."""

    @property
    def degrees_kelvin(self):
        """Return the value of this quantity as Kelvin."""
        return self.degrees_celcius + 273.15


class Celsius(Temperature):
    """A representation of Celsius quantities."""

    @property
    def symbol(self):
        """Return the unit symbol for this quantity."""
        return TemperatureUnit.CELCIUS

    @property
    def degrees_celcius(self):
        """Return the value of this quantity as Celsius."""
        return self.value

    @property
    def degrees_fahrenheit(self):
        """Return the value of this quantity as Fahrenheit."""
        return (self.degrees_celcius * 1.8) + 32.0


class Fahrenheit(Temperature):
    """A representation of Fahrenheit quantities."""

    @property
    def symbol(self):
        """Return the unit symbol for this quantity."""
        return TemperatureUnit.FAHRENHEIT

    @property
    def degrees_celcius(self):
        """Return the value of this quantity as Celsius."""
        return (self.degrees_fahrenheit - 32.0) / 1.8

    @property
    def degrees_fahrenheit(self):
        """Return the value of this quantity as Fahrenheit."""
        return self.value


class Kelvin(Celsius):
    """A representation of Kelvin quantities."""

    @property
    def symbol(self):
        """Return the unit symbol for this quantity."""
        return TemperatureUnit.KELVIN

    @property
    def degrees_celcius(self):
        """Return the value of this quantity as Celsius."""
        return self.value - 273.15
