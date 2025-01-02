#pip install opencv-python
import cv2

# Read an image from file
image = cv2.imread('ComputerVision/Source/Foto.jpeg')  # Replace 'input_image.jpg' with your image path
 
# Show the original image
cv2.imshow('Original Image', image)

cropped_image = image[0:200, 0:100]

# Show the cropped image
cv2.imshow('Cropped Image', cropped_image)

resized_image = cv2.resize(image, (0, 0), fx=0.1, fy=0.1)
 
# Show the resized image
cv2.imshow('Resized Image', resized_image)

cv2.imwrite('cropped_image.jpg', cropped_image)
cv2.imwrite('resized_image.jpg', resized_image)

print('Images have been saved successfully.')

cv2.waitKey(0)  # Wait until any key is pressed
cv2.destroyAllWindows()

