import os


def validate_filepath(base_dir: str, user_path: str) -> str:
    """
    Validate and sanitize a user-supplied file path.

    This function prevents directory traversal attacks by ensuring
    the resolved path remains within the specified base directory.

    Args:
        base_dir (str): Trusted base directory.
        user_path (str): User-supplied relative file path.

    Returns:
        str: Absolute, validated file path.

    Raises:
        ValueError: If the resolved path escapes the base directory.
    """
    full_path = os.path.abspath(os.path.join(base_dir, user_path))
    if not full_path.startswith(os.path.abspath(base_dir)):
        raise ValueError("Invalid file path detected")
    return full_path
