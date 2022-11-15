# Processing & analysis

When working with images, two related concepts frequently arise: **image processing** and **image analysis**.
They may be defined as follows:

- **Image processing** takes an *image as input* and gives *another image as output* <br />
  e.g. an image with features enhanced or suppressed, a binary image
- **Image analysis** takes an *image as input* and gives *measurements as output* <br />
  e.g. a stained area value, or number of positive cells

The distinction between processing and analysis is helpful to understand how QuPath works, and how its focus differs from some other open source applications.

## Image processing

*Image processing* transforms images by applying mathematical operations to the pixel values.

Often these operations are very simple (e.g. averaging neighboring pixels), but because images can be huge - perhaps consisting of *billions* of pixels - even simple operations can be extremely powerful when applied across the whole image.

:::{figure} images/image_processing.png
:align: center
:width: 90%

Example of processed images, using local averages, differences and gradient magnitude.
:::

:::{tip}
See [Processing fundamentals] for an overview of image processing principles and techniques.
:::

## Image analysis

*Image analysis* is oriented towards extracting some knowledge from the image.
This knowledge isn't represented in terms of pixels, and might rather be a table.

:::{figure} images/image_analysis.png
:align: center
:width: 90%

Example of image analysis, where image processing helps along the way.
:::

## Where QuPath fits in

**QuPath is designed primarily for image analysis**.

Although it *uses* image processing, this is generally wrapped up inside specific commands, e.g. for *Cell detection* or *TMA dearraying*.
These commands can be used to generate objects, which can then be queried and summarized as described {doc}`in the next section <objects>`.

:::{figure} images/qupath_approach.png
:align: center
:width: 90%

General workflow for analyzing images in QuPath.
:::

This means that, for the most part, it is not necessary to have detailed knowledge of image processing to use the software (but it can help!).
Rather, users of the software are often specialists in other areas, who, after learning the basics of how QuPath works, can focus on how they apply it and how to interpret the results.

:::{admonition} QuPath for algorithm developers
QuPath is created and maintained by researchers whose focus is on developing the image processing algorithms and other computational methods that make the analysis possible - so that those who use the software can focus on analyzing their data and interpreting the results.

However, because it's open source, scriptable and extensible, QuPath also provides a platform that can help *other* computationally-minded researchers to develop and share new algorithms in a user-friendly way.
It is hoped this can save both algorithm users and algorithm developers time, while making image analysis more accessible and reproducible to everyone.
:::

[processing fundamentals]: https://petebankhead.gitbooks.io/imagej-intro/content/chapters/processing_and_analysis/processing_and_analysis.html
