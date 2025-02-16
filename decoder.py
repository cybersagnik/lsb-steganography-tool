from image_processor import ImageProcessor

class Decoder :
	def __init__(self , image_processor: ImageProcessor):
		"""Initialize the Decoder with an ImageProcessor instance"""
		self.image_processor = image_processor
	def extract_message(self):
		"""Extract the embedded text message from the least significant bits of the image."""
		flat_pixels = self.image_processor.pixel_matrix.flatten()
		binary_message = ''

		for pixels in flat_pixels:
			binary_message += str(pixels & 1) #Extract the LSB

		#Split binary bits into 8-bit chunks
		byte_chars = [binary_message[i:i+8] for i in range(0 , len(binary_message),8)]

		extracted_message = ''
		for byte in byte_chars:
			if byte == '11111111':
				break
			extracted_message += chr(int(byte,2))
		return extracted_message
