import cv2
  
originalImage = cv2.imread('osama.png')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
RGBImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
gray_normalize=grayImage / 255
originalImage_normalize = originalImage /255

(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Black white image', blackAndWhiteImage)
cv2.imshow('BGR image',originalImage)
cv2.imshow('Gray image', grayImage)
cv2.imshow('RGB image', RGBImage)
cv2.imshow('Gray Normalize image', gray_normalize)
cv2.imshow('Original_BGR Normalize image', originalImage_normalize)
  
cv2.waitKey(0)
cv2.destroyAllWindows()