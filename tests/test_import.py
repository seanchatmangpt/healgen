"""Test HealGen."""

import healgen


def test_import() -> None:
    """Test that the app can be imported."""
    assert isinstance(healgen.__name__, str)
