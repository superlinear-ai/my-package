"""Test My Package."""

import my_package


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(my_package.__name__, str)
