import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i","--image",help="image input")
args = parser.parse_args()

# Initialize global variables
ref_point = []
cropping = False

def shape_selection(event, x, y, flags, param):
    global ref_point, cropping, image

    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x, y)]
        cropping = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping:
            temp_image = clone.copy()
            cv2.rectangle(temp_image, ref_point[0], (x, y), (0, 255, 0), 2)
            cv2.imshow("image", temp_image)

    elif event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x, y))
        cropping = False
        cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 2)
        cv2.imshow("image", image)

def calculate_hsv(image, rect):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    roi = hsv_image[rect[1]:rect[3], rect[0]:rect[2]]

    # Create a mask for the ROI
    mask = cv2.inRange(roi, lower, upper)
    masked_hsv = cv2.bitwise_and(roi, roi, mask=mask)
    mean_hsv = cv2.mean(roi, mask=mask)[:3]

    print(f'Average HSV value: H={mean_hsv[0]:.2f}, S={mean_hsv[1]:.2f}, V={mean_hsv[2]:.2f}')

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        cv2.drawContours(image[rect[1]:rect[3], rect[0]:rect[2]], [largest_contour], -1, (0, 255, 0), 2)
        cv2.imshow("image", image)

# Load the image
image = cv2.imread(args.image)
clone = image.copy()

# Define range of yellow color in HSV
lower = np.array([0, 100, 100])
upper = np.array([180, 255, 255])

cv2.namedWindow("image")
cv2.setMouseCallback("image", shape_selection)

print("Drag and select the area of the banana, then press 'c' to calculate HSV and contours.")

while True:
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        if len(ref_point) == 2:
            roi = [min(ref_point[0][0], ref_point[1][0]), min(ref_point[0][1], ref_point[1][1]), 
                   max(ref_point[0][0], ref_point[1][0]), max(ref_point[0][1], ref_point[1][1])]
            calculate_hsv(clone, roi)
            image = clone.copy()  # Reset the image to clear the rectangle
            ref_point = []  # Clear the reference points
        else:
            print("No region selected, please select the area of the banana.")

    elif key == ord('r'):
        image = clone.copy()
        ref_point = []

    elif key == ord('q'):
        break

cv2.destroyAllWindows()