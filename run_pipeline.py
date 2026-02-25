from src.feature_matching import match_features
from src.geometry import estimate_pose
from src.triangulation import reconstruct_points
from src.localization import localize_query
from src.visualization import visualize_scene

def main():
    print("Running SpatialVision pipeline...")

    matches = match_features()
    R, t = estimate_pose(matches)
    points_3d = reconstruct_points(matches, R, t)
    camera_pose = localize_query(points_3d)

    visualize_scene(points_3d, camera_pose)

    print("Pipeline completed. Results saved in /results")

if __name__ == "__main__":
    main()