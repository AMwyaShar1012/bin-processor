from PIL import Image

def encode_message(image_path, message):
    """
    Encode a secret message into an image using LSB steganography.
    """
    img = Image.open(image_path)
    width, height = img.size
    message_length = len(message)

    # Ensure the message fits within the image
    if message_length * 8 > width * height:
        raise ValueError("Message is too large to be encoded in the image")

    # Convert message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # Encode the binary message into the least significant bits of the image pixels
    binary_index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))
            for i in range(3):  # Iterate over RGB channels
                if binary_index < len(binary_message):
                    pixel[i] = pixel[i] & ~1 | int(binary_message[binary_index])
                    binary_index += 1
            img.putpixel((x, y), tuple(pixel))

    # Save the encoded image
    encoded_image_path = "encoded_" + image_path
    img.save(encoded_image_path)
    print(f"Message encoded successfully. Encoded image saved as '{encoded_image_path}'.")


def decode_message(encoded_image_path):
    """
    Decode a secret message from an image encoded using LSB steganography.
    """
    img = Image.open(encoded_image_path)
    width, height = img.size

    # Extract the binary message from the least significant bits of the image pixels
    binary_message = ""
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            for channel in pixel:
                binary_message += str(channel & 1)

    # Convert binary message to ASCII characters
    decoded_message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        decoded_message += chr(int(byte, 2))
        if decoded_message.endswith('\x00'):  # Stop decoding at null terminator
            break

    return decoded_message


def main():
    choice = input("Choose:\n1. Encode message\n2. Decode message\n")
    if choice == "1":
        image_path = input("Enter the path to the image file: ")
        message = input("Enter the message to encode: ")
        encode_message(image_path, message)
    elif choice == "2":
        encoded_image_path = input("Enter the path to the encoded image file: ")
        decoded_message = decode_message(encoded_image_path)
        print("Decoded message:", decoded_message)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
