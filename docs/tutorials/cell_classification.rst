********************
Cell classification
********************

.. include:: ../tools.txt

.. warning::
  The original version of this tutorial was written for QuPath v0.1.2.
  
  Object classifiers in QuPath v0.2.0 have been updated, and this tutorial will soon be replaced.
  In the meantime, there is some further information about the new classifiers in :doc:`Multiplexed analysis <multiplex_analysis>`.

:doc:`cell_detection` looked at computing Ki67 labelling indices by counting positive and negative cells within user-defined regions of interest.
These regions had to be drawn very carefully to try to ensure that they only included tumor cells, and excluded other cell types that should not contribute to conventional scoring of Ki67.

This section builds upon this by showing how QuPath can be trained to be able to distinguish between different cell types itself.
This provides an alternative method of analysis that avoids the requirement to laboriously draw around every region that should be scored.
Instead, all cells can be detected, and then QuPath can be requested to calculate scores based only on the cells that are relevant for the application - automatically identifying and excluding the others.

As before, the concepts described in this section are general within QuPath.
They can be applied for the *classification* of all *detections* within QuPath, and not only for classifying different cell types.

.. note::
    It is a good idea to read through the :doc:`cell_detection` section before this one.


Create annotation around main region of interest
================================================

The first step is to draw a generous annotation that corresponds to a region of interest within which cells should be detected.
This can be done very quickly, and should include a mixture of both tumor and non-tumor cells for the classification to be meaningful.

.. note::
    Although it is possible to create an annotation for the entire image using :menuselection:`Objects --> Create full image annotation`, this is not really advisable.
    It will lead to a lot of unnecessary processing and memory use within areas of the image that are not relevant.

    :menuselection:`Analyze --> Preprocessing --> Simple tissue detection` is another possible alternative, but is also likely to result in more processing being performed than necessary.

.. figure:: images/ki67_auto_original.jpg
  :class: shadow-image
  :width: 75%
  :align: center

  Ki67 image


Run *Cell detection* command
============================

With the annotation selected, the :menuselection:`Analyze --> Cell analysis --> Cell detection` command can be used to detect cells.

.. note::
  In :doc:`cell_detection`, the :menuselection:`Analyze --> Cell analysis --> Positive cell detection` command was used instead.

  It does not really matter which command is applied in this case.
  *Positive cell detection* does exactly the same thing as *Cell detection*, but has the extra step of classifying all cells as positive or negative immediately according to DAB staining intensity.
  This is most useful if all detected cells should be considered the same.

  Since in this case we need to classify cells as tumor or non-tumor first, we will postpone considering staining intensity until the end, whenever we know the cell types.
  Therefore there is no need to look at consider staining intensity now, and therefore I have used the slightly-simpler *Cell detection* command.

If the annotation is large enough, QuPath will break it into smaller regions that it can process in parallel.
This improves the speed and reduces the memory requirements.
In this case, QuPath will overlap the regions and then try to resolve cells detected on region boundaries to avoid weird artefacts in these areas (e.g. cells being cut in half, or detected twice).

.. figure:: images/ki67_auto_parallel.jpg
  :class: shadow-image
  :width: 75%
  :align: center

  Ki67 parallel cell detection

The resulting cell detection is shown below.

.. figure:: images/ki67_auto_cells_detected.jpg
  :class: shadow-image
  :width: 75%
  :align: center

  Detected cells


View cell measurements (if you want)
====================================

QuPath's ability to distinguish between different cell types depends upon which measurements have been made.

One way to view the measurements is by generating a results table, as described in :doc:`cell_detection`.

.. figure:: images/ki67_auto_results_detections.jpg
  :class: shadow-image
  :width: 75%
  :align: center

  Results table showing cell features

However, another way to visualize cell measurements is by using the :menuselection:`Measure --> Show measurement maps` command.

This creates a kind of 'heatmap' visualization, in which each cell is color-coded according to its value for a particular measurement.
The measurement can be selected from a list, and sliders can be used to adjust how colors are mapped to measurement values.

A particularly useful measurement for the purposes of tumor cell identification is the *Nucleus/Cell area ratio*.
This tends to be higher for tumor cells, because tumor nuclei tend to be larger than non-tumor nuclei, and more densely packed.
The *Nucleus/Cell area ratio* incorporates both of these characteristics in a single measurement.

.. figure:: images/ki67_auto_map_raw.jpg
  :class: shadow-image
  :width: 75%
  :align: center

  Measurement map for Nucleus/Cell area ratio


Calculate additional features
=============================

Despite the usefulness of *Nucleus/Cell area ratio* for identifying tumor cells, on its own it is not enough.
One reason is that dense populations of immune cells can also have high values for this measurement.
Ultimately we will need to rely upon combinations of measurements.

Another reason for the limited usefulness of the *Nucleus/Cell area ratio* is that the measurement is rather 'noisy'.
This can be seen in the image above, where overall tumor cells have higher values (i.e. more red in areas of tumor), but there is considerable variation on a cell-by-cell-basis.

Therefore, to help QuPath perform an accurate classification it is useful to supplement the existing measurements of individual cells with some additional features that take into consideration more contextual information.

Some commands that enable this are found in the :menuselection:`Analyze --> Calculate features` menu.
One approach is to calculate textures from the image surrounding each cell.
This can be very effective, although computationally quite demanding whenever there are very large numbers of cells.

A much faster alternative, which can give very good results, is to simply 'smooth' the existing measurements with the :menuselection:`Analyze --> Calculate features --> Add smoothed features` command.
This will supplement the existing measurements with new measurements calculated by taking a weighted average of the corresponding measurements of neighboring cells.

The weighting depends on distance, i.e. cells that are further away have less contribution to the result.
Technically, distance is based on centroids and the weighting is calculated from a Gaussian function, where the parameter required in the dialog box is the `full-width-at-half-maximum <https://en.wikipedia.org/wiki/Full_width_at_half_maximum>`_ of the Gaussian function.
Less technically, putting higher numbers into the dialog box results in more smoothing.
This reduces the noisiness of the measurements more effectively, but also makes it more difficult to distinguish smaller areas containing particular cell types.

.. figure:: images/ki67_auto_smooth_features.jpg
  :class: shadow-image
  :align: center

  Smooth features dialog

After applying smoothing with the parameters shown above, clicking *Update map* within the *Measurement map* dialog causes the new measurements to appear.
The smoothed version of *Nucleus/Cell area ratio* is shown below.
Again, more red is seen in areas of tumor - but now these are much more homogeneous.
This will help QuPath to identify all the cells within tumor areas correctly.

.. figure:: images/ki67_auto_map_smoothed.jpg
  :class: shadow-image
  :width: 75%
  :align: center

  Measurement map for smoothed Nucleus/Cell area ratio


Annotate regions containing different cell types
================================================

The next step is to begin annotating regions according to how the cells contained within them should be classified.

This requires creating annotations as normal, using any of the tools (apart from the *Line*) described in :doc:`../starting/annotating`.
It does not matter whether the cells are shown or hidden on the image at the time; it can be helpful to toggle the detections on and off with the *Show/hide detection objects* command |icon_detections| while annotating.

After an annotation has been drawn, select the *Annotations* tab in the *Analysis pane* to the left, click on the appropriate classification from the list on the top right, and press the *Set class* button.
You should see the number increase beside the class that you selected.
This is the number of cells inside all the annotations that you have drawn and assigned to this class.

.. note::
    Double-clicking on the list of classification allows you to change their colors, while right-clicking brings up more options (including to add new classifications).

.. figure:: images/ki67_auto_training_first.jpg
  :class: shadow-image
  :width: 75%
  :align: center

  Training cell classification

Continue creating annotations and assigning their classes.
Right-clicking on the image after drawing the annotation can offer an easier way to set the class, without needing to move the mouse to the other side of the screen and press the *Set class* button on the left.

.. figure:: images/ki67_auto_training_tumor.jpg
  :class: shadow-image
  :width: 75%
  :align: center

  Training cell classification with right-click


Train a cell classifier based on annotations
============================================

Once you have several annotations with different classes, it is time to create the classifier to see how well QuPath can distinguish the cells.

To do this, go to :menuselection:`Classify --> Create detection classifier`.
Pressing *Build & Apply* will train up a classifier that QuPath will then apply to all cells within the image.
If your computer is sufficiently fast, or your number of annotations sufficiently small, the *Auto-update* button can do the same - and will result in the classifier immediately updating as you draw more annotations and set their classes.

.. TIP::
    The default *Random Forest* classifier tends to get a good combination of speed and accuracy - although you can choose others if you wish.

Under *Advanced options*, you can also select exactly which measurements you want to be used for the classification, and adjust several other parameters.
By default, all measurements that are available when the classifier is first built will be used.
If you add extra measurements later (e.g. by running *Add smoothed features* again with different settings), then you will need to go into *Advanced options* and choose *Select...* to ensure that the new measurements are included.

.. figure:: images/ki67_auto_training_updated.jpg

  Training cell classification with preview


Interactively improve classification performance
================================================

Continue to add annotations and set their classes in areas that QuPath gets 'wrong', until you are satisfied with the performance.

An extra tip: holding down shift while right-clicking on the image provides a third way to set the class of an annotation that is selected, by opening a small 'ring' menu.

.. figure:: images/ki67_auto_training_ring.jpg
  :class: shadow-image
  :width: 75%
  :align: center

  Training cell classification with shift + right-click


Apply intensity classification
==============================

Once you are satisfied with QuPath's ability to identify tumor cells, it is now time to apply DAB staining intensity classification.
Because the scoring of tumor cells is a common application, there is an option to do this directly within the classifier dialog box.
Here, select *Nucleus: DAB OD mean* as the feature used for the intensity classification.
Also, make sure that *Use single threshold* is selected and then adjust *Threshold 1+* until the resulting positive/negative sub-classification of tumor cells matches with the brown vs blue appearance of the nuclei within the image.

.. figure:: images/ki67_auto_training_intensity.jpg
  :class: shadow-image
  :width: 75%
  :align: center

  Intensity classification

.. note::

  If you want to update the intensity classification threshold later, without needing to go through the whole detection classification thing, you can use this one-line script:

  .. code-block:: groovy

    setCellIntensityClassifications("Nucleus: DAB OD mean", 0.2)

  This script also works if you are assigning up to 3 thresholds (e.g. to calculate an H-score), e.g.

  .. code-block:: groovy

    setCellIntensityClassifications("Nucleus: DAB OD mean", 0.2, 0.4, 0.6)

  For more thoughts and tips on assigning intensity-based classifications, see `this blog post <https://petebankhead.github.io/qupath/tips/2018/03/22/setting-positive.html>`_.


View the results
================

That's it!  If you select the original, large annotation containing all the cells then the Ki67 labelling index show appear in the lower measurements section of the *Annotations* tab on the left of the screen as *Positive %*.
You can also generate results tables if necessary.

.. figure:: images/ki67_auto_final_markup.jpg
  :class: shadow-image
  :width: 75%
  :align: center

  Ki67 analysis results with cell classification

If you are likely to want to apply the classifier again to different images, you can also save this by clicking the *Save classifier* button at the bottom of the classifier window.
The next time you open a similar image, you can run the cell detection and feature calculations as before, and then apply your pre-trained classifier with :menuselection:`Classifier --> Load classifier`.
See also the :doc:`../scripting/index` section for more information about how to batch process larger numbers of images in a reproducible way.
