from PIL import Image
import numpy as np

class ImageProcessor:
	def __init__(self , image_path: str):
		"""Initialize the ImageProcessor with the given image file path."""
		self.image_path = image_path
		self.image = None
		self.pixel_matrix = None

	def load_image(self):
		"""Load the image and convert it into a pixel matrix."""
		try:
			self.image = Image.open(self.image_path).convert("RGB")
			self.pixel_matrix = np.array(self.image)
			return True
		except Exception as e :
			print(f"Error Loading image : {e}")
			return False

	def get_pixel_matrix(self):
		"""Return the pixel matrix of the loaded image"""
		if self.pixel_matrix is not None:
			return self.pixel_matrix
		else:
			print("Image not loaded . Call load_image() first")
			return None
	def save_image(self, output_path: str):
		"""Save the modified pixel matrix back as an image."""
		try:
			if self.pixel_matrix is not None:
				new_image = Image.fromarray(self.pixel_matrix.astype(np.uint8))
				new_image.save(output_path)
				print(f"Image saved successfully at {output_path}")
			else:
				print("No pixel matrix to save")
		except Exception as e :
			print(f"Error saving image: {e}")
