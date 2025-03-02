import argparse
from encoder import Encoder
from decoder import Decoder
from image_processor import ImageProcessor
from colorama import Fore, Style, init

init(autoreset=True)  # Enable color support

def main():
    parser = argparse.ArgumentParser(description="🔐 LSB Steganography Tool")
    parser.add_argument("mode", choices=["encode", "decode"], help="Choose mode: encode or decode")
    parser.add_argument("image", help="Path to the image file")
    parser.add_argument("--message", help="Message to hide (only for encoding)")
    parser.add_argument("--output", help="Output image file (only for encoding)")
    parser.add_argument("--password", help="Password for encrypting and decrypting message")

    args = parser.parse_args()
    processor = ImageProcessor(args.image)

    if not processor.load_image():
        print(Fore.RED + "❌ Failed to load image. Exiting.")
        return

    if args.mode == "encode":
        if not args.message or not args.output:
            print(Fore.YELLOW + "⚠️ Please provide a message and output filename for encoding.")
            return
        if not args.password:
        	  print(Fore.YELLOW + "⚠️ Please provide a key for encrypting the message.")
        	  return
        encoder = Encoder(processor, args.password)
        if encoder.embed_message(args.message):
            processor.save_image(args.output)

    elif args.mode == "decode":
        if not args.password :
           print(Fore.YELLOW + "⚠️ Cannot Decode without password.")
           return;
        decoder = Decoder(processor, args.password)
        hidden_message = decoder.extract_message()
        if hidden_message:
            print(Fore.GREEN + f"📜 Hidden Message: {hidden_message}")

if __name__ == "__main__":
    main()
