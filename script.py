import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def show_image(image):
    plt.imshow(image, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

def main():
    img = cv.imread('messi.jpg', 0)

    # Displaying image 

    cv.imshow('image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    kernel = np.ones((5,5),np.uint8)
    erosion = cv.erode(img,kernel,iterations = 1)
    dilation = cv.dilate(img,kernel,iterations = 1)

    show_image(erosion)
    show_image(dilation)

if __name__ == "__main__":
    main()