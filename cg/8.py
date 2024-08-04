import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image
image_path = "C:\\Users\\anant\\Downloads\\face.jpg"
img = cv2.imread(image_path)
if img is None:
    print("Error: Image not found.")
    exit()

height, width = img.shape[:2]

# Convert the image to RGB for displaying with Matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Define the rotation matrix (45 degrees)
angle = 45
center = (width / 2, height / 2)
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

# Define the scaling matrix
scaling_matrix = np.float32([[1.5, 0, 0], [0, 1.5, 0]])

# Define the translation matrix
translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])

# Apply transformations
rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))
scaled_img = cv2.warpAffine(img, scaling_matrix, (int(width * 1.5), int(height * 1.5)))
translated_img = cv2.warpAffine(img, translation_matrix, (width, height))

# Convert transformed images to RGB
rotated_img_rgb = cv2.cvtColor(rotated_img, cv2.COLOR_BGR2RGB)
scaled_img_rgb = cv2.cvtColor(scaled_img, cv2.COLOR_BGR2RGB)
translated_img_rgb = cv2.cvtColor(translated_img, cv2.COLOR_BGR2RGB)

# Plotting results
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.title("Original Image")
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title("Rotated Image")
plt.imshow(rotated_img_rgb)
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title("Scaled Image")
plt.imshow(scaled_img_rgb)
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title("Translated Image")
plt.imshow(translated_img_rgb)
plt.axis('off')

plt.show()
