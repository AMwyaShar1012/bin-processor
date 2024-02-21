def binary_to_text(binary_module):
    """
    Converts a binary module into text (ASCII characters).
    """
    binary_chars = binary_module.split()  # Split binary module into individual binary characters
    text = ""
    for binary_char in binary_chars:
        decimal_value = int(binary_char, 2)  # Convert binary to decimal
        text += chr(decimal_value)  # Convert decimal to ASCII character
    return text


def main():
    # Example usage
    binary_module = "01010101 01100100 01100101 01110010 00100000 01010100 01100101 01111000 01110100" # Example module
    decoded_text = binary_to_text(binary_module)
    print("Decoded text:", decoded_text)


if __name__ == "__main__":
    main()
