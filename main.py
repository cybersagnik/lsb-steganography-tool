import argparse
import time
from tqdm import tqdm
from colorama import Fore, Style, init
from steganography import Steganography

# Initialize colorama
init(autoreset=True)

def print_success(msg):
    print(Fore.GREEN + "✅ " + Style.BRIGHT + msg)

def print_error(msg):
    print(Fore.RED + "❌ " + Style.BRIGHT + msg)

def print_info(msg):
    print(Fore.CYAN + "ℹ️ " + Style.BRIGHT + msg)

def show_progress(task="Processing", duration=3):
    """Displays a progress bar for the given task."""
    print_info(f"{task}... Please wait ⏳")
    for _ in tqdm(range(100), desc="🚀 Progress", ncols=100):
        time.sleep(duration / 100)  # Simulate processing

def main():
    parser = argparse.ArgumentParser(description="🔒 LSB Steganography Tool 🎭")
    parser.add_argument("mode", choices=["encode", "decode"], help="Choose mode: encode or decode")
    parser.add_argument("image", help="🖼️ Path to the image file")
    parser.add_argument("--message", help="💬 Message to hide (required for encoding)")
    parser.add_argument("--output", help="💾 Output image path (required for encoding)")

    args = parser.parse_args()

    steg = Steganography(args.image)

    if args.mode == "encode":
        if not args.message or not args.output:
            print_error("Encoding requires a message and an output image path.")
            return
        show_progress("🔏 Embedding message")
        steg.embed_message(args.message, args.output)
        print_success(f"🎉 Message successfully embedded in {args.output}")

    elif args.mode == "decode":
        show_progress("🔍 Extracting message")
        hidden_message = steg.extract_message()
        if hidden_message:
            print_success(f"📜 Extracted message: {hidden_message}")
        else:
            print_error("😞 No hidden message found!")

if __name__ == "__main__":
    main()
