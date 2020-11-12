# Edge Detection

## Objective

The purpose of this paper is to include details on edge detection in image processing. We're going to look at what edges are, why we need to remove edges, and how we can do it using different methods.

## What are edges?

Type of edges:

- Horizontal edges
- Vertical edges
- Diagonal edges

## Why detecting edges

For several reasons: 

The main idea of why we detect edges is to catch the most interesting events or modifications in an image. Since edges are more compact than pixels, we use them to distinguish objects, fit images or analyze images, and so on.

## How to detect edges

Edges come from:

- Surface normal discontinuity
- Depth discontinuity
- Surface color discontinuity
- Illumination discontinuity
 
We can produce a sub-image by applying edge detectors containing a series of related curves showing the borders of the objects, hence the key events in an image . In addition, we can also decrease the amount of redundant data to be processed and filter out any information that is unrelated to the operation. 

Still, there are many variables in an image which makes getting the ideal edges a complicated process. Many methods are available for extraction, each with their own pros and cons

### 1. Image gradient
Image gradient is nothing but directional shifts in images' intensity. This method can help us detect the edge by measuring the gradient in a small image region and then repeating the procedure over and over again. The gradient of an image can be interpreted as a function:

![ImageGradient](imagegradient.png)

Edge strength:

$$ || \triangledown f || = \sqrt{(\frac{\partial f}{\partial x})^2 + (\frac{\partial f}{\partial y})^2 } $$

The arrows indicate the most rapid increase in intensity. 

Angle calculation:

$$ \space \theta = tan^{-1} * (\frac{\partial f}{\partial x} / \frac{\partial f}{\partial y})  $$


Each estimation is performed in a small area of the image and once all regions have been calculated, we need to keep replicating this procedure. Variations have been produced on the basis of this approach to increase the efficacy of detections, minimizing the amount of workloads.


### 2.Sobel operator

One of the most common used operator is the Sober operator, invented by Irwin Sobel andGary Feldman, it uses two 3x3 matrix kernel each for x and y direction to calculate theapproximation of the derivative of an image