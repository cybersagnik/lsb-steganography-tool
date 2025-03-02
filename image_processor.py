import numpy as np
from PIL import Image
import os

class ImageProcessor:
    def __init__(self, image_path: str):
        """Initialize with an image path."""
        self.image_path = image_path
        self.pixel_matrix = None

    def load_image(self):
        """Loads an image and converts it into a pixel matrix."""
        try:
            if not os.path.exists(self.image_path):
                raise FileNotFoundError(f"❌ Error: File '{self.image_path}' not found.")

            with Image.open(self.image_path) as img:
                img = img.convert("RGB")  # Ensure it's in RGB mode
                self.pixel_matrix = np.array(img)
            print(f"✅ Image '{self.image_path}' loaded successfully.")
            return True

        except FileNotFoundError as fe:
            print(fe)
        except Exception as e:
            print(f"⚠️ Unexpected Error: {e}")
        return False

    def save_image(self, output_path: str):
        """Saves the pixel matrix as an image."""
        try:
            if self.pixel_matrix is None:
                raise RuntimeError("❌ Error: No image data to save.")

            img = Image.fromarray(self.pixel_matrix)
            img.save(output_path)
            print(f"✅ Image saved as '{output_path}'.")
        except Exception as e:
            print(f"⚠️ Error saving image: {e}")
