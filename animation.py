import cv2
import numpy as np
import time


spritesheet = cv2.imread('runningcat.png')
cat = spritesheet.copy()

frameX = 4
frameY = 2

height = cat.shape[0] // frameX
width = cat.shape[1]//frameY


i=0
j = 0
while True:
    time.sleep(1/20)
    cv2.imshow('spritesheet',cat[height * j:height * (j+1),width * i:width * (i+1),:])
    i+=1
    if i == 2:
        j+=1
        j = j % frameX
        
    i = i % frameY
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
