# SpatialVision — 3D Reconstruction & Visual Localization

This project implements a spatial perception pipeline that reconstructs a 3D scene from multiple images and estimates the camera pose of unseen query images.

The system demonstrates core components of visual positioning and mapping used in real-world spatial AI systems.

## Key Capabilities
- Multi-view 3D reconstruction using feature matching and triangulation
- Camera pose estimation using epipolar geometry
- Sparse spatial point cloud generation
- Visual localization of query images
- 3D visualization of scene structure and camera trajectory

## Pipeline Overview
1. Detect and match image features
2. Estimate camera geometry between views
3. Triangulate 3D points
4. Build spatial map
5. Localize new query image in reconstructed scene

## Tech Stack
Python, OpenCV, NumPy, Open3D

## How to Run
```bash
pip install -r requirements.txt
python run_pipeline.py
