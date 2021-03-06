import numpy as np 
import cv2 

width = 500
height = 600
  
img = np.zeros((height, width, 3), np.uint8) 
  
p1 = (17, 10) 
p2 = (10, 83) 
p3 = (83, 17) 
  
cv2.line(img, p1, p2, (255, 0, 0), 3) 
cv2.line(img, p2, p3, (255, 0, 0), 3) 
cv2.line(img, p1, p3, (255, 0, 0), 3) 
   
cv2.imshow("image", img) 
cv2.waitKey(0) 
cv2.destroyAllWindows()

