import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

# Load the image
image_path = r'C:\\Users\\anant\\Downloads\\face.jpg'
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Unable to read the image.")
else:
    # Get image dimensions
    height, width, _ = image.shape
    
    # Calculate the center of the image
    center_x, center_y = width // 2, height // 2
    
    # Split the image into four quadrants
    top_left = image[0:center_y, 0:center_x]
    top_right = image[0:center_y, center_x:width]
    bottom_left = image[center_y:height, 0:center_x]
    bottom_right = image[center_y:height, center_x:width]
    
    # Create a figure with subplots
    plt.figure(figsize=(10, 10))
    
    # Display the top-left quadrant
    plt.subplot(2, 2, 1)
    plt.title('Top Left')
    plt.imshow(cv2.cvtColor(top_left, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    # Display the top-right quadrant
    plt.subplot(2, 2, 2)
    plt.title('Top Right')
    plt.imshow(cv2.cvtColor(top_right, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    # Display the bottom-left quadrant
    plt.subplot(2, 2, 3)
    plt.title('Bottom Left')
    plt.imshow(cv2.cvtColor(bottom_left, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    # Display the bottom-right quadrant
    plt.subplot(2, 2, 4)
    plt.title('Bottom Right')
    plt.imshow(cv2.cvtColor(bottom_right, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    # Show the plot
    plt.show()
