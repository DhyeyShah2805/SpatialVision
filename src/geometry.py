import cv2
import numpy as np

def estimate_pose(matches):
    pts1, pts2 = matches

    F, mask = cv2.findFundamentalMat(pts1, pts2, cv2.FM_RANSAC)

    focal_length = 1.0
    cx, cy = 0.0, 0.0

    K = np.array([
        [focal_length, 0, cx],
        [0, focal_length, cy],
        [0, 0, 1]
    ])

    E = K.T @ F @ K

    _, R, t, _ = cv2.recoverPose(E, pts1, pts2, K)

    return R, t