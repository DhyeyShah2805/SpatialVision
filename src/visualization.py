import matplotlib.pyplot as plt
import numpy as np

def visualize_scene(points_3d, camera_pose):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = points_3d[:, 0]
    y = points_3d[:, 1]
    z = points_3d[:, 2]

    ax.scatter(x, y, z, s=2)

    cam = camera_pose["position"]
    ax.scatter(cam[0], cam[1], cam[2], s=100)

    ax.set_title("3D Reconstruction & Camera Pose")

    plt.savefig("results/point_cloud.png")
    plt.show()