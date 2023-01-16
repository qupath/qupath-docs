(first-steps)=
# First steps

The following tutorial will guide you through your first steps with QuPath, and introduce you to the main features, buttons and concepts you need to get started.
You will see how to:

- QuPath Welcome window
- Open a whole slide image
- View image properties
- Navigate around images
- Manually annotate regions
- Detect cells
- View measurements
- Export results
- Save & reload your data

## Starting out

:::{note}
If you do not have a whole slide image handy, see {doc}`here <../intro/acknowledgements>` for examples.
:::

### Opening QuPath
Running QuPath for the first time will present you with the welcome window. This contains useful links should you have an issue or want to learn more. 

For those that like working on software in dark mode or want to use their own creative themes it's possible to change that here. Additionally updates to the software can also be checked ensuring you have access to the latest features. 

:::{figure} images/steps_welcome.jpg
:align: center
:class: shadow-image
:width: 75%

QuPath welcome window.
:::

:::{Tip}
Should you no longer want to see this pop-up, it can be deselected at the bottom right corner and will remain hidden until reactivated in settings under {menuselection}`Edit --> Preferences -> general -> Show welcome message when QuPath starts`.
:::

### Opening an image

You can open an image with {menuselection}`File --> Open...`, but that quickly becomes tiresome.

A better plan is to simply drag the file you want to open onto QuPath's main window, and let QuPath do the rest.
This works for most other file types that QuPath can handle - not only images.

:::{figure} images/steps_image.jpg
:align: center
:class: shadow-image
:width: 75%

A whole slide image (*CMU-1.svs*) opened within QuPath.
:::

### Setting the image type

One of the most important properties is the **Image type**, which can impact the behavior of some QuPath commands. When opening an image in QuPath you will be presented with a window allowing you to choose the image type. You should choose the closest match for the image, e.g. *Brightfield*, *Fluorescence*.

:::{figure} images/steps_image_type.jpg
:align: center
:class: shadow-image
:width: 75%

Option window for setting the image type in QuPath.
:::

:::{important}
QuPath can automatically estimate the image type for you, if you choose this option for *Set image type* in under {menuselection}`Edit --> Preferences...` {{ icon_cog }}.
However, in case the estimate is wrong you should be aware the option exists - and should always be checked.
:::

:::{tip}
Should you need to change the image type retrospectively, it's possible to do so in the **Image** tab within the **Analysis panel** mentioned below.
:::

### Seeing the image properties

Usually, there's a panel on the left of the QuPath window: the **Analysis panel**.
If not, click the **Analysis panel** button on the toolbar to open it {{ icon_measure }}.

There are a few tabs here that you will meet later.
For now, click the **Image** tab to get a table of properties related to your image.

:::{figure} images/steps_image_tab.jpg
:align: center
:class: shadow-image
:width: 75%

Image tab showing the image properties in QuPath.
:::

### Setting the pixel size

The pixel size is used extensively by QuPath. This is why it is good practice to make sure it's correct.

If stored in the image file, QuPath should automatically fetch the pixel size and display it under the **Image** tab ('Pixel width' & 'Pixel height').
If not, you can set the pixel size manually by double-clicking on either row and type the correct values.

:::{Tip}
You can also set the pixel size based on a specific region of your image.
To do so, create an annotation around the region then double-click on either 'Pixel width' or 'Pixel height' under the **Image** tab to type its size in micron squared.

You can also draw a line annotation (if you want to make it perfectly horizontal or vertical, hold down the {kbd}`Shift` key) and do the same steps, typing the length in micron instead of the area.
:::

## Looking around

### Zooming in & out

To **zoom in and out** of an image within QuPath, use the **scroll wheel** of your mouse (or equivalent scrolling motion on a trackpad).

You can also jump to a specific magnification if you:

- *Right-click* on the image, and choose one of the zoom options e.g. {menuselection}`Display --> 100%`, or
- *Double-click* on the little magnification box on the toolbar, and enter a value there.

:::{figure} images/steps_mag.jpg
:align: center
:class: shadow-image

The *Magnification box*
:::

Double-clicking on the magnification value in the toolbar (here, the bit that shows 10.0x) opens an input dialog to enter a specific magnification.

### Panning

To **pan** around a large image within QuPath, first make sure that the **Move** tool {{ icon_move }} is selected in the toolbar.
Then click anywhere on the image, and drag the mouse with the button held down to move.

Alternatively, you can click on the **Overview image** in the top right to automatically jump to a specific region.

:::{figure} images/steps_overview.jpg
:align: center
:class: shadow-image
:width: 75%

The *Image overview (top right) can be used for navigation*.
:::

:::{note}
For other methods to navigate large images - including multitouch support for touchpads, touch-sensitive screens and 3D mice - see {doc}`viewing`.
:::

(introducing-objects)=
## Introducing objects

Understanding **objects** is key to making sense of QuPath's features.

You can think of an **object** informally as *something in an image that QuPath can identify, classify and measure*.

For now, we only care about two kinds of objects:

- **Annotations**: Objects that you usually create yourself, by drawing on the image
- **Detections**: Objects that QuPath usually creates for you, e.g. by detecting cells (where each cell is an object)

Usually, you end up with a small number of annotations relating to larger regions (e.g. entire areas of tissue).
But you can have potentially millions of detections.
So for this reason QuPath handles and displays them a bit differently - but they also share a lot of similarities, in that you can see them both drawn on top of images and measure.

:::{note}
For a purely manual analysis - drawing regions on an image and measuring them - you may find that you don't need detections at all... annotations are enough.

For a deeper discussion of objects and why they matter so much, see {doc}`../concepts/index`.
:::

### Drawing annotations

Create your first **annotation object** by drawing a rectangle on top of the image.
Do this by clicking on the **Rectangle tool** {{ icon_rectangle }} to select it, then click and drag over a region in the image.
When releasing the mouse button, the rectangle should remain drawn on top of the image.

Now try drawing several more annotations of different shapes around different areas in the image using the **Ellipse** {{ icon_ellipse }}, **Polygon** {{ icon_polygon }} and **Brush tools** {{ icon_brush }}.

Most of QuPath's drawing tools work similarly (i.e. select the tool, click on the image, drag the mouse), but note that the polygon tool also allows you to eschew dragging and instead click each point where you want a vertex on the polygon.
Double-click to set the final point.

:::{note}
By default, QuPath will switch back to the **Move tool** {{ icon_move }} after you've drawn an annotation with any tool except the **Brush**.
This is to avoid accidentally drawing new annotations when you really just wanted to move around in the image or do something with an existing annotation.
The **Brush** is different, because it's commonly used to paint or edit multiple regions at a time, and it can be annoying to have to switch it back on regularly.

If you don't like the default behavior, it can be changed with the *Return to Move Tool automatically* option in the **Preferences** {{ icon_cog }}.

Either way, you can quickly activate the tool you want using a shortcut key, e.g. just type {kbd}`M` for **Move**, {kbd}`B` for **Brush**, {kbd}`P` for **Polygon** etc.
You can see all the shortcut keys for drawing tools under the **Tools** menu.

Since QuPath version 0.4, you can also click the middle button (or scroll wheel) on your mouse to quickly toggle between **Move** and the last drawing tool you were using.
:::

:::{figure} images/steps_annotations.jpg
:align: center
:class: shadow-image
:width: 75%

Rectangle, ellipse and polygon annotation objects drawn on an image.
:::

### Identifying selections

You should find that when you draw an annotation object, it is initially selected.
In the screenshot above, the selected (polygon) annotation is shown in **yellow** - with little square handles indicating vertices that could be adjusted if necessary.

Usually, you want to make sure an object is selected before you can do something with it.
If the object you want isn't selected already, return to the **Move tool** {{ icon_move }}, either by clicking on the tool button or pressing **M**, and then double-clicking on it to select it.

:::{tip}
By default, selections are shown in yellow.
You can change this color under {menuselection}`Edit --> Preferences...` {{ icon_cog }}.
You can also turn off using a selected color, in which case QuPath will look for another way to show you whether an object is selected, e.g. with thicker outlines or drawing a box around it.
:::

:::{tip}
You can select multiple annotations by clicking on them while holding down the {kbd}`Alt` key.
:::

### Changing colors & properties

Return now to the **Analysis panel** (left of the screen, {{ icon_measure }} and click on the **Annotations** tab.

% warn:
% In earlier QuPath versions, the tab to select was called **Objects**... which is why the screenshot is different.

You should see a list of your annotations here.
Clicking on this list gives another way to select an object.
But you can also set the properties of your annotations here if you like.
One way is to select from a predefined list of classifications on the right, and choose **Set class**.
Alternatively, right-click on any listed annotation and choose **Set properties** to choose any arbitrary name or color.
You can toggle on and off the visibility of annotation names with {kbd}`N`.

:::{Tip}
You can also set an annotation's properties by selecting it and hitting *Enter*.
:::

:::{figure} images/steps_annotation_panel.jpg
:align: center
:class: shadow-image
:width: 75%

The *Annotations tab*
:::

### Viewing measurements

Still in the **Analysis panel**, below the annotation list you should see a table showing measurements for the currently selected object.
This should update automatically if you click on another annotation.

### Removing annotations

If you draw an annotation you don't like, you can delete it from the annotation list.
Alternatively, if you're currently working inside the viewer (moving around, drawing annotations) you can simply press the {kbd}`Backspace` or {kbd}`Delete` key to remove the currently selected objects.

:::{note}
Mostly, this should 'just work'.
But if you are **deleting an object that contains other objects inside it**, then QuPath will ask you if you want to *'Keep the descendant object(s)'*.

- If you click *Yes* (or press *Enter*), only the selected object will be removed.
- If you click *No*, then both the selected annotation and all the objects inside it will be removed.
- If you click *Cancel*, nothing will be removed.

For more information on the strange use of the word *descendant*, see {doc}`../concepts/object_hierarchy`.
:::

### Detecting cells

Next, try creating detection objects inside an annotation.
First, draw an annotation in an area of the image containing cells - ideally quite small, to contain perhaps 100 cells.

Run the {menuselection}`Analyze --> Cell analysis --> Cell detection` command.
This should bring up an intimidating list of parameters to adapt the detection to different images.
If you like you can explore these, and hover the mouse over each parameter for a description - but for now, you can also just ignore them and use the defaults (which tend to behave sensibly across a range of images).

:::{figure} images/steps_cell_detection.jpg
:align: center
:class: shadow-image
:width: 75%

Adjustable parameters for cell detection
:::

Press the **Run** button at the bottom of the dialog.
After a few seconds, cells should appear in the area you have selected.

These cells are your first **detection objects**.

:::{figure} images/steps_cells_detected.jpg
:align: center
:class: shadow-image
:width: 75%

First detected cells, using default detection parameters.
:::

:::{note}
Detection objects also have measurements, like annotation objects.

You can select them, and their measurements show up in the same table in the **Analysis panel**.
But you should see that detection objects look a bit different on screen.
For example, if you zoom out to a low magnification, you should see annotations are still clearly visible, drawn with thick lines.
However detections get smaller, their outlines get thinner, and they start to merge into one another.

This is because annotations and detections serve different purposes.
Detections relate to small structures, such as cells or nuclei, of which you can easily end up with hundreds of thousands - or even millions - within a single image.
You need to zoom in to see them.
However you will generally have a much smaller number of annotations - each related to quite a large area - and you need to be able to see them when zoomed out.

The pattern we applied here here is common in QuPath:

> - Create an annotation (usually by drawing it)
> - Run a command to get QuPath to detect objects inside the annotation

In case this seems horribly manual, be assured that it's possible to get QuPath to detect across many annotations simultaneously - and even to create annotations automatically.
Just not in Lesson #1.
:::

### Showing & hiding

As your collections of objects grow on the image, it may start to become cluttered or confusing.
There are four useful toolbar buttons that can help customize how the objects are displayed. These are:

- {{ icon_annotations }} **Show and hide annotations** - shortcut {kbd}`A`
- {{ icon_tma_grid }} **Show and hide a TMA grid** (only relevant for \[\[Tissue microarrays\]\]) - shortcut {kbd}`G`
- {{ icon_detections }} **Show and hide detections** - shortcut {kbd}`D`
- {{ icon_detections_fill }} **Fill and unfill detections** - shortcut {kbd}`F`

These allow you to quickly toggle on and off your markup to switch between looking at analysis data and the underlying image.

You can also right-click on the image, and further modify how cells are displayed, i.e. with/without nuclei or boundaries shown.

:::{figure} images/steps_cells_display.jpg
:align: center
:class: shadow-image
:width: 75%

Right-click on the image to change how cells are displayed.
:::

### Creating measurement tables

You can generate a results table containing measurements for your objects by selecting the **Table** button in the toolbar {{ icon_table }}.
You can then choose whether you want your table to contain annotations or detections.

Note that this table remains connected to the image, and allows you to select individual objects, or sort by columns.
You can also generate histograms for any measurements, and save the table to a CSV file or copy its contents for pasting into another application, e.g. Excel.

:::{figure} images/steps_table.jpg
:align: center
:class: shadow-image
:width: 75%

A 'detection' measurement table containing details of all the detected cells.
:::

## Finishing up

### Saving data

When you're done, you can save your analysis with {menuselection}`File --> Save As...`, or by responding positively to any saving prompts whenever you try to open another image or to quit.

This will save a `.qpdata` file, which is QuPath's primary file format for storing objects and other image-related data.
Note that this *does not* actually store the image itself (which may be huge), but rather only a link to it.

:::{tip}
It is **strongly recommended** to use {doc}`Projects <../tutorials/projects>` rather than saving `.qpdata` files individually.
:::

### Reopening data

In most cases, you can reopen `.qpdata` files in the same way as you could open any image - by dragging it onto the QuPath viewer, or by choosing {menuselection}`File --> Open`.

It's not necessary to open your image again first.
If your original image remains where it was, the link within the `.qpdata` file will be used to open it automatically.
However if the image has been moved, QuPath will show a dialog prompting you to select the new image location.

:::{warning}
I say 'in most cases', because some images you can work with in QuPath are more complicated than the contents of a single file.
In such cases, the `.qpdata` file alone doesn't contain enough information - that's why you should really embrace {doc}`Projects <../tutorials/projects>` soon.
:::

## Recap & outlook

If you got this far, great!  You've seen many of the main features of QuPath, and had your first encounter with the fundamental idea of working with objects.

Even if not everything is clear yet, hopefully it gives enough motivation to read on through the documentation and see how powerful these ideas can become when put together.
