"""Unit tests for velocity units."""

from conftest import isclose

import wamu


def test_one_mmph():
    """Confirm simple MillimeterPerHour conversions."""
    mmph = wamu.MillimetersPerHour(1)

    assert mmph == 1.0

    assert float(mmph) == 1.0
    assert int(mmph) == 1

    assert mmph.cmph == 0.1
    assert isclose(mmph.inph, 0.03937)

    assert str(mmph) == "1 mm/h"
    assert repr(mmph) == "MillimetersPerHour(1)"
