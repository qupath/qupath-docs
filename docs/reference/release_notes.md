# Release Notes v0.6.0

Lots of useful and exciting changes have been made in this version of QuPath and we are thrilled to finally share them with you!
This document isn't a complete list of changes, for this please refer to the [CHANGELOG](https://github.com/qupath/qupath/blob/main/CHANGELOG.md).

1. [Major features](#major-features) - Spotlight changes
2. [Enhancements](#enhancements) - Improvements to existing features
3. [Keyboard Shortcuts](#keyboard-shortcuts) - External libraries and package updates

## 🚀 Major features

### Extension Manager/Wrangler

Ever been confused about which extensions you have installed or how to install new ones? Well hopefully the extension manager will help with that! You can now easily install, update and remove extensions all from within QuPath. The pre-existing installation method does still work but this new method is much more user friendly and will help you keep track of your extensions. More on the extension manager can be found in the [extension manager documentation](../intro/extensions.html#managing-extensions-with-the-extension-manager).

For extensions developed outside of the QuPath team, check out the [extension catalog github](https://github.com/qupath/extension-catalog-model) for how to add your extension to the extension catalog so other users can easily download it.

:::{figure}
:class: shadow-image full-image
Extension manager showing installed extensions
:::

### New InstanSeg Segmentation

It's here!!! The award winning [InstanSeg](https://github.com/qupath/qupath-extension-instanseg) segmentation method from Thibaut Goldsborough you can now do so in QuPath via the InstanSeg extension. This extension provides a greatly improved accuracy in segmentation of cells for both brightfield and fluorescent images. It also gets increasingly speedy with GPU support. Learn more about InstanSeg and how to use it in QuPath [here](../deep/instanseg.md).

:::{figure}
:class: shadow-image full-image

InstanSeg segmentation of haematoxylin and dab nuclei
:::

:::{figure}
:class: shadow-image full-image

InstanSeg segmentation of nuclei in a fluorescent image
:::

### Major OMERO Extension Reset

The OMERO extension has been completely rewritten under the hood, improving it's flexibility and giving access to more features such as the ability to retrieve pixel values (including raw values) in the way that your server is set up.

There has also been a big refresh to how the extension looks and feels, making it easier to use and navigate. Check out the [OMERO extension documentation](../reference/omero.md) for more information on how to get started.

:::{figure} ../reference/images/omero-overview.png
:class: shadow-image full-image

Viewing an image using OMERO extension
:::

### OME-Zarr images are now supported 🎉

It's now possible to open and work with OME-Zarr images in QuPath! OME-Zarr was developed by the OME team in collaboration with many individuals and institutes with the goal to provide a more efficient and scalable format for large images. To get started using this file type in QuPath, drag and drop an OME-Zarr image into the main window or use the 'Open' dialog to select an OME-Zarr image. Alternatively, you can also export to OME-Zarr format.

To learn more about OME-Zarr check out [this paper](https://link.springer.com/article/10.1007/s00418-023-02209-1) and how to export in QuPath [here](../advanced/exporting_images.html).

## ✨ Enhancements

### QuPath Tour 🗺

Unsure where to start with QuPath? Or maybe you just want a refresher on all the tools in the QuPath screen? The new QuPath tour will guide you through the interface, from the main viewing window to the toolbar and pane tabs. You can find "QuPath Tour" under the Help menu.

:::{figure}
:class: shadow-image full-image

QuPath tour explaining the interface
:::

### Toolbar Spring Clean 🧹

Following on from the QuPath tour, you may of notice the toolbar is looking a little different from before.
One new button has been added which allows for quick viewing of connections between objects (if you have any).
Viewer related tools such as "show scalebar", "show grid" and "show input display" have been combined into a dropdown button so that these less frequently used tools aren't always on screen, making the toolbar less busy.

:::{figure}
:class: shadow-image full-image

Updated 0.6.0 toolbar
:::

Alongside a shiny new icon design, tool buttons compatible with selection mode will now visually change when the selection mode is on to make it easier to see which mode is currently active.

Lastly, the selection mode can now be quickly accessed by using the 'S' key when the main viewer is selected.

### Annotation names

Viewing the names of annotations has been tweaked to make it easier to see which label relates to which annotation, particularly when annotations are small or overlap with others. The label is now consistently displayed at the top of the annotation and better adjusts to objective changes.

:::{figure}
:class: shadow-image full-image

Annotation names displayed at the top of the annotation
:::

### Class management

The class list within the annotation pane has been improved to make it easier to manage classes and less dependant on the one dropdown.

To add or remove or populate the class list in specific ways, this can now all be done from top of the pane.

:::{figure}
:class: shadow-image full-image

Class list pane with new class addition and deletion options
:::

Below, the options are related to showing or hiding classes within the viewer. Each class has a visual indicator for whether it's being shown or not and can be toggled on or off by clicking the eye icon next to that class name.

:::{figure}
:class: shadow-image full-image

Class list pane with new class viewing options
:::

### Project browser improvements

* **Image names can now be masked**: Useful for blinded studies or when you want to keep the image names private, just right click the pane and select "mask image names" toggle on or off.
* **Thumbnails can now be hidden**: Sometimes thumbnails can slow things down a lot in really big projects, so now you have the option to hide them for later. Additionally, the size of the thumbnail can be adjusted by right clicking on the thumbnail and selecting an option in "thumbnail size".
* **Alerts when images go missing**: Previously if an image was moved or deleted from the project folder, QuPath would not alert the user that the image was missing until the image was opened. Now, if an image is missing from the project folder, a warning will be displayed next to the name in the project browser so no more surprises when opening.
* **Sorted our sorting**: The sorting of images in projects has been sharpened up. Images will now remain sorted when re-opening the project or after adding new metadata values.

### Measurement viewing improvements

Minor visual improvements have been made to the measurement tables for annotations and detections. We hope this makes it clearer to use the tools already available. There is also an new option "Add class visibility", which links up the classes currently being displayed in the viewer to only show in the measurement table too.

:::{figure}
:class: shadow-image full-image

Measurement table with new class linking feature
:::

### Multidimensional image navigation + z-stack projection overlays

Navigating through time series and z-stacks now features a refreshed visual design, aimed at making it easier to explore your images. Additionally, for those looking to get a general overview of the z-stack, a maximum intensity projection overlay can now be displayed on top of the image. To learn more about this, check out the [multidimensional image documentation](../advanced/multidimensional_images.md).

### ImageJ script runner

!waiting on docs

### QuPath and fiji built together

!I may not be the best person to hype this up

### Dependency updates

!waiting on final list

## Keyboard shortcuts

* **Tired of using the mouse to close sub-windows?** Now you can press {kbd}`Esc` or {kbd}`Ctrl + W` to close them (well, most of them... let us know if an important window isn't responding to this and you think it should).
* **Got lots of things to select?** Quickly activate the selection tool by pressing 'S' when the main viewer is selected.
* **Want to select all the annodations or detections?** Use {kbd}`Ctrl + Alt + A` to select all annotations or {kbd}`Ctrl + Alt + D` to select the detections in the current image.
