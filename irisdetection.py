import sys
import cv2
import numpy as np
from scipy.interpolate import interp1d
from PIL import Image

imagepath = str(sys.argv[1])

original_eye = np.asarray(Image.open(imagepath))
eye_image = cv2.cvtColor(original_eye, cv2.COLOR_RGB2GRAY)


eye_circles = cv2.HoughCircles(eye_image, cv2.HOUGH_GRADIENT, 2, 100,  minRadius = 90, maxRadius = 200)

if eye_circles is not None:
    circle = eye_circles[0][0]
    iris_coordinates = (circle[0], circle[1])

if iris_coordinates is not None:
    x = int(iris_coordinates[0])
    y = int(iris_coordinates[1])

    w = int(round(circle[2]) + 10)
    h = int(round(circle[2]) + 10)

    #cv2.circle(original_eye, iris_coordinates, int(circle[2]), (255,0,0), thickness=2)
    iris_image = original_eye[y-h:y+h,x-w:x+w]
    iris_image_to_show = cv2.resize(iris_image, (iris_image.shape[1]*2, iris_image.shape[0]*2))

q = np.arange(0.00, np.pi*2, 0.01) #theta
inn = np.arange(0, int(iris_image_to_show.shape[0]/2), 1) #radius

cartisian_image = np.empty(shape = [inn.size, int(iris_image_to_show.shape[1]), 3])
m = interp1d([np.pi*2, 0],[0,iris_image_to_show.shape[1]])

for r in inn:
    for t in q:
        polarX = int((r * np.cos(t)) + iris_image_to_show.shape[1]/2)
        polarY = int((r * np.sin(t)) + iris_image_to_show.shape[0]/2)
        cartisian_image[r][int(m(t) - 1)] = iris_image_to_show[polarY][polarX]

im = Image.fromarray(iris_image_to_show)
im.save('eye.jpeg')
cartisian_image = cartisian_image.astype('uint8')
im = Image.fromarray(cartisian_image)
im.save('cartesian_eye.jpeg')
