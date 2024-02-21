import cv2
import numpy as np

def image_to_binary(file_path):
    """
    Converts an image file to binary data.
    """
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)  # Read the image in grayscale
    _, binary_data = cv2.imencode('.png', img)  # Encode the image as PNG format and convert to binary
    return binary_data.tobytes()  # Convert the binary data to bytes


def resize_image(binary_data, new_size):
    """
    Resizes an image represented in binary data.
    """
    img_np = np.frombuffer(binary_data, dtype=np.uint8)  # Convert binary data back to numpy array
    img = cv2.imdecode(img_np, cv2.IMREAD_GRAYSCALE)  # Decode image from numpy array
    resized_img = cv2.resize(img, new_size)  # Resize the image
    _, resized_binary_data = cv2.imencode('.png', resized_img)  # Encode the resized image as PNG format
    return resized_binary_data.tobytes()  # Convert the binary data of resized image to bytes


def apply_edge_detection(binary_data):
    """
    Applies edge detection to an image represented in binary data.
    """
    img_np = np.frombuffer(binary_data, dtype=np.uint8)  # Convert binary data back to numpy array
    img = cv2.imdecode(img_np, cv2.IMREAD_GRAYSCALE)  # Decode image from numpy array
    edges = cv2.Canny(img, 100, 200)  # Apply Canny edge detection
    _, edges_binary_data = cv2.imencode('.png', edges)  # Encode the edge-detected image as PNG format
    return edges_binary_data.tobytes()  # Convert the binary data of edge-detected image to bytes


def main():
    file_path = input("Enter the path to the image file: ")
    original_binary_data = image_to_binary(file_path)

    # Resize the image to a new size
    new_size = (300, 300)
    resized_binary_data = resize_image(original_binary_data, new_size)

    # Apply edge detection to the original image
    edge_detected_binary_data = apply_edge_detection(original_binary_data)

    # Write the processed images to files for demonstration
    with open("resized_image.png", "wb") as resized_file:
        resized_file.write(resized_binary_data)

    with open("edge_detected_image.png", "wb") as edge_detected_file:
        edge_detected_file.write(edge_detected_binary_data)

    print("Processing completed. Resized and edge-detected images saved as 'resized_image.png' and 'edge_detected_image.png'.")


if __name__ == "__main__":
    main()
