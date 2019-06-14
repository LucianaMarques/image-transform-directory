import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image
import argparse
import os
from os import listdir
from os.path import isfile, join

def show_image(image):
    plt.imshow(image, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

def create_folders(source, destination):
    source_path = os.path.dirname(source)
    destination_path = os.path.dirname(destination)

    try:
        os.stat(source_path)
    except:
        os.mkdir(source_path)
    
    try:
        os.stat(destination_path)
    except:
        os.mkdir(destination_path)

def apply_transformation(images, destination, transform):
    i = 1
    for img in images:
        image = cv.imread(img, 0)
    
        # Uncomment for displaying image 
        # cv.imshow('image', image)
        # cv.waitKey(0)
        # cv.destroyAllWindows()

        kernel = np.ones((5,5),np.uint8)

        if (transform == 'erosion'):
            transf_result = cv.erode(image, kernel, iterations = 3)
        else:
            transf_result = cv.dilate(image, kernel, iterations = 3)

        image_name = 'image'+str(i)+'.png'

        # Uncomment for plotting the image transformation result
        show_image(transf_result)
        
        cv.imwrite(os.path.join(destination, image_name), transf_result)
        
        i += 1

def main():
    parser = argparse.ArgumentParser(description='Process images from a folder and save them to another')

    parser.add_argument('--origin', dest='org', type=str, required=True)
    parser.add_argument('--destiny', dest='dest', type=str, required=True)
    parser.add_argument('--transform', dest='transf', type=str, required=True)

    args = parser.parse_args()

    # if origin and destination folders do not exist, create them
    create_folders(args.org, args.dest)

    images = [args.org+img for img in listdir(args.org) if isfile(join(args.org, img))]

    apply_transformation(images, args.dest, args.transf)

if __name__ == "__main__":
    main()
