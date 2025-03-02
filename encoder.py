from tqdm import tqdm
from image_processor import ImageProcessor
from encrypy_decrypt import AESCipher
class Encoder:
    def __init__(self, image_processor: ImageProcessor, encryption_key: str):
        """Initialize Encoder with an ImageProcessor instance."""
        if not isinstance(image_processor, ImageProcessor):
            raise TypeError("Expected an instance of ImageProcessor.")
        self.image_processor = image_processor
        self.aes_cipher = AESCipher(encryption_key)

    def embed_message(self, message: str):
        """Embeds a message into the LSB of an image."""
        try:
            if not isinstance(message, str):
                raise ValueError("❌ Error: Message must be a string.")

            if self.image_processor.pixel_matrix is None:
                raise RuntimeError("❌ Error: Image not loaded. Please load an image first.")

            encrypted_msg = self.aes_cipher.encrypt_message(message)
            binary_message = ''.join(format(ord(char), '08b') for char in encrypted_msg) + '1111111111111110'
            flat_pixels = self.image_processor.pixel_matrix.flatten()

            if len(binary_message) > len(flat_pixels):
                raise ValueError("❌ Error: Message is too large for this image.")

            # Embed message bit-by-bit
            for i in tqdm(range(len(binary_message)), desc="Embedding", unit="bit"):
                flat_pixels[i] = (flat_pixels[i] & ~1) | int(binary_message[i])

            self.image_processor.pixel_matrix = flat_pixels.reshape(self.image_processor.pixel_matrix.shape)
            print("✅ Message embedded successfully.")
            return True

        except Exception as e:
            print(f"⚠️ Unexpected Error: {e}")
            return False
