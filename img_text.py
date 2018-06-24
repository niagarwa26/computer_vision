import cv2

#loading image
img = cv2.imread('dog1.jpeg',1)
img1 = cv2.imread('dog1.jpeg',0)


# print height and width 
print (img.shape)

#to write a text on image 
#deciding font type
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"dog",(50,50),font,3,(100,23,200),lineType = cv2.LINE_AA)

#to display that image 
cv2.imshow("txtimg",img)




#image key handler
#image window holder activate 

cv2.waitKey(0)

# wait key will destroy by using q button 

cv2.destroyAllWindows()

