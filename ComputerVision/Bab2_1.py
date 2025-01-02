import cv2

image=cv2.imread("ComputerVision/Source/putih.jpeg")

cv2.imshow('OriginalSize', image)

#cv2.circle(image, koordinat, radius, color, thickness)
cv2.circle(image,(150,100),50,(250,0,0),2)
cv2.line(image, (5, 5),(20, 20),(0, 225, 0), 2)
cv2.imshow('Circle', image) 

resized_image = cv2.resize(image, (800, 500))
cv2.imshow('Resize', resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()