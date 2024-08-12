
# Super Resolution Hazard Map for Lunar Lander Navigation

This project aims to generate hazard maps at 1m grid spacing using 5m spatial resolution data for safely navigating a lunar lander to a safe landing site. The challenge involves the use of super-resolution techniques to enhance TMC (Terrain Mapping Camera) images from 5m resolution to identify hazards such as slopes, craters, boulders, and shadows that could affect the landing.

## Problem Statement

The Terrain Mapping Camera (TMC) on board the lunar orbiter has imaged nearly 80% of the Moon's surface at a resolution of 5m. However, higher resolution data from the OHRC (Orbiter High-Resolution Camera) is only available for limited regions at 25cm resolution. Due to this limited coverage, it is not feasible to land at any arbitrary location on the Moon's surface. 

The problem involves creating hazard maps using super-resolution techniques on TMC 5m images while considering hazard definitions like:
- Slope: > 10 degrees
- Crater/Boulder Depth/Height: > 1m
- Crater Distribution
- Shadows

This project also demonstrates the techniques used to navigate a lunar lander safely in near real-time using the generated hazard maps.

## Features

- **Super-Resolution Enhancement**: Uses machine learning models to enhance the resolution of 5m TMC images to 1m grid spacing.
- **Hazard Detection**: Identification of critical hazards like slopes, craters, boulders, and shadows on the lunar surface.
- **Real-Time Lander Navigation**: Simulation of real-time navigation for safe lunar lander touchdown using the generated hazard maps.
- **Data Integration**: Combining data from different lunar missions (TMC and OHRC) for comprehensive lunar surface analysis.

## Technologies Used

- **Python**: For data processing, model training, and hazard map generation.
- **TensorFlow/PyTorch**: For implementing super-resolution techniques.
- **Geospatial Libraries**: Such as GDAL and Rasterio for image processing.
- **Matplotlib/Seaborn**: For visualizing the lunar surface and hazard maps.

## Results

The project successfully generates high-resolution hazard maps using 5m TMC images, allowing for safe navigation of a lunar lander. The maps highlight critical hazards on the lunar surface, ensuring a safe and accurate landing.

This project was undertaken as part of the **SIH 2023** challenge under Problem Statement Code **PS1519**. Special thanks to all team members and mentors who contributed to the success of this project.

