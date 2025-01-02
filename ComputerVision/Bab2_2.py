import cv2

image=cv2.imread("ComputerVision/Source/putih.jpeg")
text="Test"
position=(50,50)
font=cv2.FONT_HERSHEY_SIMPLEX
font_scale=1
color=(0,0,255)
thickness=2

cv2.putText(image, text, position, font, font_scale, color, thickness, cv2.LINE_AA)
resized_image= cv2. resize(image, (400,200))
cv2.imshow("Image_text", image)
cv2.imshow("Resized", resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()