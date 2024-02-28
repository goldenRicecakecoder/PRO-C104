import cv2
import numpy as np

#Creating a black image
black = np.zeros([600,600])
#f_row=black[1:2]
#f_col=black[:,1:2]
#print(f_col)
#print(f_row)
black[200:400,200:400] = 255
print(black)
cv2.imshow("black",black)
cv2.waitKey(0)



#img = cv2.imread("butterfly.jpg")
#cv2.imshow("display the image",img)
#print(img)
#gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#cv2.imshow("grayScale",gray_img)
#print(gray_img)
#cv2.waitKey(2000)