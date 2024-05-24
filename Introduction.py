import os
import cv2
#Reading an image
img1 = cv2.imread("OpenCV.png")
img2 = cv2.imread("Pikachu.png")
print(img1)
#Showing an image as a window
cv2.imshow("test1", img1)
cv2.waitKey(0)
path = "C:/Users/USER/OneDrive/Desktop/"
os.chdir(path)
cv2.imwrite("Test.png", img1)
#splitting colours from the image
B,G,R = cv2.split(img1)
cv2.imshow("blue", B)
cv2.waitKey(0)
cv2.imshow("green", G)
cv2.waitKey(0)
cv2.imshow("red", R)
cv2.waitKey(0)
print(img1.shape)
#[start:end,start:end] -> [0:100,100:200]
RoI = img1[0:100,100:200]
cv2.imshow("cropped_img", RoI)
cv2.waitKey(0)
cv2.destroyAllWindows()