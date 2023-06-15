# View tracker

## What is the view tracker?

View tracking in QuPath is the feature that allows you to
record the actions done in the main viewer. In other words, a view recording
can be seen as a chronological table retracing what part of your image
was being viewed at a certain time (and possibly more):

| Timestamp | X   | Y   | Width | Height | Canvas Width | Canvas Height | Downsample | Rotation |
| --------- | --- | --- | ----- | ------ | ------------ | ------------- | ---------- | -------- |
| 0         | 0   | 50  | 150   | 150    | 150          | 150           | 1          | 0        |
| 33        | 50  | 50  | 150   | 150    | 150          | 150           | 1          | 0        |
| ...       | ... | ... | ...   | ...    | ...          | ...           | ...        | ...      |

Where:
* **Timestamp** is the time at which the frame was recorded
* **X**, **Y**, **Width** and **Height** are the image bounds
* **Canvas width** and **Canvas height** are the size of the viewer\'s window
* **Downsample** is the downsample at which the frame was viewed (useful for pyramidal images)
* **Rotation** is the rotation in gradian at which the image was viewed

## How to use view tracker?

### The view tracker

View tracking is accessible through {menuselection}`View --> Show view tracker`. A
small window, such as the one below, will show:

:::{figure} images/tracker_viewer_recording_example.png
:align: center
:class: shadow-image
:width: 40%

View tracker window including an example record
:::

All the recordings of the currently opened image are listed there, as
well as in the project folder (in the current image\'s folder, under
\'recordings\').

### Create a recording

To start a new recording of the viewer, simply click the button. To stop
the recording, click the button. After stopping a recording, QuPath will
automatically save it as a TSV file in the project folder.

:::{tip}
You can also add mouse tracking and active tool tracking to the
recording by clicking on the more button ().
:::

### Play a recording back

You can replay any selected recording by clicking the button and stop
the replay by clicking on the button.

::: {warning}
A recording can only be made for one viewer at a time. I.e. You cannot
jump from one viewer to another during a recording, even in multi-view.
Doing so will simply stop the current recording.
:::

## How to analyze a recording?

### Analysis pane

To analyze a recording, select it and click `Analyze`{.interpreted-text
role="guilabel"} (or alternatively, double-click on the recording). This
will bring up the analysis pane, as shown below.

:::{figure} images/tracker_viewer_recording_example.png
:align: center
:class: shadow-image
:width: 40%

View tracker window including an example record
:::

There you will be presented with a slide overview of the current image.
You can then play the recording back or move the slider along to jump to
a specific frame.

### Data overlay

On ticking `Enable data overlay`,
QuPath will display on top of the opened image (and the slide overview
in the same pane) an overlay representing the time (in milliseconds)
spent on each region of the image. In other words, each pixel of the
overlay represents the amount of milliseconds spent on the corresponding
pixel of the original image.

You can dynamically crop the recording to display only the data from a
certain period of the recording by sliding the `Time range` slider
(e.g. only the frames between 5 minutes and before 10 minutes).
Similarly, you can dynamically crop the recording to only display the
data from the frames which were captured in a specified downsample range
(e.g. only the frames where the image was viewed as full resolution).

::: {tip}
You can export the overlay to a `tif` file by right-clicking
on the slide overview (after making sure that
`Enable data overlay` is ticked),
then `Export data as TIF`.
:::

### Recording table

As mentioned above, all recordings are automatically saved as a TSV file
in the project folder. You can preview this table by clicking
`Show frames` (and `Hide frames` to collapse them).

::: {note}
Selecting a recording from the previewed table will automatically change
the position of the current viewer to match the frame selected.
:::
