# importing cv2
import cv2

# importing numpy
import numpy as np

# path
path = ('C:\\Users\\user\\Desktop\\newp\\venv\\resources\\g.png')

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Creating kernel
kernel = np.ones((6, 6), np.uint8)

# Using cv2.erode() method
image = cv2.erode(image, kernel, cv2.BORDER_REFLECT)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()