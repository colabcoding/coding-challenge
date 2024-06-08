# HSV Region with Drag Mouse Event

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

# Global variables to store the HSV values and region coordinates
clicked_hsv = None
start_point = None
end_point = None
dragging = False

# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    global clicked_hsv, start_point, end_point, dragging
    if event == cv2.EVENT_LBUTTONDOWN:
        start_point = (x, y)
        dragging = True
    elif event == cv2.EVENT_MOUSEMOVE and dragging:
        end_point = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        end_point = (x, y)
        dragging = False
        if start_point and end_point:
            x1, y1 = start_point
            x2, y2 = end_point
            if x1 > x2:
                x1, x2 = x2, x1
            if y1 > y2:
                y1, y2 = y2, y1
            region = hsv_gradation_image[y1:y2, x1:x2]
            if region.size > 0:
                min_hsv = np.min(region, axis=(0, 1))
                max_hsv = np.max(region, axis=(0, 1))
                print(f"Region HSV Min: {min_hsv}, Max: {max_hsv}")
                update_plot(min_hsv, max_hsv)

# Set the mouse callback function
cv2.namedWindow('HSV Gradation')
cv2.setMouseCallback('HSV Gradation', mouse_callback)

# Function to update the Matplotlib plot
def update_plot(min_hsv=None, max_hsv=None):
    plt.clf()
    plt.imshow(cv2.cvtColor(bgr_gradation_image, cv2.COLOR_BGR2RGB))
    if min_hsv is not None and max_hsv is not None:
        plt.title(f"HSV Min: {min_hsv}, Max: {max_hsv}")
    elif clicked_hsv is not None:
        plt.title(f"HSV Value: {clicked_hsv}")
    plt.draw()

# Initial Matplotlib plot
plt.ion()  # Turn on interactive mode
plt.imshow(cv2.cvtColor(bgr_gradation_image, cv2.COLOR_BGR2RGB))
plt.show()

# Display the image in OpenCV window
while True:
    display_image = bgr_gradation_image.copy()
    if start_point and end_point:
        cv2.rectangle(display_image, start_point, end_point, (255, 0, 0), 2)
    cv2.imshow('HSV Gradation', display_image)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Exit on ESC key
        break

cv2.destroyAllWindows()
