# Release Notes v0.6.0

Welcome to the expanded release notes for QuPath v0.6.0. This version was released on 2024-**-**. The hopes of this document are to provide a more detailed overview of the changes in this version than the original github [release notes](https://github.com/qupath/qupath/blob/main/CHANGELOG.md).

1. [Major features](../reference/release_notes.html#major-features) - Spotlight changes
2. [Enhancements](../reference/release_notes.html#enhancements) - Additions to make existing features better
3. [Experimental features](../reference/release_notes.html#experimental-featuress) -  New features included for testing and feedback. They may change or be removed in future versions.
4. [Bugs fixed](../reference/release_notes.html#bug-fixed) - Previous problems that have been resolved
5. [Scripting changes](../reference/release_notes.html#api-changess) - Changes related to the API and anything script related
6. [Dependency updates](../reference/release_notes.html#dependency-updates) - External libraries and package updates

## 🚀 Major features

### New InstanSeg Segmentation

In this new version we have added support for the exciting new segmentation extension [InstanSeg](https://github.com/qupath/qupath-extension-instanseg). This extension provides speedy and accurate segmentation of cells for both brightfield and fluorescent images. Learn more about InstanSeg and how to use it in QuPath [here](../deep/instanseg.md).

:::{figure} https://global.discourse-cdn.com/business4/uploads/imagej/optimized/3X/0/0/0047d91a99114d47e9a22e68c04eacd9e1cd24a5_2_690x392.jpeg
:class: shadow-image

InstanSeg segmentation of haematoxylin and dab nuclei
:::

:::{figure} https://global.discourse-cdn.com/business4/uploads/imagej/optimized/3X/a/9/a970374cfd08ec4708364ca5b42807ceaaa24133_2_690x392.jpeg
:class: shadow-image

InstanSeg segmentation of nuclei in a fluorescent image
:::

### OME-Zarr images are now supported

Its now possible to open and work with OME-Zarr images in QuPath. This is a new format that is designed to be more efficient and scalable than the traditional OME-TIFF format. Learn more about OME-Zarr in general check out [this paper](https://link.springer.com/article/10.1007/s00418-023-02209-1) and how to use it in QuPath [here](../reference/ome_zarr.md).

## ✨ Enhancements

### New keyboard shortcuts

* **Tired of using the mouse to close sub-windows?** Now you can use the escape key or ctrl/cmd + W to close them! (well most of them... we're working on the less frequently used ones).
* **Got lots of things to select?** Quickly activate the selection tool by pressing 'S' when the main viewer is selected.

### Viewing Annotation Names

Previously when displaying annotation names the label would be displayed in the center of the annotation. This could be problematic when the annotation was small or overlapped with another. Now the label is displayed consistently at the top of the annotation. This makes it easier to see which label relates to which annotation as seen below.

:::{figure} : https://github.com/user-attachments/assets/f180d900-f6de-4230-a7b7-fe054b70108e
:class: shadow-image

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

***TODO***: Confirm replication steps and insert image of histogram

### Classy TMAs

TMA cores now by default are assigned a specific class when created, keeping them further distinguished from other annotations types. The default color for this class is now lighter to make it easier to see for both brightfield and fluorescent images. If a core is missing from the grid then it will be displayed the same color as the other cores but with more transparency.

***TODO***: Add image of TMA updated cores once image confirmed

### Classification color warnings

Changing the color of your annotations can get tricky when your needing more colors than are in the color pallete. Now when you slelct a color very similar to one already used, QuPath will warn you and suggest a new color to use.

***TODO***: Add image of color warning and check full functionality

### Package project warnings removed

When using self contained projects with all your images in beside the project file, QuPath would previously prompt users to update the image paths if the project was moved. This is no longer the case so enjoy taking your projects to new locations!

### RGB fluorescence images

Previously an RGB fluorescence image would be stuck with the default "red", "green" and "blue" channels. Now you can change these to any name you like.

### Symbolic Links Support

Symlinks (short for symbolic links) are special types of files in an operating system that act as references or pointers to other files or directories. They are often used to create shortcuts or aliases to another file or folder without duplicating the actual data. QuPath now supports SymLinks for images giving users more flexibility with image organisation.

### Bio-Formats defualt preferences

Due to some troubles with opening remote OME-Zarr images, bioformats default is set to "local files only" within preferences.

## 🔥 Experimental features

### Stain normalization and background subtraction

The foundations for stain normalization and background subtraction have been startd. Currently they are only accessible via the scripting and not yet available to interface only users (but watch this sapce!).

***TODO***: Fix in-line example images

![Image 1](https://github.com/user-attachments/assets/84b18c6c-260e-47d7-acf2-9ee97d9c3c76) ![Image 2](https://github.com/user-attachments/assets/ecd1d6a7-9b49-4a93-b635-2298d43abf09) ![Image 3](https://github.com/user-attachments/assets/12d7060b-35bc-40ca-89a3-f837c5417dbf)

```{image} {https://private-user-images.githubusercontent.com/4690904/345100501-84b18c6c-260e-47d7-acf2-9ee97d9c3c76.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjgyNDkxNTYsIm5iZiI6MTcyODI0ODg1NiwicGF0aCI6Ii80NjkwOTA0LzM0NTEwMDUwMS04NGIxOGM2Yy0yNjBlLTQ3ZDctYWNmMi05ZWU5N2Q5YzNjNzYucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI0MTAwNiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNDEwMDZUMjEwNzM2WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YzYzNTM3MDAxYzM0MTNjMmE0YmZlNWRkYTA1NWNmZWVjZDMyZTA3YzhjZjY5OTI0ZDhhYjU1MTQ3OWQ3N2NiZCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.l18GWWquTouo7lS4umx9m6VQLSdZ1SfUQ2K-ei6IL_8}
:class: mini-image
:width: 30%
```

```{image} https://private-user-images.githubusercontent.com/4690904/345100588-ecd1d6a7-9b49-4a93-b635-2298d43abf09.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjgyNDkxNTYsIm5iZiI6MTcyODI0ODg1NiwicGF0aCI6Ii80NjkwOTA0LzM0NTEwMDU4OC1lY2QxZDZhNy05YjQ5LTRhOTMtYjYzNS0yMjk4ZDQzYWJmMDkucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI0MTAwNiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNDEwMDZUMjEwNzM2WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MDlmNDIxNDUxYjEzMTQ4N2Y0MmQ3M2QwOTZmMDM3NjhmNDljNDkwMzgyZDlmNzJjYWZhYjlkNzBmZjFjYjk1NiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.CORhm0Kv85fjGiqBJMM411WXQDtPZzRkbTVUUBTylLQ
:class: mini-image
:width: 30%
```
```{image} https://private-user-images.githubusercontent.com/4690904/345103010-12d7060b-35bc-40ca-89a3-f837c5417dbf.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjgyNDkxNTYsIm5iZiI6MTcyODI0ODg1NiwicGF0aCI6Ii80NjkwOTA0LzM0NTEwMzAxMC0xMmQ3MDYwYi0zNWJjLTQwY2EtODlhMy1mODM3YzU0MTdkYmYucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI0MTAwNiUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNDEwMDZUMjEwNzM2WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ODJlNmQ5ZWYzNzAxNWUzY2NhOGExNTE1MmM2ODg3NmRiMTNlYmE5NGQ4NjM1MjY4ODM4YTU0ODU4NzRmZTE0YiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.wzlzrABeXctUMPYKgbp68LH_XUl-G4xzLs7jv5PsPH8
:class: mini-image
:width: 30%
```

## 🐛 Bugs fixed

### Script saving on close

Users will be prompted to save unsaved changes to scripts when closing QuPath, even when the scripting editor is minimised so your precious code is safe.

###

## 👩‍💻 Scripting and API changes

### Faster running scripts for projects

When images arented needed in a script (for example exporting measurements) it will run faster. This is due to the image pixels are no longer fetched regardless if they are used or not.

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
