import cv2
import numpy as np

# Define the path to the image
image_path = "C:\\Users\\anant\\Downloads\\face.jpg"

# Load the image
img = cv2.imread(image_path)

# Check if the image was loaded successfully
if img is None:
    print("Error: Image not found.")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect edges using the Canny edge detector
edges = cv2.Canny(gray, 100, 200)

# Create a kernel for texture filtering
kernel = np.ones((5, 5), np.float32) / 25

# Apply the filter to the grayscale image to extract texture
texture = cv2.filter2D(gray, -1, kernel)

# Display the original image, edges, and texture
cv2.imshow("Original Image", img)
cv2.imshow("Edges", edges)
cv2.imshow("Texture", texture)

# Wait for a key press and close the image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
