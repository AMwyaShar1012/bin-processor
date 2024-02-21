def text_to_binary(text):
    binary_result = ""
    for char in text:
        # Convert each character to its binary representation
        binary_char = bin(ord(char))[2:].zfill(8)
        binary_result += binary_char + " "  # Add a space between each binary representation
    return binary_result.strip()  # Remove trailing space


def main():
    input_text = input("Enter text to convert to binary: ")
    binary_output = text_to_binary(input_text)
    print("Binary representation:")
    print(binary_output)


if __name__ == "__main__":
    main()
