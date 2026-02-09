from src.security.hashing import hash_password, verify_password
from src.security.encryption import EncryptionManager


def test_password_hashing():
    """
    Verify password hashing and verification workflow.

    This test ensures that:
    - A correct password validates successfully
    - An incorrect password fails verification
    """
    salt, hashed = hash_password("secret")
    assert verify_password("secret", salt, hashed)
    assert not verify_password("wrong", salt, hashed)


def test_encryption_cycle():
    """
    Verify encryption and decryption cycle integrity.

    This test ensures that data encrypted using the
    EncryptionManager can be decrypted back to its
    original plaintext form.
    """
    enc = EncryptionManager()
    data = "financial_data"
    encrypted = enc.encrypt(data)
    decrypted = enc.decrypt(encrypted)
    assert decrypted == data
