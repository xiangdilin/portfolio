# Artificial Painting Toolbox

A project exploring multiple algorithms based on image processing techniques to generate artificial painting-style effects using MATLAB and Mathematica.

## Overview

Artistic creations are generally difficult to mimic or duplicate digitally. However, a close observation of the features that critically build an artificial painting provided us with inspiration for developing painting-like effects to apply to existing images. We aimed to test and evaluate the feasibility of our artificial painting toolbox in a general case.

The project focused on generating five unique artistic touches: pencil sketch, comic, oil painting, the Van Gogh style, and the Cubism-like effect.

## Methods

Our team explored several mathematical and computational approaches:

### Smoothing and Edge Detection
* **Pencil Sketch Effect:** Achieved by applying a 6x6 8-connected Laplacian kernel for edge detection, followed by color inversion and contrast stretching.
* **Comic-Like Effect:** Used a bilateral filter to blur images while preserving edges, a Sobel operator for outlining, and enhanced color saturation.

### Oil Painting and Van Gogh Styles
* **Oil Painting Effect:** Relies on histogram calculation within an a x b neighborhood to replace pixels with the most frequently occurring value, unifying the region to look like a stroke.
* **Van Gogh's Stroke Style:** Utilizes gradient orientation filters to generate line segments, and square box kernels to smooth unconnected line segments to mimic spiral brushstrokes.

### Cubism-Like Effect
* **Triangulation:** Applied a Delaunay triangulation algorithm to edges found via a Sobel operator to form non-intersecting triangles.
* **Coloring:** Mapped the original image colors at the centroid of each generated triangle to color it in.

## My Contributions

* Explored and developed algorithms for the **Oil Painting** and **Van Gogh stroke** effects
* Implemented the **Oil Painting Effect** by calculating the histogram of R, G, and B values within a chosen a x b neighborhood and assigning the maximum pixel value to the region to create a uniform stroke-like pattern.
* Identified limitations in handling sharp edges in the oil painting algorithm and researched improvements, leading to the initial setup and evaluation of the **Van Gogh's stroke effect**.
* Handled gradient orientation maps (calculating the orientation angle theta = arctan(-Gx/Gy)) and applied a square box kernel to smooth unconnected line segments.

## Technologies & Results

* **Programming:** MATLAB, Wolfram Mathematica
* **Mathematical Methods:** Bilateral filtering, gradient filters, Euclidean norms, Delaunay triangulation, histogram calculation

The algorithms performed well across various generic photographs, demonstrating the immense potential and versatility of digital image processing techniques in creating diverse artistic styles.
