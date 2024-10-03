# Release Notes v0.6.0

Welcome to the expanded release notes for QuPath v0.6.0. This version was released on 2024-**-**. The hopes of this document are to provide a more detailed overview of the changes in this version than the original github [release notes](https://github.com/qupath/qupath/blob/main/CHANGELOG.md).

1. [Major features](../reference/release_notes.html#major-features) - Spotlight changes
2. [Enhancements](../reference/release_notes.html#enhancements) - Additions to make existing features better
3. [Experimental features](../reference/release_notes.html#experimental-featuress) -  New features included for testing and feedback. They may change or be removed in future versions.
4. [Bugs fixed](../reference/release_notes.html#experimental-features) - Previous problems that have been resolved
5. [API changes](../reference/release_notes.html#api-changess) - Scripting changes
6. [Dependency updates](../reference/release_notes.html#dependency-updates) - External libraries and package updates

## Major features
### New InstanSeg Segmentation
In this new version we have added support for the exciting new segmentation extension [InstanSeg](https://github.com/qupath/qupath-extension-instanseg). This extension provides speedy and accurate segmentation of cells for both brightfield and fluorescent images. Learn more about InstanSeg and how to use it in QuPath [here](../deep/instanseg.md).

:::{figure} images/release_notes_CMU-2_InstanSeg.png
:class: shadow-image

InstanSeg segmentation of H&E nuclei
:::

:::{figure} images/release_notes_LuCa_InstanSeg.png
:class: shadow-image

InstanSeg segmentation of nuclei in a fluorescent image
:::

### OME-Zarr images are now supported
Its now possible to open and work with OME-Zarr images in QuPath. This is a new format that is designed to be more efficient and scalable than the traditional OME-TIFF format. Learn more about OME-Zarr in general check out [this paper](https://link.springer.com/article/10.1007/s00418-023-02209-1) and how to use it in QuPath [here](../reference/ome_zarr.md).

## Enhancements

### Viewing Annotation Names
Previously when displaying annotation names the label would be displayed in the center of the annotation. This could be problematic when the annotation was small or annotations overlapped. Now the label is displayed at the top of the annotation. This makes it easier to see which label relates to which annotation as seen below.

:::{figure} images/release_notes_annotation_names.png
:class: shadow-image

InstanSeg segmentation of nuclei in a fluorescent image
:::

### Project Browser Improvements
* **Thumbnails can now be hidden**: This is useful when you have a large number of images in a project and don't want to wait for the thumbnails to load or for double blinded studies where comparisons between thumbnails could be problematic. In addition to this, the size of the thumbnail can be adjusted to suit your needs by simply right clicking on the thumbnail and selecting an option in "thumbnail size".

* **Alerts when images go missing**: Previously if an image was moved or deleted from the project folder, QuPath would not alert the user that the image was missing until the image was opened. Now, if an image is missing from the project folder, a warning will be displayed next to the name in the project browser so no more surprises when opening.

## Experimental features

## Bugs fixed

## API changes

## Dependency updates