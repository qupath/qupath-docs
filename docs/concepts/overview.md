# Overview

Here's an overview of the general concepts in QuPath:

- Your images may (and probably should) be organized in a `Project`

  > - Each image in the project is represented by a `ProjectImageEntry`
  >
  > - When you open a `ProjectImageEntry`, you get an `ImageData` displayed in the viewer
  >
  >   - The `ImageData` stores a few things, including:
  >
  >     - The `ImageType` (e.g. Brightfield, Fluorescence)
  >
  >     - Any `ColorDeconvolutionStains` required (if brightfield)
  >
  >     - An `ImageServer`, for accessing pixels and metadata
  >
  >     - A `PathObjectHierarchy`, containing `PathObjects` in a tree-like structure
  >
  >       - Each `PathObject` contains a `ROI` and a `MeasurementList`

When you analyze an image in QuPath, you take your `ImageData`, access pixels from the `ImageServer` and try to represent what the image contains in the `PathObjectHierarchy`.

Then you query the object hierarchy to extract some kind of summary measurements.
