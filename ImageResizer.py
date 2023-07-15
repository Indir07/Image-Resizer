#   pip install opencv-python

import cv2

print("Welcome to Image Resizer Project Created by Indir Solanki\n")

source = "img.jpg"
destination = "newImage.jpg"

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

new_width = int(input("Enter width of new image: "))
new_height = int(input("Enter height of new image: "))

# resize image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)
