import cv2
import numpy
Star = cv2.imread("Star.jpg")
Diamond = cv2.imread("Diamond.jpg")
Mountain = cv2.imread("Mountain.jpg")
Tiger = cv2.imread("Tiger.jpg")
Pikachu = cv2.imread("Pikachu.png")
# Arithmetic Operation on Images
# Pixel values are directly added / subtracted for 2 images
# make sure that the 2 images are of same size
"""
sum = cv2.addWeighted(Star,0.2,Diamond,1,0)
cv2.imshow("window", sum)
cv2.waitKey(0)
sub = cv2.subtract(Star, Diamond)
cv2.imshow("window2", sub)
cv2.waitKey(0)
# Gaussian Blur - used mostly in machine learning preprocessing steps
blur = cv2.GaussianBlur(Mountain, (5,5), 0, 0)
cv2.imshow("window3", blur)
cv2.waitKey(0)
# Median Blur - used in digital processing preserves edges but removes noise
medblur = cv2.medianBlur(Tiger, 3)
cv2.imshow("window4", medblur)
cv2.waitKey(0)
# Bilateral Blur - only sharp edges are preserved here
bilblur = cv2.bilateralFilter(Mountain, 9, 50, 50)
cv2.imshow("window5", bilblur)
cv2.waitKey(0)
# Erosion of an image, corners are trimmed in erosion
matrix = numpy.ones((3, 3), numpy.uint8)
erosion = cv2.erode(Pikachu, matrix)
cv2.imshow("window6", erosion)
cv2.waitKey(0)
"""
border = cv2.copyMakeBorder(Pikachu,1,415,2,2,cv2.BORDER_REFLECT)
cv2.imshow("window7", border)
cv2.waitKey(0)