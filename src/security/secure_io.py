import os
from pathlib import Path


def secure_write(base_dir: str, filename: str, content: str) -> None:
    """
    Securely write content to a file within a trusted base directory.

    This function prevents directory traversal attacks by resolving
    and validating file paths before writing. It ensures that the
    target file remains within the specified base directory.

    Args:
        base_dir (str): Trusted base directory for file storage.
        filename (str): User-supplied filename.
        content (str): Content to be written to the file.

    Raises:
        ValueError: If the resolved file path escapes the base directory.
    """
    base_path = Path(base_dir).resolve()
    base_path.mkdir(parents=True, exist_ok=True)

    file_path = (base_path / filename).resolve()

    if not str(file_path).startswith(str(base_path)):
        raise ValueError("Directory traversal detected")
    """
     Securely write data to a file.
     """
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
