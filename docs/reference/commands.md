# Commands

:::{contents}
:local:
:depth: 1
:::

<!-- Generated with 
qupath.lib.gui.tools.CommandFinderTools.menusToMarkdown() 
(Remember to reset preferences and don't open a project, to avoid 'dynamic' lines!)
-->

## File
### Create project
{menuselection}`File --> Project... --> Create project`

Create a new project. Usually it's easier just to drag an empty folder onto QuPath to create a project, rather than navigate these menus.

### Open project
{menuselection}`File --> Project... --> Open project`

Open an existing project. Usually it's easier just to drag a project folder onto QuPath to open it, rather than bother with this command.

### Close project
{menuselection}`File --> Project... --> Close project`

Close the current project, including any images that are open.

### Add images
{menuselection}`File --> Project... --> Add images`

Add images to the current project. You can also add images by dragging files onto the main QuPath window.

### Export image list
{menuselection}`File --> Project... --> Export image list`

Export a list of the image paths for images in the current project.

### Edit project metadata
{menuselection}`File --> Project... --> Edit project metadata`

Edit the metadata for the current project. By adding key-value properties to images, they can be sorted and queried more easily.

### Check project URIs
{menuselection}`File --> Project... --> Check project URIs`

Check the 'Uniform Resource Identifiers' for images in the current project. This basically helps fix things whenever files have moved and images can no longer be found.

### Import images from v0.1.2
{menuselection}`File --> Project... --> Import images from v0.1.2`

Import images from a legacy project (QuPath v0.1.2 or earlier).

Note that it is generally a bad idea to mix versions of QuPath for analysis, but this can be helpful to recover old data and annotations.

The original images will need to be available, with the paths set correctly in the project file.

### Open...
{menuselection}`File --> Open...`  - {kbd}`Ctrl+O`

Open an image in the current viewer, using a file chooser. You can also just drag the file on top of the viewer.

### Open URI...
{menuselection}`File --> Open URI...`  - {kbd}`Shift+Ctrl+O`

Open an image in the current viewer, by entering the path to the image. This can be used to add images that are not represented by local files (e.g. hosted by OMERO), but beware that a compatible image reader needs to be available to interpret them.

### Reload data
{menuselection}`File --> Reload data`  - {kbd}`Ctrl+R`

Reload any previously-saved data for the current image. This provides a more dramatic form of 'undo' (albeit without any 'redo' option).

### Save As
{menuselection}`File --> Save As`  - {kbd}`Shift+Ctrl+S`

Save a .qpdata file for this image, specifying the file path. Warning! It is usually much better to use projects instead, and allow QuPath to decide where to store your data files.

### Save
{menuselection}`File --> Save`  - {kbd}`Ctrl+S`

Save a .qpdata file for this image. This command is best used within projects, where QuPath will choose the location to save the file.

### Original pixels
{menuselection}`File --> Export images... --> Original pixels`

Export an image region, by extracting the pixels from the original image.

### Rendered RGB (with overlays)
{menuselection}`File --> Export images... --> Rendered RGB (with overlays)`

Export an image region, as an RGB image matching how it is displayed in the viewer.

### OME TIFF
{menuselection}`File --> Export images... --> OME TIFF`

Write regions as OME-TIFF images. This supports writing image pyramids.

### Rendered SVG
{menuselection}`File --> Export images... --> Rendered SVG`

Export the current selected region as a rendered (RGB) SVG image. Any annotations and ROIs will be stored as vectors, which can later be adjusted in other software.

### Main window screenshot
{menuselection}`File --> Export snapshot... --> Main window screenshot`

Export the area of the screen corresponding to the main QuPath window to the clipboard. This includes any additional overlapping windows and dialog boxes.

### Main window content
{menuselection}`File --> Export snapshot... --> Main window content`

Export the contents of the main QuPath window to the clipboard. This ignores any additional overlapping windows and dialog boxes.

### Current viewer content
{menuselection}`File --> Export snapshot... --> Current viewer content`

Export the contents of the current viewer to the clipboard. Note that this creates an RGB image, which does not necessarily contain the original pixel values.

### Current viewer content (SVG)
{menuselection}`File --> Export snapshot... --> Current viewer content (SVG)`

Export an RGB snapshot of the current viewer content as an SVG image. Any annotations and ROIs will be stored as vectors, which can later be adjusted in other software.

### Import objects from file
{menuselection}`File --> Import objects from file`

Import objects from GeoJSON or .qpdata files.

### Export objects as GeoJSON
{menuselection}`File --> Export objects as GeoJSON`

Export objects in GeoJSON format to file.

### Import TMA map
{menuselection}`File --> TMA data... --> Import TMA map`

Import a TMA map, e.g. a grid containing 'Unique ID' values for each core.

### Export TMA data
{menuselection}`File --> TMA data... --> Export TMA data`

Export TMA data for the current image, in a format compatible with the 'TMA data viewer'.

### Launch TMA data viewer
{menuselection}`File --> TMA data... --> Launch TMA data viewer`

Launch the 'TMA data viewer' to visualize TMA core data that was previously exported.

### Quit
{menuselection}`File --> Quit`

Quit QuPath.

## Edit
### Undo
{menuselection}`Edit --> Undo`  - {kbd}`Ctrl+Z`

Undo the last action for the current viewer. Note QuPath's undo is limited, and turns itself off (for performance reasons) when many objects are present. The limit can be adjusted in the preferences.

### Redo
{menuselection}`Edit --> Redo`  - {kbd}`Shift+Ctrl+Z`

Redo the last action for the current viewer.

### Selected objects
{menuselection}`Edit --> Copy to clipboard... --> Selected objects`

Copy the selected objects to the system clipboard as GeoJSON.

### Annotation objects
{menuselection}`Edit --> Copy to clipboard... --> Annotation objects`

Copy all annotation objects to the system clipboard as GeoJSON.

### Current viewer
{menuselection}`Edit --> Copy to clipboard... --> Current viewer`

Copy the contents of the current viewer to the clipboard. Note that this creates an RGB image, which does not necessarily contain the original pixel values.

### Main window content
{menuselection}`Edit --> Copy to clipboard... --> Main window content`

Copy the contents of the main QuPath window to the clipboard. This ignores any additional overlapping windows and dialog boxes.

### Main window screenshot
{menuselection}`Edit --> Copy to clipboard... --> Main window screenshot`

Copy the area of the screen corresponding to the main QuPath window to the clipboard. This includes any additional overlapping windows and dialog boxes.

### Full screenshot
{menuselection}`Edit --> Copy to clipboard... --> Full screenshot`

Make a screenshot and copy it to the clipboard.

### Paste
{menuselection}`Edit --> Paste`

Paste the contents of the system clipboard, if possible.
If the clipboard contents are GeoJSON objects, the objects will be pasted to the current image. Otherwise, any text found will be shown in a the script editor.

### Paste objects to current plane
{menuselection}`Edit --> Paste objects to current plane`

Paste GeoJSON objects from the system clipboard to the current z-slice and timepoint, if possible.
New object IDs will be generated if needed to avoid duplicates.

### Preferences...
{menuselection}`Edit --> Preferences...`  - {kbd}`Ctrl+','`

Set preferences to customize QuPath's appearance and behavior.

### Reset preferences
{menuselection}`Edit --> Reset preferences`

Reset preferences to their default values - this can be useful if you are experiencing any newly-developed persistent problems with QuPath.

## Tools
### Move
{menuselection}`Tools --> Move`  - {kbd}`M`

Move tool, both for moving around the viewer (panning) and moving objects (translation).

### Rectangle
{menuselection}`Tools --> Rectangle`  - {kbd}`R`

Click and drag to draw a rectangle annotation. Hold down 'Shift' to constrain shape to be a square.

### Ellipse
{menuselection}`Tools --> Ellipse`  - {kbd}`O`

Click and drag to draw an ellipse annotation. Hold down 'Shift' to constrain shape to be a circle.

### Line
{menuselection}`Tools --> Line`  - {kbd}`L`

Click and drag to draw a line annotation.

### Polygon
{menuselection}`Tools --> Polygon`  - {kbd}`P`

Create a closed polygon annotation, either by clicking individual points (with double-click to end) or clicking and dragging.

### Polyline
{menuselection}`Tools --> Polyline`  - {kbd}`V`

Create a polyline annotation, either by clicking individual points (with double-click to end) or clicking and dragging.

### Brush
{menuselection}`Tools --> Brush`  - {kbd}`B`

Click and drag to paint with a brush. By default, the size of the region being drawn depends upon the zoom level in the viewer.

### Wand
{menuselection}`Tools --> Wand`  - {kbd}`W`

Click and drag to draw with a wand tool. Adjust brightness/contrast or wand preferences to customize the sensitivity and behavior.

### Points
{menuselection}`Tools --> Points`  - {kbd}`'.'`

Click to add points to an annotation.

### Selection mode
{menuselection}`Tools --> Selection mode`  - {kbd}`Shift+S`

Turn on/off selection mode - this converts drawing tools into selection tools

## View
### Show analysis pane
{menuselection}`View --> Show analysis pane`  - {kbd}`Shift+A`

Show/hide the analysis pane (the one on the left).

### Show command list
{menuselection}`View --> Show command list`  - {kbd}`Ctrl+L`

Show the command list (much easier than navigating menus...).

### Show recent commands
{menuselection}`View --> Show recent commands`  - {kbd}`Ctrl+P`

Show a list containing recently-used commands.

### Brightness/Contrast
{menuselection}`View --> Brightness/Contrast`  - {kbd}`Shift+C`

Show the brightness/contrast dialog. This enables changing how the image is displayed, but not the image data itself.

### Synchronize viewers
{menuselection}`View --> Multi-view... --> Synchronize viewers`  - {kbd}`Alt+Ctrl+S`

Synchronize panning and zooming when working with images open in multiple viewers.

### Match viewer resolutions
{menuselection}`View --> Multi-view... --> Match viewer resolutions`

Adjust zoom factors to match the resolutions of images open in multiple viewers.

### Add row
{menuselection}`View --> Multi-view... --> Add row`

Add a new row of viewers to the multi-view grid. This makes it possible to view two or more images side-by-side (vertically).

### Add column
{menuselection}`View --> Multi-view... --> Add column`

Add a new column of viewers to the multi-view grid. This makes it possible to view two or more images side-by-side (horizontally).

### Remove row
{menuselection}`View --> Multi-view... --> Remove row`

Remove the row containing the current viewer from the multi-view grid, if possible. The last row cannot be removed.

### Remove column
{menuselection}`View --> Multi-view... --> Remove column`

Remove the column containing the current viewer from the multi-view grid, if possible. The last column cannot be removed.

### Reset grid size
{menuselection}`View --> Multi-view... --> Reset grid size`

Reset the multi-view grid so that all viewers have the same size

### Close viewer
{menuselection}`View --> Multi-view... --> Close viewer`

Close the image in the current viewer. This is needed before it's possible to remove a viewer from the multi-view grid.

### Show channel viewer
{menuselection}`View --> Show channel viewer`

Open a viewer window that shows individual channels of an image size by side. This is useful when working with multiplexed/multichannel fluorescence images.

### Show mini viewer
{menuselection}`View --> Show mini viewer`

Open a viewer window that shows a view of the pixel under the cursor. This is useful for viewing the image booth zoomed in and zoomed out at the same time.

### 400%
{menuselection}`View --> Zoom... --> 400%`

Set the zoom factor to 400% (downsample = 0.25).

### 100%
{menuselection}`View --> Zoom... --> 100%`

Set the zoom factor to 100% (downsample = 1).

### 10%
{menuselection}`View --> Zoom... --> 10%`

Set the zoom factor to 10% (downsample = 10).

### 1%
{menuselection}`View --> Zoom... --> 1%`

Set the zoom factor to 1% (downsample = 100).

### Zoom in
{menuselection}`View --> Zoom... --> Zoom in`

Zoom in for the current viewer.

### Zoom out
{menuselection}`View --> Zoom... --> Zoom out`  - {kbd}`'-'`

Zoom out for the current viewer.

### Zoom to fit
{menuselection}`View --> Zoom... --> Zoom to fit`

Adjust zoom for all images to fit the entire image in the viewer.

### Rotate image
{menuselection}`View --> Rotate image`

Rotate the image visually (this is only for display - the coordinate system remains unchanged).

### Cell boundaries only
{menuselection}`View --> Cell display --> Cell boundaries only`

Show cells by drawing the outer boundary ROI only.

### Nuclei only
{menuselection}`View --> Nuclei only`

Show cells by drawing the nucleus ROI only (if available).

### Nuclei & cell boundaries
{menuselection}`View --> Nuclei & cell boundaries`

Show cells by drawing both the outer boundary and nucleus ROIs (if available).

### Centroids only
{menuselection}`View --> Centroids only`

Show cells by drawing the centroids only.

### Show annotations
{menuselection}`View --> Show annotations`  - {kbd}`A`

Toggle showing all annotations in the viewer.

### Fill annotations
{menuselection}`View --> Fill annotations`  - {kbd}`Shift+F`

Toggle showing annotation ROIs as filled shapes in the viewer.

### Show names
{menuselection}`View --> Show names`  - {kbd}`N`

Toggle showing all annotation names in the viewer.

### Show TMA grid
{menuselection}`View --> Show TMA grid`  - {kbd}`G`

Toggle showing any TMA grid in the viewer.

### Show TMA grid labels
{menuselection}`View --> Show TMA grid labels`

Toggle showing any TMA core labels in the viewer.

### Show detections
{menuselection}`View --> Show detections`  - {kbd}`D`

Toggle showing all detections in the viewer.

### Fill detections
{menuselection}`View --> Fill detections`  - {kbd}`F`

Toggle showing detection ROIs as filled shapes in the viewer.

### Show object connections
{menuselection}`View --> Show object connections`

Show connections between objects, if available. This can be used alongside some spatial commands, such as to display a Delaunay triangulation as an overlay.

### Show pixel classification
{menuselection}`View --> Show pixel classification`  - {kbd}`C`

Toggle pixel classification overlays in the viewer. This only has an effect if there is actually a pixel classification available.

### Show slide overview
{menuselection}`View --> Show slide overview`

Toggle showing the image overview in the viewer. This is a clickable thumbnail used for navigation.

### Show cursor location
{menuselection}`View --> Show cursor location`

Toggle showing the cursor location in the viewer.

### Show scalebar
{menuselection}`View --> Show scalebar`

Toggle showing the scalebar in the viewer.

### Show grid
{menuselection}`View --> Show grid`  - {kbd}`Shift+G`

Toggle showing the counting grid in the viewer.

### Set grid spacing
{menuselection}`View --> Set grid spacing`

Adjust the counting grid spacing for the viewers.

### Show view tracker
{menuselection}`View --> Show view tracker`

Record zoom and panning movements within a viewer for later playback and analysis.

### Show slide label
{menuselection}`View --> Show slide label`

Show the slide label associated with the image in the active viewer (if available).

### Show input display
{menuselection}`View --> Show input display`

Show mouse clicks and keypresses on screen. This is particularly useful for demos and tutorials.

### Show memory monitor
{menuselection}`View --> Show memory monitor`

Show a dialog to track memory usage within QuPath, and clear the cache if required.

### Show log
{menuselection}`View --> Show log`  - {kbd}`Shift+Ctrl+L`

Show the log. This is very helpful for identifying and debugging errors. 

If you wish to report a problem using QuPath, please check the log for relevant information to provide.

### Turn on all gestures
{menuselection}`View --> Multi-touch gestures --> Turn on all gestures`

Turn on all multi-touch gestures for touchscreens and trackpads.

### Turn off all gestures
{menuselection}`View --> Multi-touch gestures --> Turn off all gestures`

Turn off all multi-touch gestures for touchscreens and trackpads.

### Use scroll gestures
{menuselection}`View --> Multi-touch gestures --> Use scroll gestures`

Toggle scroll gestures for touchscreens and trackpads.

### Use zoom gestures
{menuselection}`View --> Multi-touch gestures --> Use zoom gestures`

Toggle zoom gestures for touchscreens and trackpads.

### Use rotate gestures
{menuselection}`View --> Multi-touch gestures --> Use rotate gestures`

Toggle rotate gestures for touchscreens and trackpads.

## Objects
### Delete selected objects
{menuselection}`Objects --> Delete... --> Delete selected objects`

Delete the currently selected objects.

### Delete all objects
{menuselection}`Objects --> Delete... --> Delete all objects`

Delete all objects for the current image.

### Delete all annotations
{menuselection}`Objects --> Delete... --> Delete all annotations`

Delete all annotation objects for the current image.

### Delete all detections
{menuselection}`Objects --> Delete... --> Delete all detections`

Delete all detection objects for the current image.

### Reset selection
{menuselection}`Objects --> Select... --> Reset selection`  - {kbd}`Alt+Ctrl+R`

Reset the selected objects for the current image.

### Select TMA cores
{menuselection}`Objects --> Select... --> Select TMA cores`  - {kbd}`Alt+Ctrl+T`

Select all TMA cores for the current image.

### Select annotations
{menuselection}`Objects --> Select... --> Select annotations`  - {kbd}`Alt+Ctrl+A`

Select all annotation objects for the current image.

### Select all detections
{menuselection}`Objects --> Select... --> Select detections... --> Select all detections`  - {kbd}`Alt+Ctrl+D`

Select all detection objects for the current image (this includes cells and tiles).

### Select cells
{menuselection}`Objects --> Select... --> Select detections... --> Select cells`  - {kbd}`Alt+Ctrl+C`

Select all cell objects for the current image.

### Select tiles
{menuselection}`Objects --> Select... --> Select detections... --> Select tiles`

Select all tile objects for the current image.

### Select objects by classification
{menuselection}`Objects --> Select... --> Select objects by classification`

Select objects based upon their classification.

### Select objects on current plane
{menuselection}`Objects --> Select... --> Select objects on current plane`

Select all objects on the current plane visiible in the viewer.

### Lock selected objects
{menuselection}`Objects --> Lock... --> Lock selected objects`  - {kbd}`Shift+Ctrl+K`

Lock all currently selected objects.

### Unlock selected objects
{menuselection}`Objects --> Lock... --> Unlock selected objects`  - {kbd}`Alt+Ctrl+K`

Unlock all currently selected objects.

### Toggle selected objects locked
{menuselection}`Objects --> Lock... --> Toggle selected objects locked`  - {kbd}`Ctrl+K`

Toggle the 'locked' state of all currently selected objects.

### Show object descriptions
{menuselection}`Objects --> Show object descriptions`

Show descriptions for the currently-selected object, where available. Descriptions can be any plain text, markdown or html added as the 'description' property to an object (currently, only annotations are supported).

### Specify annotation
{menuselection}`Objects --> Annotations... --> Specify annotation`

Create a rectangle or ellipse annotation with the specified properties.

### Create full image annotation
{menuselection}`Objects --> Annotations... --> Create full image annotation`  - {kbd}`Shift+Ctrl+A`

Create an annotation representing the full width and height of the current image.

### Insert into hierarchy
{menuselection}`Objects --> Annotations... --> Insert into hierarchy`  - {kbd}`Shift+Ctrl+I`

Insert the selected objects in the object hierarchy. This involves resolving parent/child relationships based upon regions of interest.

### Resolve hierarchy
{menuselection}`Objects --> Annotations... --> Resolve hierarchy`  - {kbd}`Shift+Ctrl+R`

Resolve the object hierarchy by setting parent/child relationships between objects based upon regions of interest.

### Transform annotations
{menuselection}`Objects --> Annotations... --> Transform annotations`  - {kbd}`Shift+Ctrl+T`

Interactively translate and/or rotate the current selected annotation.

### Duplicate selected annotations
{menuselection}`Objects --> Annotations... --> Duplicate selected annotations`  - {kbd}`Shift+D`

Duplicate the selected annotations.

### Copy annotations to current plane
{menuselection}`Objects --> Annotations... --> Copy annotations to current plane`  - {kbd}`Shift+Ctrl+V`

Duplicate the selected objects and paste them on the current plane (z-slice and timepoint visible in the viewer).
This avoids using the system clipboard. It is intended to help transfer annotations quickly across multidimensional images.

### Transfer last annotation
{menuselection}`Objects --> Annotations... --> Transfer last annotation`  - {kbd}`Shift+E`

Transfer the last annotation to the current image. This can be used to bring annotations from one viewer to another, or to recover an annotation that has just been deleted.

### Expand annotations
{menuselection}`Objects --> Annotations... --> Expand annotations`

Expand (or contract) the selected annotations, optionally removing the interior.

### Split annotations
{menuselection}`Objects --> Annotations... --> Split annotations`

Split complex annotations that contain disconnected pieces into separate annotations.

### Remove fragments & holes
{menuselection}`Objects --> Annotations... --> Remove fragments & holes`

Remove small fragments of annotations that contain disconnected pieces.

### Fill holes
{menuselection}`Objects --> Annotations... --> Fill holes`

Fill holes occurring inside annotations.

### Make inverse
{menuselection}`Objects --> Annotations... --> Make inverse`

Make annotations corresponding to the 'inverse' of the selected annotation. The inverse annotation contains 'everything else' outside the current annotation, constrained by its parent.

### Merge selected
{menuselection}`Objects --> Annotations... --> Merge selected`

Merge the selected annotations to become one, single annotation.

### Simplify shape
{menuselection}`Objects --> Annotations... --> Simplify shape`

Simplify the shapes of the current selected annotations. This removes vertices that are considered unnecessary, using a specified amplitude tolerance.

### Refresh object IDs
{menuselection}`Objects --> Refresh object IDs`

Update all object IDs to ensure they are unique.

### Refresh duplicate object IDs
{menuselection}`Objects --> Refresh duplicate object IDs`

Update all duplicate object IDs to ensure they are unique.

## TMA
### TMA dearrayer
{menuselection}`TMA --> TMA dearrayer`

Identify cores and grid arrangement of a tissue microarray.

### Specify TMA grid
{menuselection}`TMA --> Specify TMA grid`

Create a manual TMA grid, by defining labels and the core diameter. This can optionally be restricted to a rectangular annotation.

### Add TMA row before
{menuselection}`TMA --> Add... --> Add TMA row before`

Add a row to the TMA grid before (above) the row containing the current selected object.

### Add TMA row after
{menuselection}`TMA --> Add... --> Add TMA row after`

Add a row to the TMA grid after (below) the row containing the current selected object.

### Add TMA column before
{menuselection}`TMA --> Add... --> Add TMA column before`

Add a column to the TMA grid before (to the left of) the column containing the current selected object.

### Add TMA column after
{menuselection}`TMA --> Add... --> Add TMA column after`

Add a column to the TMA grid after (to the right of) the column containing the current selected object.

### Remove TMA row
{menuselection}`TMA --> Remove... --> Remove TMA row`

Remove the row containing the current selected object from the TMA grid.

### Remove TMA column
{menuselection}`TMA --> Remove... --> Remove TMA column`

Remove the column containing the current selected object from the TMA grid.

### Relabel TMA grid
{menuselection}`TMA --> Relabel TMA grid`

Relabel the cores of a TMA grid. This is often needed after adding or deleting rows or columns.

### Reset TMA metadata
{menuselection}`TMA --> Reset TMA metadata`

Remove all the metadata for the TMA grid in the current image.

### Delete TMA grid
{menuselection}`TMA --> Delete TMA grid`

Delete the TMA grid for the current image.

### Find convex hull detections (TMA)
{menuselection}`TMA --> Find convex hull detections (TMA)`

Find all detections occurring on the convex hull of the detections within a TMA core. This can be used to find cells occurring towards the edge of the core, which can then be deleted if necessary. Often these cells may yield less reliable measurements because of artifacts.

## Measure
### Show measurement maps
{menuselection}`Measure --> Show measurement maps`  - {kbd}`Shift+Ctrl+M`

View detection measurements in context using interactive, color-coded maps.

### Show measurement manager
{menuselection}`Measure --> Show measurement manager`

View and optionally delete detection measurements.

### Show TMA measurements
{menuselection}`Measure --> Show TMA measurements`

Show a measurement table for tissue microarray cores.

### Show annotation measurements
{menuselection}`Measure --> Show annotation measurements`

Show a measurement table for annotation objects.

### Show detection measurements
{menuselection}`Measure --> Show detection measurements`

Show a measurement table for detection objects.

### Annotation grid summary view
{menuselection}`Measure --> Grid views --> Annotation grid summary view`

Show all the annotations in the current image in a grid view, which can be ranked by measurements.

### TMA grid summary view
{menuselection}`Measure --> Grid views --> TMA grid summary view`

Show all the TMA cores in the current image in a grid view, which can be ranked by measurements.

### Export measurements
{menuselection}`Measure --> Export measurements`

Export summary measurements for multiple images within a project.

## Automate
### Show script editor
{menuselection}`Automate --> Show script editor`  - {kbd}`Ctrl+'['`

Open the script editor.

### Script interpreter
{menuselection}`Automate --> Script interpreter`

Open a script interpreter. This makes it possible to run scripts interactively, line by line. However, in general the Script Editor is more useful.

### Show workflow command history
{menuselection}`Automate --> Show workflow command history`  - {kbd}`Shift+Ctrl+W`

Show a history of the commands applied to the current image. Note that this is not fully exhaustive, because not all commands can be recorded. However, the command history is useful to help automatically generate batch-processing scripts.

### Create command history script
{menuselection}`Automate --> Create command history script`

Create a script based upon the actions recorded in the command history.

### No scripts found
{menuselection}`Automate --> Shared scripts... --> No scripts found`


### No scripts found
{menuselection}`Automate --> User scripts... --> No scripts found`


## Analyze
### Estimate stain vectors
{menuselection}`Analyze --> Preprocessing --> Estimate stain vectors`

Estimate stain vectors for color deconvolution in brightfield images. This can be used when there are precisely 2 stains (e.g. hematoxylin and eosin, hematoxylin and DAB) to improve stain separation.

### Create tiles
{menuselection}`Analyze --> Tiles & superpixels --> Create tiles`

Create tiles. These can be useful as part of a larger workflow, for example by adding intensity measurements to the tiles, training a classifier and then merging classified tiles to identify larger regions.

### SLIC superpixel segmentation
{menuselection}`Analyze --> Tiles & superpixels --> SLIC superpixel segmentation`

Create superpixel tiles using the SLIC method.

### DoG superpixel segmentation
{menuselection}`Analyze --> Tiles & superpixels --> DoG superpixel segmentation`

Create superpixel tiles using a Difference of Gaussians method.

### Tile classifications to annotations
{menuselection}`Analyze --> Tiles & superpixels --> Tile classifications to annotations`

Merge tiles sharing the same classification to become annotations.

### Cell detection
{menuselection}`Analyze --> Cell detection --> Cell detection`

Default cell detection in QuPath. Note that this is general-purpose method, not optimized for any particular staining.

It is essential to set the image type first (e.g. brightfield or fluorescence) before running this command.

### Positive cell detection
{menuselection}`Analyze --> Cell detection --> Positive cell detection`

Equivalent to 'Cell detection', with additional parameters to set a threshold during detection to identify single-positive cells.

### Subcellular detection (experimental)
{menuselection}`Analyze --> Cell detection --> Subcellular detection (experimental)`

Identify subcellular structures (e.g. spots of all kinds) within detected cells.

### Fast cell counts (brightfield)
{menuselection}`Analyze --> Cell detection --> Fast cell counts (brightfield)`

Fast cell counting for hematoxylin and DAB images.

### Add smoothed features
{menuselection}`Analyze --> Calculate features --> Add smoothed features`

Supplement the measurements for detection objects by calculating a weighted sum of the corresponding measurements from neighboring objects.

### Add intensity features
{menuselection}`Analyze --> Calculate features --> Add intensity features`

Add new intensity-based features to objects.

### Add shape features
{menuselection}`Analyze --> Calculate features --> Add shape features`

Add new shape-based features to objects.

### Distance to annotations 2D
{menuselection}`Analyze --> Spatial analysis --> Distance to annotations 2D`

Calculate distances between detection centroids and the closest annotation for each classification, using zero if the centroid is inside the annotation. For example, this may be used to identify the distance of every cell from 'bigger' region that has been annotated (e.g. an area of tumor, a blood vessel).

### Signed distance to annotations 2D
{menuselection}`Analyze --> Spatial analysis --> Signed distance to annotations 2D`

Calculate distances between detection centroids and the closest annotation for each classification, using the negative distance to the boundary if the centroid is inside the annotation. For example, this may be used to identify the distance of every cell from 'bigger' region that has been annotated (e.g. an area of tumor, a blood vessel).

### Detect centroid distances 2D
{menuselection}`Analyze --> Spatial analysis --> Detect centroid distances 2D`

Calculate distances between detection centroids for each classification. For example, this may be used to identify the closest cell of a specified type.

### Delaunay cluster features 2D
{menuselection}`Analyze --> Spatial analysis --> Delaunay cluster features 2D`

Apply a Delaunay triangulation to detection objects based on their centroid locations. This helps identify clusters of objects neighboring one another.

Note this command is likely to be replaced in a future version.

### Positive pixel count (deprecated)
{menuselection}`Analyze --> Deprecated --> Positive pixel count (deprecated)`

Area-based quantification of positive pixels with DAB staining. This command does not handle large regions well; if possible, pixel classification should usually be used instead.

### Simple tissue detection (deprecated)
{menuselection}`Analyze --> Deprecated --> Simple tissue detection (deprecated)`

Detect large regions using a simple thresholding method. This command is not very flexible and lacks any preview of the results; if possible, pixel classification should usually be used instead.

### Cell + membrane detection (deprecated)
{menuselection}`Analyze --> Deprecated --> Cell + membrane detection (deprecated)`

Cell detection that uses membrane information to constrain cell boundary expansion. 

This was designed specifically for hematoxylin and DAB staining, and works only where membrane staining is either very clear or absent. It is not recommended in general.

### Create density map
{menuselection}`Analyze --> Density maps --> Create density map`


### Load density map
{menuselection}`Analyze --> Density maps --> Load density map`


## Classify
### Reset detection classifications
{menuselection}`Classify --> Object classification --> Reset detection classifications`

Reset the classifications of all detections.

### Load object classifier
{menuselection}`Classify --> Object classification --> Load object classifier`

Load an existing object classifier. This can be used to apply the classifier to new objects, but not to continue training.

### Train object classifier
{menuselection}`Classify --> Object classification --> Train object classifier`  - {kbd}`Shift+Ctrl+D`

Interactively train an object classifier using machine learning. This is useful whenever objects cannot be classified based on one measurement alone.

### Create single measurement classifier
{menuselection}`Classify --> Object classification --> Create single measurement classifier`

Create a simple object classifier that applies a threshold to a single measurement.

### Create composite classifier
{menuselection}`Classify --> Object classification --> Create composite classifier`

Combine multiple classifiers together to create a single classifier by applying them sequentially.

### Set cell intensity classifications
{menuselection}`Classify --> Object classification --> Set cell intensity classifications`

Set cell intensity classifications based upon a single measurement. This is useful to calculate densities/percentages of positive cells or H-scores.

### Load pixel classifier
{menuselection}`Classify --> Pixel classification --> Load pixel classifier`

Load an existing pixel classifier. This can be used to apply the classifier to new images, but not to continue training.

### Train pixel classifier
{menuselection}`Classify --> Pixel classification --> Train pixel classifier`  - {kbd}`Shift+Ctrl+P`

Train a pixel classifier. This can be used to quantify areas, or to generate or classify objects.

### Create thresholder
{menuselection}`Classify --> Pixel classification --> Create thresholder`

Create a simple pixel classifier that applies a threshold to an image.

### Create region annotations
{menuselection}`Classify --> Training images --> Create region annotations`

Create annotations of fixed-size regions.

This can be used to select representative regions of multiple images to train (usually pixel) classifier, in combination with 'Create training image'.

### Create training image
{menuselection}`Classify --> Training images --> Create training image`

Create an image comprised of regions extracted from multiple images in a project. This can be useful for interactively training a classifier across a varied dataset.

### Create duplicate channel training images
{menuselection}`Classify --> Training images --> Create duplicate channel training images`

Duplicate an image in a project so that there is one duplicate for each channel of the image. 

This can be used to train separate classifiers for different channels in multiplexed images, which are then merged to form a composite classifier.

### Split project train/validation/test
{menuselection}`Classify --> Training images --> Split project train/validation/test`

Split images within a project into training, validation and test sets.

## Extensions
### Installed extensions
{menuselection}`Extensions --> Installed extensions`

View a list of installed QuPath extensions.

### Send region to ImageJ
{menuselection}`Extensions --> ImageJ --> Send region to ImageJ`

Extract the selected image region and send it to ImageJ.

### Send snapshot to ImageJ
{menuselection}`Extensions --> ImageJ --> Send snapshot to ImageJ`

Create a rendered (RGB) snapshot and send it to ImageJ.

### Import ImageJ ROIs
{menuselection}`Extensions --> ImageJ --> Import ImageJ ROIs`

Import ImageJ ROIs from .roi or .zip files, converting them QuPath objects

### Set plugins directory
{menuselection}`Extensions --> ImageJ --> Set plugins directory`

Set the plugins directory to use with QuPath's embedded version of ImageJ. 

This can be set to the plugins directory of an existing ImageJ installation, to make the plugins associated with that installation available within QuPath.

### ImageJ macro runner
{menuselection}`Extensions --> ImageJ --> ImageJ macro runner`

Run ImageJ macros within QuPath.

## Help
### Show welcome message
{menuselection}`Help --> Show welcome message`

Show the welcome message that appears when QuPath is first launched

### Documentation (web)
{menuselection}`Help --> Documentation (web)`

Open the main QuPath documentation website.

### YouTube channel (web)
{menuselection}`Help --> YouTube channel (web)`

Open the QuPath demo videos and tutorials.

### Check for updates (web)
{menuselection}`Help --> Check for updates (web)`

Check online for an updated QuPath release.

### Cite QuPath (web)
{menuselection}`Help --> Cite QuPath (web)`

Please cite the QuPath publication if you use the software! 
This command opens a web page to show how.

### Report bug (web)
{menuselection}`Help --> Report bug (web)`

Report a bug. Please follow the template and do not use this for general questions!

### View user forum (web)
{menuselection}`Help --> View user forum (web)`

Visit the user forum. This is the place to ask questions (and give answers).

### View source code (web)
{menuselection}`Help --> View source code (web)`

View the QuPath source code online.

### License
{menuselection}`Help --> License`

View license information for QuPath and its third-party dependencies.

### System info
{menuselection}`Help --> System info`

View system information.
