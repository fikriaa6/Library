import cv2
import numpy as np

image=cv2.imread("ComputerVision/Source/kucing.jpeg")
cv2.imshow("Original",image)
#image.shape
#   - memberikan dimensi gambar dalam format (height, width, channels) untuk gambar berwarna
#   - :2 mengambil 2 elemen pertama yaitu height (h), dan width (w)
#   contoh: jika gambar berukuran 400x300 piksel, maka h= 400 dan w= 300 
(h,w)=image.shape[:2]

#Applying Rotation
center=(w//2,h//2)                                          # menetukan titik pusat rotasi
rotation_matrix=cv2. getRotationMatrix2D(center,45,1)       # membuat matriks rotasi
rotated_image=cv2.warpAffine(image,rotation_matrix, (w,h))
cv2.imshow("Rotation", rotated_image)

#Applying Translation
translation_matrix=np.float32([[1,0,50],[0,1,50]])
translated_image=cv2.warpAffine(image, translation_matrix,(w,h))
cv2.imshow("Translation",translated_image)

#Brightness and Contrast adjustment
bright_contrast_image=cv2.convertScaleAbs(image, alpha=1.5, beta=50)

#Applying Gaussian Blur
blurred_image=cv2.GaussianBlur(image, (15, 15), 0)

#Applying Sharpening
kernel= np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharpened_image = cv2.filter2D(image,-1, kernel)

cv2.imshow("Brightness and Contrast", bright_contrast_image)
cv2.imshow("Gaussian Blur", blurred_image)
cv2.imshow("Sharpened Image", sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()