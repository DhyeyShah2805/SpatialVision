import cv2
import numpy as np
import os

IMAGE_DIR = "data/sample_images"

def load_images():
    images = []
    for file in sorted(os.listdir(IMAGE_DIR)):
        path = os.path.join(IMAGE_DIR, file)
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            images.append(img)
    return images

def match_features():
    images = load_images()
    if len(images) < 2:
        raise ValueError("Need at least two images")

    orb = cv2.ORB_create(2000)

    kp1, des1 = orb.detectAndCompute(images[0], None)
    kp2, des2 = orb.detectAndCompute(images[1], None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    pts1 = np.float32([kp1[m.queryIdx].pt for m in matches])
    pts2 = np.float32([kp2[m.trainIdx].pt for m in matches])

    return pts1, pts2