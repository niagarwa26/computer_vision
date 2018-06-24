#!usr/bin/python2

import cv2

#loading image
img = cv2.imread('dog1.jpeg',1)
img1 = cv2.imread('dog1.jpeg',0)

# print height and width 
print (img.shape)

#to display that image 
cv2.imshow("dog",img)
cv2.imshow("doguncolord",img1)

#image key handler
#image window holder activate 

cv2.waitKey(0)

# wait key will destroy by using q button 

cv2.destroyAllWindows()



