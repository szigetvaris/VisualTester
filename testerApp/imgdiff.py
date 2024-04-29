# https://pyimagesearch.com/2017/06/19/image-difference-with-opencv-and-python/

from skimage.metrics import structural_similarity
import cv2
import numpy as np

def compare_and_draw_rectangles(reference_picture_path, actual_picture_path):
    # Read the reference and actual pictures
    reference_img = cv2.imread(reference_picture_path)
    actual_img = cv2.imread(actual_picture_path)

    # Convert images to grayscale for comparison
    reference_gray = cv2.cvtColor(reference_img, cv2.COLOR_BGR2GRAY)
    actual_gray = cv2.cvtColor(actual_img, cv2.COLOR_BGR2GRAY)

    # Find differences between the images
    difference_img = cv2.absdiff(reference_gray, actual_gray)
    _, threshold_img = cv2.threshold(difference_img, 30, 255, cv2.THRESH_BINARY)

    # Find contours of the differences
    contours, _ = cv2.findContours(threshold_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around the differences
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(reference_img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(actual_img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display the images with rectangles
    # cv2.imshow('Reference Image with Rectangles', reference_img)
    # cv2.imshow('Actual Image with Rectangles', actual_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    cv2.imwrite('./../data/result/ref_diff.png', reference_img)
    cv2.imwrite('./../data/result/act_diff.png', actual_img)
    
    # return True/False if len(contours) > 0


# before = cv2.imread('./../data/p3_ref.png')
# after = cv2.imread('./../data/p3.png')

# # Calculate the per-element absolute difference between 
# # two arrays or between an array and a scalar
# diff = 255 - cv2.absdiff(before, after)

# cv2.imshow('diff', diff)
# cv2.waitKey()

a = './../data/p3_ref.png'
b = './../data/p3.png'

compare_and_draw_rectangles(b, a)