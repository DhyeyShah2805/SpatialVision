import numpy as np
import cv2

def reconstruct_points(matches, R, t):
    pts1, pts2 = matches

    proj1 = np.hstack((np.eye(3), np.zeros((3,1))))
    proj2 = np.hstack((R, t))

    pts1 = pts1.T
    pts2 = pts2.T

    points_4d = cv2.triangulatePoints(proj1, proj2, pts1, pts2)
    points_3d = points_4d[:3] / points_4d[3]

    return points_3d.T