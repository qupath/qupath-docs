========
Commands
========

.. contents:: :local:
  :depth: 1

File
====

Create project
--------------
*File → Project... → Create project*

Create a new project. Usually it's easier just to drag an empty folder onto QuPath to create a project, rather than navigate these menus.

Open project
------------
*File → Project... → Open project*

Open an existing project. Usually it's easier just to drag a project folder onto QuPath to open it, rather than bother with this command.

Close project
-------------
*File → Project... → Close project*

Close the current project, including any images that are open.

Add images
----------
*File → Project... → Add images*

Add images to the current project. You can also add images by dragging files onto the main QuPath window.

Export image list
-----------------
*File → Project... → Export image list*

Export a list of the image paths for images in the current project.

Edit project metadata
---------------------
*File → Project... → Edit project metadata*

Edit the metadata for the current project. By adding key-value properties to images, they can be sorted and queried more easily.

Check project URIs
------------------
*File → Project... → Check project URIs*

Check the 'Uniform Resource Identifiers' for images in the current project. This basically helps fix things whenever files have moved and images can no longer be found.

Import images from v0.1.2
-------------------------
*File → Project... → Import images from v0.1.2*

Import images from a legacy project (QuPath v0.1.2 or earlier).

Note that it is generally a bad idea to mix versions of QuPath for analysis, but this can be helpful to recover old data and annotations.

The original images will need to be available, with the paths set correctly in the project file.

Open...
-------
*File → Open...*  - :kbd:`Ctrl+O`

Open an image in the current viewer, using a file chooser. You can also just drag the file on top of the viewer.

Open URI...
-----------
*File → Open URI...*  - :kbd:`Ctrl+Shift+O`

Open an image in the current viewer, by entering the path to the image. This can be used to add images that are not represented by local files (e.g. hosted by OMERO), but beware that a compatible image reader needs to be available to interpret them.

Reload data
-----------
*File → Reload data*  - :kbd:`Ctrl+R`

Reload any previously-saved data for the current image. This provides a more dramatic form of 'undo' (albeit without any 'redo' option).

Save As
-------
*File → Save As*  - :kbd:`Ctrl+Shift+S`

Save a .qpdata file for this image, specifying the file path. Warning! It is usually much better to use projects instead, and allow QuPath to decide where to store your data files.

Save
----
*File → Save*  - :kbd:`Ctrl+S`

Save a .qpdata file for this image. This command is best used within projects, where QuPath will choose the location to save the file.

Original pixels
---------------
*File → Export images... → Original pixels*

Export an image region, by extracting the pixels from the original image.

Rendered RGB (with overlays)
----------------------------
*File → Export images... → Rendered RGB (with overlays)*

Export an image region, as an RGB image matching how it is displayed in the viewer.

OME TIFF
--------
*File → Export images... → OME TIFF*

Write regions as OME-TIFF images. This supports writing image pyramids.

Rendered SVG
------------
*File → Export images... → Rendered SVG*

Export the current selected region as a rendered (RGB) SVG image. Any annotations and ROIs will be stored as vectors, which can later be adjusted in other software.

Main window screenshot
----------------------
*File → Export snapshot... → Main window screenshot*

Export the area of the screen corresponding to the main QuPath window to the clipboard. This includes any additional overlapping windows and dialog boxes.

Main window content
-------------------
*File → Export snapshot... → Main window content*

Export the contents of the main QuPath window to the clipboard. This ignores any additional overlapping windows and dialog boxes.

Current viewer content
----------------------
*File → Export snapshot... → Current viewer content*

Export the contents of the current viewer to the clipboard. Note that this creates an RGB image, which does not necessarily contain the original pixel values.

Current viewer content (SVG)
----------------------------
*File → Export snapshot... → Current viewer content (SVG)*

Export an RGB snapshot of the current viewer content as an SVG image. Any annotations and ROIs will be stored as vectors, which can later be adjusted in other software.

Import TMA map
--------------
*File → TMA data... → Import TMA map*

Import a TMA map, e.g. a grid containing 'Unique ID' values for each core.

Export TMA data
---------------
*File → TMA data... → Export TMA data*

Export TMA data for the current image, in a format compatible with the 'TMA data viewer'.

Launch TMA data viewer
----------------------
*File → TMA data... → Launch TMA data viewer*

Launch the 'TMA data viewer' to visualize TMA core data that was previously exported.

Quit
----
*File → Quit*

Quit QuPath.

Edit
====

Undo
----
*Edit → Undo*  - :kbd:`Ctrl+Z`

Undo the last action for the current viewer. Note QuPath's undo is limited, and turns itself off (for performance reasons) when many objects are present. The limit can be adjusted in the preferences.

Redo
----
*Edit → Redo*  - :kbd:`Ctrl+Shift+Z`

Redo the last action for the current viewer.

Current viewer
--------------
*Edit → Copy to clipboard... → Current viewer*  - :kbd:`Ctrl+C`

Copy the contents of the current viewer to the clipboard. Note that this creates an RGB image, which does not necessarily contain the original pixel values.

Main window content
-------------------
*Edit → Copy to clipboard... → Main window content*

Copy the contents of the main QuPath window to the clipboard. This ignores any additional overlapping windows and dialog boxes.

Main window screenshot
----------------------
*Edit → Copy to clipboard... → Main window screenshot*

Copy the area of the screen corresponding to the main QuPath window to the clipboard. This includes any additional overlapping windows and dialog boxes.

Full screenshot
---------------
*Edit → Copy to clipboard... → Full screenshot*

Make a screenshot and copy it to the clipboard.

Preferences...
--------------
*Edit → Preferences...*  - :kbd:`Ctrl+,`

Set preferences to customize QuPath's appearance and behavior.

Reset preferences
-----------------
*Edit → Reset preferences*

Reset preferences to their default values - this can be useful if you are experiencing any newly-developed persistent problems with QuPath.

Tools
=====

Move
----
*Tools → Move*  - :kbd:`M`

Move tool, both for moving around the viewer (panning) and moving objects (translation).

Rectangle
---------
*Tools → Rectangle*  - :kbd:`R`

Click and drag to draw a rectangle annotation. Hold down 'Shift' to constrain shape to be a square.

Ellipse
-------
*Tools → Ellipse*  - :kbd:`O`

Click and drag to draw an ellipse annotation. Hold down 'Shift' to constrain shape to be a circle.

Line
----
*Tools → Line*  - :kbd:`L`

Click and drag to draw a line annotation.

Polygon
-------
*Tools → Polygon*  - :kbd:`P`

Create a closed polygon annotation, either by clicking individual points (with double-click to end) or clicking and dragging.

Polyline
--------
*Tools → Polyline*  - :kbd:`V`

Create a polyline annotation, either by clicking individual points (with double-click to end) or clicking and dragging.

Brush
-----
*Tools → Brush*  - :kbd:`B`

Click and drag to paint with a brush. By default, the size of the region being drawn depends upon the zoom level in the viewer.

Wand tool
---------
*Tools → Wand tool*  - :kbd:`W`

Click and drag to draw with a wand tool. Adjust brightness/contrast or wand preferences to customize the sensitivity and behavior.

Points
------
*Tools → Points*  - :kbd:`.`

Click to add points to an annotation.

View
====

Show analysis pane
------------------
*View → Show analysis pane*  - :kbd:`Shift+A`

Show/hide the analysis pane (the one on the left).

Show command list
-----------------
*View → Show command list*  - :kbd:`Ctrl+L`

Show the command list (much easier than navigating menus...).

Brightness/Contrast
-------------------
*View → Brightness/Contrast*  - :kbd:`Shift+C`

Show the brightness/contrast dialog. This enables changing how the image is displayed, but not the image data itself.

Synchronize viewers
-------------------
*View → Synchronize viewers*  - :kbd:`Ctrl+Alt+S`

Synchronize panning and zooming when working with images open in multiple viewers.

Match viewer resolutions
------------------------
*View → Match viewer resolutions*

Adjust zoom factors to match the resolutions of images open in multiple viewers.

Show channel viewer
-------------------
*View → Mini viewers... → Show channel viewer*

Open a viewer window that shows individual channels of an image size by side.

Show mini viewer
----------------
*View → Mini viewers... → Show mini viewer*

Open a viewer window that shows a view of the pixel under the cursor.

400%
----
*View → Zoom... → 400%*

Set the zoom factor to 400% (downsample = 0.25).

100%
----
*View → Zoom... → 100%*

Set the zoom factor to 100% (downsample = 1).

10%
---
*View → Zoom... → 10%*

Set the zoom factor to 10% (downsample = 10).

1%
--
*View → Zoom... → 1%*

Set the zoom factor to 1% (downsample = 100).

Zoom in
-------
*View → Zoom... → Zoom in*  - :kbd:`+`

Zoom in for the current viewer.

Zoom out
--------
*View → Zoom... → Zoom out*  - :kbd:`-`

Zoom out for the current viewer.

Zoom to fit
-----------
*View → Zoom... → Zoom to fit*

Adjust zoom for all images to fit the entire image in the viewer.

Rotate image
------------
*View → Rotate image*

Rotate the image visually (this is only for display - the coordinate system remains unchanged).

Cell boundaries only
--------------------
*View → Cell display → Cell boundaries only*

Show cells by drawing the outer boundary ROI only.

Nuclei only
-----------
*View → Nuclei only*

Show cells by drawing the nucleus ROI only (if available).

Nuclei & cell boundaries
------------------------
*View → Nuclei & cell boundaries*

Show cells by drawing both the outer boundary and nucleus ROIs (if available).

Centroids only
--------------
*View → Centroids only*

Show cells by drawing the centroids only.

Show annotations
----------------
*View → Show annotations*  - :kbd:`A`

Toggle showing all annotations in the viewer.

Fill annotations
----------------
*View → Fill annotations*  - :kbd:`Shift+F`

Toggle showing annotation ROIs as filled shapes in the viewer.

Show names
----------
*View → Show names*  - :kbd:`N`

Toggle showing all annotation names in the viewer.

Show TMA grid
-------------
*View → Show TMA grid*  - :kbd:`G`

Toggle showing any TMA grid in the viewer.

Show TMA grid labels
--------------------
*View → Show TMA grid labels*

Toggle showing any TMA core labels in the viewer.

Show detections
---------------
*View → Show detections*  - :kbd:`D`

Toggle showing all detections in the viewer.

Fill detections
---------------
*View → Fill detections*  - :kbd:`F`

Toggle showing detection ROIs as filled shapes in the viewer.

Show object connections
-----------------------
*View → Show object connections*

Show connections between objects, if available. This can be used alongside some spatial commands, such as to display a Delaunay triangulation as an overlay.

Show pixel classification
-------------------------
*View → Show pixel classification*  - :kbd:`C`

Toggle pixel classification overlays in the viewer. This only has an effect if there is actually a pixel classification available.

Show slide overview
-------------------
*View → Show slide overview*

Toggle showing the image overview in the viewer. This is a clickable thumbnail used for navigation.

Show cursor location
--------------------
*View → Show cursor location*

Toggle showing the cursor location in the viewer.

Show scalebar
-------------
*View → Show scalebar*

Toggle showing the scalebar in the viewer.

Show grid
---------
*View → Show grid*  - :kbd:`Shift+G`

Toggle showing the counting grid in the viewer.

Set grid spacing
----------------
*View → Set grid spacing*

Adjust the counting grid spacing for the viewers.

Show view recorder
------------------
*View → Show view recorder*

Record zoom and panning movements within a viewer for later playback.

Show slide label
----------------
*View → Show slide label*

Show the slide label associated with the image in the active viewer (if available).

Show input display
------------------
*View → Show input display*

Show mouse clicks and keypresses on screen. This is particularly useful for demos and tutorials.

Show memory monitor
-------------------
*View → Show memory monitor*

Show a dialog to track memory usage within QuPath, and clear the cache if required.

Show log
--------
*View → Show log*  - :kbd:`Ctrl+Shift+L`

Show the log. This is very helpful for identifying and debugging errors. 

If you wish to report a problem using QuPath, please check the log for relevant information to provide.

Turn on all gestures
--------------------
*View → Multi-touch gestures → Turn on all gestures*

Turn on all multi-touch gestures for touchscreens and trackpads.

Turn off all gestures
---------------------
*View → Multi-touch gestures → Turn off all gestures*

Turn off all multi-touch gestures for touchscreens and trackpads.

Use scroll gestures
-------------------
*View → Multi-touch gestures → Use scroll gestures*

Toggle scroll gestures for touchscreens and trackpads.

Use zoom gestures
-----------------
*View → Multi-touch gestures → Use zoom gestures*

Toggle zoom gestures for touchscreens and trackpads.

Use rotate gestures
-------------------
*View → Multi-touch gestures → Use rotate gestures*

Toggle rotate gestures for touchscreens and trackpads.

Objects
=======

Delete selected objects
-----------------------
*Objects → Delete... → Delete selected objects*

Delete the currently selected objects.

Delete all objects
------------------
*Objects → Delete... → Delete all objects*

Delete all objects for the current image.

Delete all annotations
----------------------
*Objects → Delete... → Delete all annotations*

Delete all annotation objects for the current image.

Delete all detections
---------------------
*Objects → Delete... → Delete all detections*

Delete all detection objects for the current image.

Reset selection
---------------
*Objects → Select... → Reset selection*  - :kbd:`Ctrl+Alt+R`

Reset the selected objects for the current image.

Select TMA cores
----------------
*Objects → Select... → Select TMA cores*  - :kbd:`Ctrl+Alt+T`

Select all TMA cores for the current image.

Select annotations
------------------
*Objects → Select... → Select annotations*  - :kbd:`Ctrl+Alt+A`

Select all annotation objects for the current image.

Select all detections
---------------------
*Objects → Select... → Select detections... → Select all detections*  - :kbd:`Ctrl+Alt+D`

Select all detection objects for the current image (this includes cells and tiles).

Select cells
------------
*Objects → Select... → Select detections... → Select cells*  - :kbd:`Ctrl+Alt+C`

Select all cell objects for the current image.

Select tiles
------------
*Objects → Select... → Select detections... → Select tiles*

Select all tile objects for the current image.

Select objects by classification
--------------------------------
*Objects → Select... → Select objects by classification*

Select objects based upon their classification.

Specify annotation
------------------
*Objects → Annotations... → Specify annotation*

Create a rectangle or ellipse annotation with the specified properties.

Create full image annotation
----------------------------
*Objects → Annotations... → Create full image annotation*  - :kbd:`Ctrl+Shift+A`

Create an annotation representing the full width and height of the current image.

Insert into hierarchy
---------------------
*Objects → Annotations... → Insert into hierarchy*  - :kbd:`Ctrl+Shift+I`

Insert the selected objects in the object hierarchy. This involves resolving parent/child relationships based upon regions of interest.

Resolve hierarchy
-----------------
*Objects → Annotations... → Resolve hierarchy*  - :kbd:`Ctrl+Shift+R`

Resolve the object hierarchy by setting parent/child relationships between objects based upon regions of interest.

Rotate annotation
-----------------
*Objects → Annotations... → Rotate annotation*  - :kbd:`Ctrl+Alt+Shift+R`

Interactively rotate the current selected annotation.

Duplicate annotations
---------------------
*Objects → Annotations... → Duplicate annotations*  - :kbd:`Shift+D`

Duplicate the selected annotations.

Transfer last annotation
------------------------
*Objects → Annotations... → Transfer last annotation*  - :kbd:`Shift+E`

Transfer the last annotation to the current image. This can be used to bring annotations from one viewer to another, or to recover an annotation that has just been deleted.

Expand annotations
------------------
*Objects → Annotations... → Expand annotations*

Expand (or contract) the selected annotations, optionally removing the interior.

Split annotations
-----------------
*Objects → Annotations... → Split annotations*

Split complex annotations that contain disconnected pieces into separate annotations.

Remove fragments & holes
------------------------
*Objects → Annotations... → Remove fragments & holes*

Remove small fragments of annotations that contain disconnected pieces.

Fill holes
----------
*Objects → Annotations... → Fill holes*

Fill holes occurring inside annotations.

Make inverse
------------
*Objects → Annotations... → Make inverse*

Make annotations corresponding to the 'inverse' of the selected annotation. The inverse annotation contains 'everything else' outside the current annotation, constrained by its parent.

Merge selected
--------------
*Objects → Annotations... → Merge selected*

Merge the selected annotations to become one, single annotation.

Simplify shape
--------------
*Objects → Annotations... → Simplify shape*

Simplify the shapes of the current selected annotations. This removes vertices that are considered unnecessary, using a specified amplitude tolerance.

TMA
===

TMA dearrayer
-------------
*TMA → TMA dearrayer*

Identify cores and grid arrangement of a tissue microarray.

Add TMA row before
------------------
*TMA → Add... → Add TMA row before*

Add a row to the TMA grid before (above) the row containing the current selected object.

Add TMA row after
-----------------
*TMA → Add... → Add TMA row after*

Add a row to the TMA grid after (below) the row containing the current selected object.

Add TMA column before
---------------------
*TMA → Add... → Add TMA column before*

Add a column to the TMA grid before (to the left of) the column containing the current selected object.

Add TMA column after
--------------------
*TMA → Add... → Add TMA column after*

Add a column to the TMA grid after (to the right of) the column containing the current selected object.

Remove TMA row
--------------
*TMA → Remove... → Remove TMA row*

Remove the row containing the current selected object from the TMA grid.

Remove TMA column
-----------------
*TMA → Remove... → Remove TMA column*

Remove the column containing the current selected object from the TMA grid.

Relabel TMA grid
----------------
*TMA → Relabel TMA grid*

Relabel the cores of a TMA grid. This is often needed after adding or deleting rows or columns.

Reset TMA metadata
------------------
*TMA → Reset TMA metadata*

Remove all the metadata for the TMA grid in the current image.

Delete TMA grid
---------------
*TMA → Delete TMA grid*

Delete the TMA grid for the current image.

TMA grid summary view
---------------------
*TMA → TMA grid summary view*

Show an interactive summary view of all the TMA cores in the current image.

Find convex hull detections (TMA)
---------------------------------
*TMA → Find convex hull detections (TMA)*

Find all detections occurring on the convex hull of the detections within a TMA core. This can be used to find cells occurring towards the edge of the core, which can then be deleted if necessary. Often these cells may yield less reliable measurements because of artifacts.

Measure
=======

Show measurement maps
---------------------
*Measure → Show measurement maps*  - :kbd:`Ctrl+Shift+M`

View detection measurements in context using interactive, color-coded maps.

Show measurement manager
------------------------
*Measure → Show measurement manager*

View and optionally delete detection measurements.

Show TMA measurements
---------------------
*Measure → Show TMA measurements*

Show a measurement table for tissue microarray cores.

Show annotation measurements
----------------------------
*Measure → Show annotation measurements*

Show a measurement table for annotation objects.

Show detection measurements
---------------------------
*Measure → Show detection measurements*

Show a measurement table for detection objects.

Export measurements
-------------------
*Measure → Export measurements*

Export summary measurements for multiple images within a project.

Automate
========

Show script editor
------------------
*Automate → Show script editor*  - :kbd:`Ctrl+[`

Open the script editor.

Script interpreter
------------------
*Automate → Script interpreter*

Open a script interpreter. This makes it possible to run scripts interactively, line by line. However, in general the Script Editor is more useful.

Show workflow command history
-----------------------------
*Automate → Show workflow command history*  - :kbd:`Ctrl+Shift+W`

Show a history of the commands applied to the current image. Note that this is not fully exhaustive, because not all commands can be recorded. However, the command history is useful to help automatically generate batch-processing scripts.

Create command history script
-----------------------------
*Automate → Create command history script*

Create a script based upon the actions recorded in the command history.

Set script directory...
-----------------------
*Automate → Shared scripts... → Set script directory...*

Set the directory containing scripts that should be shown in this menu.

Analyze
=======

Estimate stain vectors
----------------------
*Analyze → Preprocessing → Estimate stain vectors*

Estimate stain vectors for color deconvolution in brightfield images. This can be used when there are precisely 2 stains (e.g. hematoxylin and eosin, hematoxylin and DAB) to improve stain separation.

Create tiles
------------
*Analyze → Tiles & superpixels → Create tiles*

Create tiles. These can be useful as part of a larger workflow, for example by adding intensity measurements to the tiles, training a classifier and then merging classified tiles to identify larger regions.

SLIC superpixel segmentation
----------------------------
*Analyze → Tiles & superpixels → SLIC superpixel segmentation*

Create superpixel tiles using the SLIC method.

DoG superpixel segmentation
---------------------------
*Analyze → Tiles & superpixels → DoG superpixel segmentation*

Create superpixel tiles using a Difference of Gaussians method.

Tile classifications to annotations
-----------------------------------
*Analyze → Tiles & superpixels → Tile classifications to annotations*

Merge tiles sharing the same classification to become annotations.

Fast cell counts (brightfield)
------------------------------
*Analyze → Cell detection → Fast cell counts (brightfield)*

Fast cell counting for hematoxylin and DAB images.

Cell detection
--------------
*Analyze → Cell detection → Cell detection*

Default cell detection in QuPath. Note that this is general-purpose method, not optimized for any particular staining.

It is essential to set the image type first (e.g. brightfield or fluorescence) before running this command.

Positive cell detection
-----------------------
*Analyze → Cell detection → Positive cell detection*

Equivalent to 'Cell detection', with additional parameters to set a threshold during detection to identify single-positive cells.

Subcellular detection (experimental)
------------------------------------
*Analyze → Cell detection → Subcellular detection (experimental)*

Identify subcellular structures (e.g. spots of all kinds) within detected cells.

Add smoothed features
---------------------
*Analyze → Calculate features → Add smoothed features*

Supplement the measurements for detection objects by calculating a weighted sum of the corresponding measurements from neighboring objects.

Add intensity features
----------------------
*Analyze → Calculate features → Add intensity features*

Add new intensity-based features to objects.

Add shape features
------------------
*Analyze → Calculate features → Add shape features*

Add new shape-based features to objects.

Distance to annotations 2D
--------------------------
*Analyze → Spatial analysis → Distance to annotations 2D*

Calculate distances between detection centroids and the closest annotation for each classification. For example, this may be used to identify the distance of every cell from 'bigger' region that has been annotated (e.g. an area of tumor, a blood vessel).

Detect centroid distances 2D
----------------------------
*Analyze → Spatial analysis → Detect centroid distances 2D*

Calculate distances between detection centroids for each classification. For example, this may be used to identify the closest cell of a specified type.

Delaunay cluster features 2D
----------------------------
*Analyze → Spatial analysis → Delaunay cluster features 2D*

Apply a Delaunay triangulation to detection objects based on their centroid locations. This helps identify clusters of objects neighboring one another.

Note this command is likely to be replaced in a future version.

Interactive image alignment
---------------------------
*Analyze → Interactive image alignment*

Experimental command to interactively align images using an Affine transform. This is currently not terribly useful in itself, but may be helpful as part of more complex scripting workflows.

Positive pixel count (deprecated)
---------------------------------
*Analyze → Deprecated → Positive pixel count (deprecated)*

Area-based quantification of positive pixels with DAB staining. This command does not handle large regions well; if possible, pixel classification should usually be used instead.

Simple tissue detection (deprecated)
------------------------------------
*Analyze → Deprecated → Simple tissue detection (deprecated)*

Detect large regions using a simple thresholding method. This command is not very flexible and lacks any preview of the results; if possible, pixel classification should usually be used instead.

Cell + membrane detection (deprecated)
--------------------------------------
*Analyze → Deprecated → Cell + membrane detection (deprecated)*

Cell detection that uses membrane information to constrain cell boundary expansion. 

This was designed specifically for hematoxylin and DAB staining, and works only where membrane staining is either very clear or absent. It is not recommended in general.

Classify
========

Reset detection classifications
-------------------------------
*Classify → Object classification → Reset detection classifications*

Reset the classifications of all detections.

Load object classifier
----------------------
*Classify → Object classification → Load object classifier*

Load an existing object classifier. This can be used to apply the classifier to new objects, but not to continue training.

Train object classifier
-----------------------
*Classify → Object classification → Train object classifier*  - :kbd:`Ctrl+Shift+D`

Interactively train an object classifier using machine learning. This is useful whenever objects cannot be classified based on one measurement alone.

Create single measurement classifier
------------------------------------
*Classify → Object classification → Create single measurement classifier*

Create a simple object classifier that applies a threshold to a single measurement.

Create composite classifier
---------------------------
*Classify → Object classification → Create composite classifier*

Combine multiple classifiers together to create a single classifier by applying them sequentially.

Set cell intensity classifications
----------------------------------
*Classify → Object classification → Set cell intensity classifications*

Set cell intensity classifications based upon a single measurement. This is useful to calculate densities/percentages of positive cells or H-scores.

Create detection classifier (deprecated)
----------------------------------------
*Classify → Object classification → Older classifiers → Create detection classifier (deprecated)*

QuPath's original detection classifier. 

This is being replaced by a new and more flexible approach to object classification.

Load detection classifier (deprecated)
--------------------------------------
*Classify → Object classification → Older classifiers → Load detection classifier (deprecated)*

Load an old-style detection classifier. Note that it is not a good idea to mix classifiers across different QuPath versions.

Load pixel classifier
---------------------
*Classify → Pixel classification → Load pixel classifier*

Load an existing pixel classifier. This can be used to apply the classifier to new images, but not to continue training.

Train pixel classifier
----------------------
*Classify → Pixel classification → Train pixel classifier*  - :kbd:`Ctrl+Shift+P`

Train a pixel classifier. This can be used to quantify areas, or to generate or classify objects.

Create thresholder
------------------
*Classify → Pixel classification → Create thresholder*

Create a simple pixel classifier that applies a threshold to an image.

Create region annotations
-------------------------
*Classify → Training images → Create region annotations*

Create annotations of fixed-size regions.

This can be used to select representative regions of multiple images to train (usually pixel) classifier, in combination with 'Create training image'.

Create training image
---------------------
*Classify → Training images → Create training image*

Create an image comprised of regions extracted from multiple images in a project. This can be useful for interactively training a classifier across a varied dataset.

Create duplicate channel training images
----------------------------------------
*Classify → Training images → Create duplicate channel training images*

Duplicate an image in a project so that there is one duplicate for each channel of the image. 

This can be used to train separate classifiers for different channels in multiplexed images, which are then merged to form a composite classifier.

Split project train/validation/test
-----------------------------------
*Classify → Training images → Split project train/validation/test*

Split images within a project into training, validation and test sets.

Extensions
==========

Send region to ImageJ
---------------------
*Extensions → ImageJ → Send region to ImageJ*

Extract the selected image region and send it to ImageJ.

Send snapshot to ImageJ
-----------------------
*Extensions → ImageJ → Send snapshot to ImageJ*

Create a rendered (RGB) snapshot and send it to ImageJ.

Set plugins directory
---------------------
*Extensions → ImageJ → Set plugins directory*

Set the plugins directory to use with QuPath's embedded version of ImageJ. 

This can be set to the plugins directory of an existing ImageJ installation, to make the plugins associated with that installation available within QuPath.

ImageJ macro runner
-------------------
*Extensions → ImageJ → ImageJ macro runner*

Run ImageJ macros within QuPath.

Help
====

Show setup options
------------------
*Help → Show setup options*

Show the setup options that appear when QuPath is first started, to set the maximum memory and locale.

Documentation (web)
-------------------
*Help → Documentation (web)*

Open the main QuPath documentation website.

YouTube channel (web)
---------------------
*Help → YouTube channel (web)*

Open the QuPath demo videos and tutorials.

Check for updates (web)
-----------------------
*Help → Check for updates (web)*

Check online for an updated QuPath release.

Cite QuPath (web)
-----------------
*Help → Cite QuPath (web)*

Please cite the QuPath publication if you use the software! 
This command opens a web page to show how.

Report bug (web)
----------------
*Help → Report bug (web)*

Report a bug. Please follow the template and do not use this for general questions!

View user forum (web)
---------------------
*Help → View user forum (web)*

Visit the user forum. This is the place to ask questions (and give answers).

View source code (web)
----------------------
*Help → View source code (web)*

View the QuPath source code online.

License
-------
*Help → License*

View license information for QuPath and its third-party dependencies.

System info
-----------
*Help → System info*

View system information.

Installed extensions
--------------------
*Help → Installed extensions*

View a list of installed QuPath extensions.
