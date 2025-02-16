from image_processor  import ImageProcessor

class Encoder:
	def __init__(self, image_processor: ImageProcessor):
		"""Initialize the Encoder with an ImageProcessor instance"""
		self.image_processor = image_processor

	def embed_message(self , message: str):
		"""Embed a text message into the least significant bits of the image"""
		binary_msg = ''.join(format(ord(char) , '08b') for char in message) + '11111111' #EOF
		flat_pixels = self.image_processor.pixel_matrix.flatten()
		if len(binary_msg) > len(flat_pixels):
			print("Message is too large to be embedded in the image")
			return False

		for i in range(len(binary_msg)):
			flat_pixels[i] = (flat_pixels[i] & ~1) | int(binary_msg[i])

		self.image_processor.pixel_matrix = flat_pixels.reshape(self.image_processor.pixel_matrix.shape)
		print("Message embedded successfully")
		return True
