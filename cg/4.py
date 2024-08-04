#4. Develop a program to demonstrate 2D transformation on basic objects Program
import cv2
import numpy as np

# Canvas setup
canvas_width = 500
canvas_height = 500
canvas = np.ones((canvas_height, canvas_width, 3), dtype=np.uint8) * 255

# Define the object points
obj_points = np.array([[100, 100], [200, 100], [200, 200], [100, 200]], dtype=np.int32)

# Translation matrix
translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])

# Apply translation
translated_obj = cv2.transform(np.array([obj_points]), translation_matrix)[0]

# Rotation matrix
center = (150, 150)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1)

# Apply rotation
rotated_obj = cv2.transform(np.array([translated_obj]), rotation_matrix)[0]

# Scaling matrix
scaling_matrix = np.float32([[1.5, 0, 0], [0, 1.5, 0]])

# Apply scaling
scaled_obj = cv2.transform(np.array([rotated_obj]), scaling_matrix)[0]

# Draw the shapes
cv2.polylines(canvas, [obj_points], True, (0, 0, 0), 2)
cv2.polylines(canvas, [translated_obj], True, (0, 255, 0), 2)
cv2.polylines(canvas, [rotated_obj], True, (255, 0, 0), 2)
cv2.polylines(canvas, [scaled_obj], True, (0, 0, 255), 2)

# Display the canvas
cv2.imshow("2D Transformations", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
