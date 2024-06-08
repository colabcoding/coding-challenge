# HSV Region with Mouse Click

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create an HSV color gradation image
def create_hsv_gradation_image():
    height, width = 360, 1000  # You can adjust these values
    hsv_gradation = np.zeros((height, width, 3), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            hue = int((x / width) * 180)
            saturation = 255
            value = int((y / height) * 255)
            hsv_gradation[y, x] = (hue, saturation, value)

    return hsv_gradation

hsv_gradation_image = create_hsv_gradation_image()
bgr_gradation_image = cv2.cvtColor(hsv_gradation_image, cv2.COLOR_HSV2BGR)

# Global variable to store the HSV value
clicked_hsv = None

# Mouse callback function
def get_hsv_value(event, x, y, flags, param):
    global clicked_hsv
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_hsv = hsv_gradation_image[y, x]
        print(f"HSV Value at ({x}, {y}): {clicked_hsv}")
        update_plot()

# Set the mouse callback function
cv2.namedWindow('HSV Gradation')
cv2.setMouseCallback('HSV Gradation', get_hsv_value)

# Function to update the Matplotlib plot
def update_plot():
    if clicked_hsv is not None:
        plt.clf()
        plt.imshow(cv2.cvtColor(bgr_gradation_image, cv2.COLOR_BGR2RGB))
        plt.title(f"HSV Value: {clicked_hsv}")
        plt.draw()

# Initial Matplotlib plot
plt.ion()  # Turn on interactive mode
plt.imshow(cv2.cvtColor(bgr_gradation_image, cv2.COLOR_BGR2RGB))
plt.show()

# Display the image in OpenCV window
while True:
    cv2.imshow('HSV Gradation', bgr_gradation_image)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Exit on ESC key
        break

cv2.destroyAllWindows()
