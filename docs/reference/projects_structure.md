# Project structure

This section provides an overview of the contents of a {doc}`project directory <../tutorials/projects>` within QuPath.

:::{note}
Projects are actually represented by a Java interface.
This means they do not *have* to rely on the local filesystem, and could be implemented differently.

However, here we focus on the 'default' project implementation within QuPath, which uses a specific folder.
:::

## The *project.qpproj* file

This provides a JSON representation of the images within the project.

Each image is referred to as a **project entry**, and has

- A **serverBuilder** to create the `ImageServer`
- A unique **entryID**
- A human-readable **imageName** used to help identify the image
- A **randomizedName**, which is a UUID that can be used to mask the image name if *Mask image names* is selected under {menuselection}`Edit --> Preferences...`

The *serverBuilder* typically specifies an image reading library (e.g. OpenSlide, Bio-Formats) and URI representing the full path to the image.
It can also include additional instructions, e.g. that the image should be rotated or have custom metadata set.

:::{tip}
A *.qpproj* file can be opened and edited in a text editor - although this should be done with care, to avoid making the JSON invalid!
:::

:::{tip}
It is possible to duplicate the *project.qpproj* file, and have a copy within the same project directory that gives another view on the same data.
You can use any filename so long as the *.qpproj* extension is retained.
The file will define the image paths for the project, which do not need to be identical to those in the original *project.qpproj* file - although they should refer to the same images.

If you open the project by dragging the folder onto QuPath, a drop-down list will be displayed from which you can choose which *.qpproj* file to use.

This can be useful in two scenarios:

- You are working on a shared drive, and want to work with the same project across multiple computers. The paths to the images might differ for each computer. You can set the image paths within each *.qpproj* file differently, and open the appropriate file for the computer currently in use.
- You wish to create a project that contains only a subset of all the images, while retaining the ability to access all images elsewhere. This could be useful, for example, if you want to separate out a training and test set of images.
:::

:::{warning}
If you do create duplicate *.qpproj* files as above, be cautious if you wish to add new images later - since this may inadvertently result in adding different images with the same IDs.
:::

## The *data* directory

The *data* directory contains separate subdirectories for each *entry*, named according to the *entryID*.

Each subdirectory may contain

- A **data.qpdata** file containing the main saved data (including the object hierarchy) for the entry
- A **thumbnail.jpg** that is displayed under the *Project* tab through the user interface
- A **summary.json** file that contains some summary data

The summary data should be written at the same time as *data.qpdata*, and provides a mechanism to preview the saved data for the entry without opening the entire (possibly-large) *data.qpdata* file.

## The *scripts* directory

The optional *scripts* directory can contain Groovy scripts relevant to the project.
When the project is opened, these can be accessed directly via the {menuselection}`Automate --> Project scripts...` menu.

## The *classifiers* directory

The *classifiers* directory contains files related to classification within QuPath.

- A **classes.json** file, which contains the default classifications available under the *Annotations* tab (used when training classifiers)
- An optional **pixel_classifiers** subdirectory containing pixel classifiers relevant to the project
- An optional **object_classifiers** subdirectory containing object classifiers relevant to the project
