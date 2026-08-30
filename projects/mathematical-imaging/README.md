# Artificial Painting Toolbox

A MATLAB-based image processing project that explores how mathematical and computational techniques can be used to transform photographs into different artistic styles.

**You can find the project writeup PDF in this repo. Visit our drive for code implementation files in PDF: https://drive.google.com/drive/folders/1CBeuyZd3X2Oc---hu0VKI8YonJtwGk11**

## Overview

This project investigates the use of classical image processing techniques to generate five artificial painting effects:

- Pencil Sketch
- Comic
- Oil Painting
- Van Gogh's Stroke Style
- Cubism

The project combines edge detection, filtering, histogram analysis, gradient orientation, image blending, triangulation, and color manipulation to create visually distinct artistic effects from ordinary photographs.

## My Contribution

I primarily developed and analyzed the **Oil Painting Effect**, with additional contributions to the initial setup and evaluation of the **Van Gogh's Stroke Style**. 

### Oil Painting Effect

I implemented an efficient histogram-based algorithm to generate localized brush-stroke patterns while preserving the major visual features of the input image.

The algorithm works by:

1. Defining a local neighborhood around each pixel
2. Computing RGB histograms within each neighborhood
3. Identifying the most frequently occurring pixel values
4. Replacing pixels in the neighborhood with the dominant values
5. Repeating this process across the image to produce a stroke-like texture

This approach creates an oil-painting effect using relatively simple image processing operations without computationally intensive optimization.

### Van Gogh's Stroke Style

I also contributed to the initial development and evaluation of the Van Gogh-inspired stroke effect.

The approach extends the oil painting effect by incorporating **gradient orientation** to determine the direction of artificial brush strokes. Stroke segments are generated according to local image gradients and subsequently smoothed and blended with the original image.

This approach helps address some limitations of the basic oil painting algorithm, particularly its performance around sharp edges and uniform regions.

## Technical Approach

### Oil Painting

**Key techniques:**

- RGB histogram calculation
- Local neighborhood processing
- Dominant pixel selection
- Image manipulation
- Stroke-like texture generation

The oil painting algorithm is lightweight and computationally efficient, while producing visually recognizable painting-like textures.

### Van Gogh Stroke Effect

**Key techniques:**

- Gradient orientation
- Image resizing and grayscale conversion
- Gradient-based stroke generation
- Line segment generation
- Box-kernel smoothing
- Image blending
- Contrast and saturation adjustment

Gradient orientation was used to align artificial strokes with the dominant local directions of the image, producing a more structured brush-stroke appearance.

## Other Effects

The complete toolbox also includes three additional image processing effects developed by other team members:

- **Pencil Sketch:** Laplacian edge detection, color inversion, and contrast stretching
- **Comic:** Bilateral filtering, Sobel edge detection, and color adjustment
- **Cubism:** Gaussian smoothing, Sobel edge detection, Delaunay triangulation, and color mapping

Together, these methods demonstrate how different combinations of fundamental image processing techniques can produce substantially different artistic styles.

## Technologies

**Programming:** MATLAB

**Image Processing:** Edge Detection, Histogram Analysis, Bilateral Filtering, Gaussian Filtering, Gradient Orientation

**Mathematical Techniques:** Convolution, Local Feature Analysis, Image Blending, Delaunay Triangulation

## Results

The oil painting algorithm successfully generated stroke-like patterns from a variety of input images. However, the basic approach has limitations around sharp edges and uniform-color regions.

The Van Gogh-inspired extension improved the visual quality by incorporating gradient-based stroke directions and smoothing, producing more structured and continuous brush strokes.

The complete toolbox demonstrates the versatility of classical image processing techniques for computational art and visual transformation.

## Team

- **Dakota Lin** — Oil Painting Effect; initial setup and evaluation of Van Gogh's Stroke Style
- **Sherry Zhou** — Pencil Sketch and Comic Effects
- **Martin Zhang** — Development of Van Gogh's Stroke Style
- **Brandon Vuong** — Cubism-like Effect

## Report

[📄 Download the Full Report (PDF)](./Artificial_Painting_Toolbox.pdf)

> For the best viewing experience, please download the PDF.
