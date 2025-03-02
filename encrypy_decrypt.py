import hashlib
import sys
import getpass
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


class AESCipher:
    def __init__(self, password: str):
        """Initialize AES Cipher using a password-derived key."""
        self.secret_key = self.derive_key(password)
        self.iv = b"2cssSxDubiMfy5vl"  # Static 16-byte IV (for AES CBC mode) change if needed

    def derive_key(self, password: str) -> bytes:
        """Derives a 32-byte AES key from the user's password."""
        return hashlib.sha256(password.encode()).digest()

    def encrypt_message(self, message: str) -> str:
        """Encrypts the message using AES-256-CBC."""
        try:
            message_padded = message + " " * (16 - len(message) % 16)
            cipher = Cipher(algorithms.AES(self.secret_key), modes.CBC(self.iv), backend=default_backend())
            encryptor = cipher.encryptor()
            encrypted_bytes = encryptor.update(message_padded.encode()) + encryptor.finalize()
            return base64.b64encode(encrypted_bytes).decode()
        except Exception as e:
            print(f"❌ Encryption Error: {e}")
            sys.exit(0)

    def decrypt_message(self, encrypted_message: str) -> str:
        """Decrypts an AES-256 encrypted message."""
        try:
            encrypted_bytes = base64.b64decode(encrypted_message)
            cipher = Cipher(algorithms.AES(self.secret_key), modes.CBC(self.iv), backend=default_backend())
            decryptor = cipher.decryptor()
            decrypted_padded = decryptor.update(encrypted_bytes) + decryptor.finalize()
            return decrypted_padded.decode().strip()
        except Exception as e:
            print(f"❌ Decryption Error: {e}")
            sys.exit(0)
