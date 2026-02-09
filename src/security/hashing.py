import hashlib
import os
from typing import Tuple


def hash_password(password: str) -> Tuple[str, str]:
    """
    Hash a password using SHA-256 with a randomly generated salt.

    A unique salt is generated for each password to protect against
    rainbow table and precomputed hash attacks.

    Args:
        password (str): Plaintext password to hash.

    Returns:
        Tuple[str, str]: A tuple containing:
            - salt (str): Hex-encoded random salt
            - hashed_password (str): SHA-256 hash of salt + password
    """
    salt = os.urandom(16).hex()
    hashed = hashlib.sha256((salt + password).encode()).hexdigest()
    return salt, hashed


def verify_password(password: str, salt: str, hashed_password: str) -> bool:
    """
    Verify a plaintext password against a stored hash.

    Recomputes the hash using the stored salt and compares it
    with the expected hashed password.

    Args:
        password (str): Plaintext password to verify.
        salt (str): Salt used during hashing.
        hashed_password (str): Stored password hash.

    Returns:
        bool: True if the password is valid, otherwise False.
    """
    verified_password = hashlib.sha256((salt + password).encode()).hexdigest()
    return verified_password == hashed_password
