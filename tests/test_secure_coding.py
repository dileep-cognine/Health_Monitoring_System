import pytest
from src.security.file_validation import validate_filepath


def test_path_traversal_blocked():
    """
    Verify that directory traversal attempts are blocked.

    This test ensures that `validate_filepath` raises a ValueError
    when a user-supplied path tries to escape the trusted base directory.
    """
    with pytest.raises(ValueError):
        validate_filepath("/safe", "../etc/passwd")
