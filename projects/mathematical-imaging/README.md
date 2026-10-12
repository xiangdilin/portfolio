# Artificial Painting Toolbox

A MATLAB-based image processing project that explores how mathematical and computational techniques can be used to transform photographs into different artistic styles.

**You can find the project code and the project writeup PDF in this repo through either the navigation sidebar or the links at the end of this README.**

## Overview

Classical image processing offers a rich set of tools for modifying and analyzing images, but it is not always obvious how they can be combined to imitate traditional artistic media. This project investigates how fundamental techniques, without any deep learning or neural style transfer, can be used to generate five artificial painting effects:

- Pencil Sketch
- Comic
- Oil Painting
- Van Gogh's Stroke Style
- Cubism

The toolbox combines edge detection, filtering, histogram analysis, gradient orientation, image blending, triangulation, and color manipulation to create visually distinct artistic effects from ordinary photographs.

## Project Goals

- Reproduce the visual characteristics of traditional artistic media using **classical image processing** techniques.
- Develop an **efficient, lightweight oil painting algorithm** that generates brush-like textures while preserving the major features of the input image.
- Extend the oil painting effect with **gradient-based stroke directions** to better imitate a Van Gogh-style painting.
- Compare how different combinations of **fundamental image processing operations** produce substantially different artistic styles.

## Methods

1. **Oil Painting**
   - Defined a local neighborhood around each pixel and computed **RGB histograms** within each neighborhood.
   - Identified the most frequently occurring pixel values and used them to replace pixels in the neighborhood.
   - Repeated this process across the image to produce a stroke-like texture.

2. **Van Gogh's Stroke Style**
   - Extended the oil painting effect using **gradient orientation** to determine the direction of artificial brush strokes.
   - Generated line segments along local image gradients, then applied **box-kernel smoothing** and blended the result with the original image.
   - Adjusted contrast and saturation to finish the effect.

3. **Pencil Sketch** *(team member)*
   - Laplacian edge detection, color inversion, and contrast stretching.

4. **Comic** *(team member)*
   - Bilateral filtering, Sobel edge detection, and color adjustment.

5. **Cubism** *(team member)*
   - Gaussian smoothing, Sobel edge detection, Delaunay triangulation, and color mapping.

## Key Findings

- **Oil Painting:** The histogram-based algorithm is lightweight and computationally efficient while producing visually recognizable painting-like textures, without computationally intensive optimization.
- **Limitations:** The basic oil painting approach performs poorly around sharp edges and uniform-color regions.
- **Van Gogh Extension:** Incorporating gradient-based stroke directions and smoothing produced more structured and continuous brush strokes, addressing some of the limitations of the basic algorithm.
- **Versatility:** Different combinations of fundamental image processing techniques can produce substantially different artistic styles.

## My Contributions

- Implemented and analyzed the **oil painting effect**, including the efficient histogram-based stroke-generation algorithm
- Used local RGB histograms to identify dominant colors and generate brush-like regions
- Investigated improvements to reduce artifacts around sharp edges and uniform regions
- Contributed to the initial development and evaluation of the **Van Gogh-inspired stroke effect**

## Technologies & Methods

**Programming:** MATLAB, Mathematica

**Image Processing:** Edge Detection, Histogram Analysis, Bilateral Filtering, Gaussian Filtering, Gradient Orientation

**Mathematical Techniques:** Convolution, Local Feature Analysis, Image Blending, Delaunay Triangulation

## Results

The oil painting algorithm successfully generated stroke-like patterns from a variety of input images, though the basic approach showed limitations around sharp edges and uniform-color regions. The Van Gogh-inspired extension improved visual quality by incorporating gradient-based stroke directions and smoothing, producing more structured and continuous brush strokes.

Together with the pencil sketch, comic, and Cubism effects developed by other team members, the complete toolbox demonstrates the versatility of classical image processing techniques for computational art and visual transformation.

## Contributors

- **Dakota Lin:** Oil Painting Effect; initial setup and evaluation of Van Gogh's Stroke Style
- **Brandon Vuong:** Cubism-like Effect
- **Martin Zhang:** Development of Van Gogh's Stroke Style
- **Sherry Zhou:** Pencil Sketch and Comic Effects

> Listed in alphabetical order by last name.

## Code

[💻 Browse the Code Files](./code_files)

> The `code_files` folder contains the code implementation files for the toolbox.

## Report

[📄 Download the Full Report (PDF)](./Artificial_Painting_Toolbox.pdf)

> For the best viewing experience, please download the PDF.

## License

This project is licensed under the MIT License.
