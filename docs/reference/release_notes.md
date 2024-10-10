# Release Notes v0.6.0

Welcome to the expanded release notes for QuPath v0.6.0. This version was released on 2024- ***TODO***. The hopes of this document are to provide a more detailed overview of the changes in this version than the original github [release notes](https://github.com/qupath/qupath/blob/main/CHANGELOG.md).

1. [Major features](#major-features) - Spotlight changes
2. [Enhancements](#enhancements) - Additions to make existing features better
3. [Experimental features](#experimental-features) -  New features included for testing and feedback. They may change or be removed in future versions.
4. [Bugs fixed](#bugs-fixed) - Previous problems that have been resolved
5. [Scripting and API changes](#scripting-and-api-changes) - Changes related to the API and anything script related. Useful notes for script writers and extension developers!
6. [Dependency updates](#dependency-updates) - External libraries and package updates

## 🚀 Major features

### New InstanSeg Segmentation

In this new version we have added support for the exciting new segmentation extension [InstanSeg](https://github.com/qupath/qupath-extension-instanseg). This extension provides speedy and accurate segmentation of cells for both brightfield and fluorescent images. Learn more about InstanSeg and how to use it in QuPath [here](../deep/instanseg.md).

:::{figure} https://global.discourse-cdn.com/business4/uploads/imagej/optimized/3X/0/0/0047d91a99114d47e9a22e68c04eacd9e1cd24a5_2_690x392.jpeg
:class: shadow-image full-image

InstanSeg segmentation of haematoxylin and dab nuclei
:::

:::{figure} https://global.discourse-cdn.com/business4/uploads/imagej/optimized/3X/a/9/a970374cfd08ec4708364ca5b42807ceaaa24133_2_690x392.jpeg
:class: shadow-image full-image

InstanSeg segmentation of nuclei in a fluorescent image
:::

***TODO*** Update images once InstanSeg page is complete (since images have been compressed)

### OME-Zarr images are now supported

Its now possible to open and work with OME-Zarr images in QuPath. This is a new format that is designed to be more efficient and scalable than the traditional OME-TIFF format. Learn more about OME-Zarr in general check out [this paper](https://link.springer.com/article/10.1007/s00418-023-02209-1) and how to use it in QuPath [here](../reference/ome_zarr.md).

## ✨ Enhancements

### New keyboard shortcuts

* **Tired of using the mouse to close sub-windows?** Now you can use the escape key or ctrl/cmd + W to close them! (well most of them... we're working on the less frequently used ones).
* **Got lots of things to select?** Quickly activate the selection tool by pressing 'S' when the main viewer is selected.

### Viewing Annotation Names

Previously when displaying annotation names the label would be displayed in the center of the annotation. This could be problematic when the annotation was small or overlapped with another. Now the label is displayed consistently at the top of the annotation. This makes it easier to see which label relates to which annotation as seen below.

:::{figure} https://github.com/user-attachments/assets/f180d900-f6de-4230-a7b7-fe054b70108e
:class: shadow-image full-image

Annotation names displayed at the top of the annotation
:::

### Project Browser Improvements

* **Thumbnails can now be hidden**: This is useful when you have a large number of images in a project and don't want to wait for the thumbnails to load or for double blinded studies where comparisons between thumbnails could be problematic. In addition to this, the size of the thumbnail can be adjusted to suit your needs by simply right clicking on the thumbnail and selecting an option in "thumbnail size".
* **Alerts when images go missing**: Previously if an image was moved or deleted from the project folder, QuPath would not alert the user that the image was missing until the image was opened. Now, if an image is missing from the project folder, a warning will be displayed next to the name in the project browser so no more surprises when opening.
* **Sorted our sorting**: The sorting of images in projects has been sharpened up. Images will remain sorted when re-opening the project or after adding new metadata values.

### Selection mode refresh

Allongside a shiny new icon design, tool buttons will now change when the selection mode is selected to make it easier to see which mode is currently active.
If the current tool options that work with selection mode are not enough it's now possible to use the line tool too with any object that the line intercepts being selected.
Lastly, the selection mode can now be quickly accessed by using the 'S' key when the main viewer is selected.

### Histograms now use Logarithmic scaling

When viewing histograms in QuPath, the scaling can now be using log$_{10}$ rather than natural log. Measurement tables for annotations and detections are both now able to utilize this feature.

***TODO***: Add images of log scaling once general doc update is complete

### Classy TMAs

TMA cores now by default are assigned a specific class when created, keeping them further distinguished from other annotations types. The default color for this class is now lighter to make it easier to see for both brightfield and fluorescent images. If a core is missing from the grid then it will be displayed the same color as the other cores but with more transparency.

***TODO***: Add image of TMA once TMA page is complete

### Classification color warnings

Changing the color of your annotations can get tricky when your needing more colors than are in the color palette. Now when you select a color very similar to one already used, QuPath will warn you and suggest a new color to use.

***TODO***: Add image of color warning and check full functionality

### Package project warnings removed

When using self contained projects with all your images in beside the project file, QuPath would previously prompt users to update the image paths if the project was moved. This is no longer the case so enjoy taking your projects to new locations!

### RGB fluorescence images

Previously an RGB fluorescence image would be stuck with the default "red", "green" and "blue" channels. Now you can change these to any name you like.

### Symbolic Links Support

Symlinks (short for symbolic links) are special types of files in an operating system that act as references or pointers to other files or directories. They are often used to create shortcuts or aliases to another file or folder without duplicating the actual data. QuPath now supports SymLinks for images giving users more flexibility with image organization.

### Bio-Formats default preferences

Due to some troubles with opening remote OME-Zarr images, bioformats default is set to "local files only" within preferences.

## 🔥 Experimental features

### Stain normalization and background subtraction

The foundations for stain normalization and background subtraction have been started. Currently they are only accessible via the scripting and not yet available to interface only users (but watch this space!).

```{image} https://github.com/user-attachments/assets/84b18c6c-260e-47d7-acf2-9ee97d9c3c76
:width: 48%
```

```{image} https://github.com/user-attachments/assets/ecd1d6a7-9b49-4a93-b635-2298d43abf09
:width: 48%
```

:::{Figure} https://github.com/user-attachments/assets/12d7060b-35bc-40ca-89a3-f837c5417dbf
:class: mid-image

Top Left: Original image, Top Right: Image after background subtraction, Bottom: Image after stain normalization and background subtraction.
:::

## 🐛 Bugs fixed

### Script saving on close

Users will be prompted to save unsaved changes to scripts when closing QuPath, even when the scripting editor is minimized so your precious code is safe.

### OME.tiff exporting 8 bit
When using the Tile exporter to export an OME.tiff image, the image previously went through a RGB check that resulted in the images wrongly being converted to 8-bit. It now exports in the correct bit depth of the original image.

## 👩‍💻 Scripting and API changes

### Faster running scripts for projects

When images are not needed in a script (for example exporting measurements) it will run faster. This is due to the image pixels are no longer fetched regardless if they are used or not.

## 📚 Dependency updates

* Bio-Formats 7.3.1
* Commonmark 0.23.0
* DeepJavaLibrary 0.30.0
* Groovy 4.0.22
* Gson 2.11.0
* Guava 33.3.1-jre
* JavaFX 23
* Java Topology Suite 1.20.0
* JFreeSVG 5.0.6
* JNA 5.14.0
* JUnit 5.11.0
* Logback 1.5.8
* Picocli 4.7.6
* OpenCV 4.9.0
* OpenJDK 21
* RichTextFX 0.11.3
* slf4j 2.0.16
* snakeyaml 2.3
