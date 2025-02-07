"""Tests for the fio utils module."""

from mimspy import configs


def test_version() -> None:
    """Test that the version is correctly set."""
    assert configs.__version__ == "0.7.3", "Version mismatch"


def test_name() -> None:
    """Test that the package name is correctly set."""
    assert configs.APP_NAME == "Mimspy", "Package name mismatch"


def test_organization() -> None:
    """Test that the organization is correctly set."""
    assert configs.APP_ORGANIZATION == "CREL", "Organization mismatch"


def test_author() -> None:
    """Test that the author name is correctly set."""
    assert configs.APP_AUTHOR == "Brady Fry", "Author name mismatch"


def test_email() -> None:
    """Test that the author email is correctly set."""
    assert configs.APP_EMAIL == "dev@chaytus.com", "Email mismatch"


def test_version_alias() -> None:
    """Test that VERSION alias points to the same value as __version__."""
    assert configs.__version__ == configs.APP_VERSION, "VERSION alias mismatch"
