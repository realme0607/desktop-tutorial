import cv2
image_path = 'C:\\Users\\anant\\Downloads\\face.jpg'
image = cv2.imread(image_path)
if image is None:
 print(f"Error loading image at {image_path}")
else:
 gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)
 median_blur = cv2.medianBlur(image, 5)
 bilateral_filter = cv2.bilateralFilter(image, 9, 75, 75)
 cv2.imshow('Original Image', image)
 cv2.imshow('Gaussian Blur', gaussian_blur)
 cv2.imshow('Median Blur', median_blur)
 cv2.imshow('Bilateral Filter', bilateral_filter)
 cv2.waitKey(0) 
 cv2.destroyAllWindows()
