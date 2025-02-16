from image_processor import ImageProcessor
from encoder import Encoder
from decoder import Decoder

class Steganography:
	def __init__(self , image_path):
		"""Initialize Stegnography with an image path."""
		self.image_processor = ImageProcessor(image_path)

	def embed_message(self , message , output_image):
		"""Embed a message into an image and save the module"""
		if self.image_processor.load_image():
			encoder = Encoder(self.image_processor)
			if encoder.embed_message(message):
				self.image_processor.save_image(output_image)
				print(f"Message successfully embedded in {output_image}")
	def extract_message(self):
		"""Extract a hidden message from the image"""
		if self.image_processor.load_image():
			decoder = Decoder(self.image_processor)
			return decoder.extract_message()
