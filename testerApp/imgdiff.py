from skimage.metrics import structural_similarity as compare_ssim
import cv2
import numpy as np

def compare_and_draw_rectangles(reference_picture_path, actual_picture_path):
    # Read the reference and actual pictures
    reference_img = cv2.imread(reference_picture_path)
    actual_img = cv2.imread(actual_picture_path)

    # Convert images to grayscale for comparison
    reference_gray = cv2.cvtColor(reference_img, cv2.COLOR_BGR2GRAY)
    actual_gray = cv2.cvtColor(actual_img, cv2.COLOR_BGR2GRAY)

    # Compute the Structural Similarity Index (SSIM) between the two images
    score, diff = compare_ssim(reference_gray, actual_gray, full=True)

    # The diff image contains the difference map, scale it to range 0..255
    diff = (diff * 255).astype("uint8")

    # Threshold the difference image, followed by finding contours to
    # obtain the regions of the two input images that differ
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around the differences
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # you can adjust this value based on your needs
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(reference_img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(actual_img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Save the output images
    cv2.imwrite(actual_picture_path, actual_img)

    if len(contours) > 0:
        return True
    else:
        return False