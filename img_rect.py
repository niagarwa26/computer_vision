import cv2

#loading image
img = cv2.imread('dog1.jpeg',1)
img1 = cv2.imread('dog1.jpeg',0)


# print height and width 
print (img.shape)

#to draw a rectangle in dog image
#image data,start corner point,end corner point,color,line width

cv2.rectangle(img,(50,50),(100,200),(0,0,255),3)

#to display that image 
cv2.imshow("rectimg",img)




#image key handler
#image window holder activate 

cv2.waitKey(0)

# wait key will destroy by using q button 

cv2.destroyAllWindows()

