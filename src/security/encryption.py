from cryptography.fernet import Fernet


class EncryptionManager:
    """
    Manages symmetric encryption and decryption of sensitive data.

    Uses the Fernet implementation from the `cryptography` library,
    providing authenticated encryption with a shared secret key.
    """

    def __init__(self, key: bytes | None = None) -> None:
        """
        Initialize the EncryptionManager.

        If no key is provided, a new secure key is generated.

        Args:
            key (bytes | None): Optional pre-generated encryption key.
        """
        self._key = key or Fernet.generate_key()
        self._cipher = Fernet(self._key)

    @property
    def key(self) -> bytes:
        """
        Retrieve the encryption key.

        Returns:
            bytes: The symmetric encryption key.
        """
        return self._key

    def encrypt(self, data: str) -> bytes:
        """
        Encrypt plaintext data.

        Args:
            data (str): Plaintext string to encrypt.

        Returns:
            bytes: Encrypted token.
        """
        return self._cipher.encrypt(data.encode())

    def decrypt(self, token: bytes) -> str:
        """
        Decrypt an encrypted token.

        Args:
            token (bytes): Encrypted token to decrypt.

        Returns:
            str: Decrypted plaintext string.
        """
        return self._cipher.decrypt(token).decode()
