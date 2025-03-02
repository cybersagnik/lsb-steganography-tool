from tqdm import tqdm
from image_processor import ImageProcessor
from encrypy_decrypt import AESCipher

class Decoder:
    def __init__(self, image_processor: ImageProcessor,encrypt_key: str):
        """Initialize Decoder with an ImageProcessor instance."""
        if not isinstance(image_processor, ImageProcessor):
            raise TypeError("Expected an instance of ImageProcessor.")
        self.image_processor = image_processor
        self.aes_cipher = AESCipher(encrypt_key)

    def extract_message(self):
        """Extracts the hidden message from the LSB of the image."""
        try:
            if self.image_processor.pixel_matrix is None:
                raise RuntimeError("❌ Error: Image not loaded. Please load an image first.")

            flat_pixels = self.image_processor.pixel_matrix.flatten()
            binary_message = ''.join(str(pixel & 1) for pixel in tqdm(flat_pixels, desc="Extracting", unit="bit"))

            end_index = binary_message.find('1111111111111110') #16-bit 1111111111111110 #8-bit 11111111
            if end_index == -1:
                raise ValueError("❌ Error: No valid hidden message found.")

            binary_message = binary_message[:end_index]
            encrypted_decoded_message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
            decrypted_message = self.aes_cipher.decrypt_message(encrypted_decoded_message)

            print("✅ Hidden Message Extracted Successfully:")
            print(f"📜 {decrypted_message}")
            return decrypted_message

        except Exception as e:
            print(f"⚠️ Unexpected Error: {e}")
            return None
