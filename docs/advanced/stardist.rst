********
StarDist
********

StarDist is a fantastic, deep-learning-based method of 2D and 3D nucleus detection from Martin Weigert and Uwe Schmidt.
It exists as a `Python library <https://github.com/mpicbg-csbd/stardist>`_ and `Fiji plugin <https://github.com/mpicbg-csbd/stardist-imagej>`_.

This page describes how to start using StarDist 2D directly within QuPath as an alternative method of cell detection.

.. admonition:: Cite the paper!
  
  If you use StarDist in a publication, be sure to cite it:
  
    * Uwe Schmidt, Martin Weigert, Coleman Broaddus, and Gene Myers. `Cell Detection with Star-convex Polygons <https://arxiv.org/abs/1806.03535>`_. *International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI)*, Granada, Spain, September 2018.
  
  (And if you use it in combination with QuPath, be sure to :doc:`cite the QuPath paper too <../intro/citing>`!)



Getting the StarDist extension
==============================

To use StarDist with QuPath, you'll need to add an extension.
You can find it with installation instructions at http://github.com/qupath/qupath-extension-stardist


Getting pretrained models
=========================

StarDist is powered by a deep learning model that is trained to detect specific kinds of nuclei.
Different models can be trained to detect nuclei within different kinds of image.

You can download three example models originally trained by StarDist's authors from https://github.com/qupath/models/tree/main/stardist

The two we will consider here are:

* *dsb2018_heavy_augment.pb* - for fluorescence images (one detection channel)
* *he_heavy_augment.pb* - for brightfield H&E (three detection channels, RGB)


.. admonition:: No TensorFlow?

  StarDist usually requires a powerful machine learning library called `TensorFlow <https://www.tensorflow.org>`_.
  This is the main reason running StarDist in QuPath v0.2 was rather complicated.
  
  As an alternative, it's now possible to run StarDist using `OpenCV <http://opencv.org>`_ instead.
  This requires that the models are in a slightly different format (*.pb* files), 
  but because OpenCV is *already* included within QuPath it makes installation 
  much easier.
  
  If you still want to use TensorFlow instead, see :ref:`stardist-advanced`.
  

.. tip::
  
  See the original StarDist papers and GitHub repos for information about training your own models.


.. tip::
  
  The *he_heavy_augment* model is capable of more than one might legitimately expect.
  
  .. figure:: images/stardist_madness_small.gif
    :class: shadow-image
    :width: 75%
    :align: center

    StarDist applied to region of OS-3.ndpi
  
  


Detecting nuclei
================

QuPath's current early StarDist support is **only available by scripting** and is rather limited in terms of reporting progress.
You can run it and... wait.

The following script applies the *he_heavy_augment.pb* StarDist model to a brightfield H&E image:

.. code-block:: groovy
  
  import qupath.ext.stardist.StarDist2D

  // Specify the model file (you will need to change this!)
  var pathModel = '/path/to/he_heavy_augment.pb'
  
  var stardist = StarDist2D.builder(pathModel)
        .threshold(0.5)              // Prediction threshold
        .normalizePercentiles(1, 99) // Percentile normalization
        .pixelSize(0.5)              // Resolution for detection
        .build()

  // Run detection for the selected objects
  var imageData = getCurrentImageData()
  var pathObjects = getSelectedObjects()
  if (pathObjects.isEmpty()) {
      Dialogs.showErrorMessage("StarDist", "Please select a parent object!")
      return
  }
  stardist.detectObjects(imageData, pathObjects)
  println 'Done!'

.. figure:: images/stardist_nuclei_os1.jpg
  :class: shadow-image
  :width: 75%
  :align: center

  StarDist applied to region of OS-1.ndpi

.. tip:: 
  
  You can copy the model directory outside QuPath (e.g. in Windows Explorer, Mac Finder) and then paste it in the script editor.
  QuPath will paste in the path to the directory.
  
  If you do this, make sure to add quotation marks around the path!


The following script applies the *dsb2018_heavy_augment.pb* model to the DAPI channel of a fluorescence image:

.. code-block:: groovy
  
  import qupath.ext.stardist.StarDist2D

  // Specify the model file (you will need to change this!)
  var pathModel = '/path/to/dsb2018_heavy_augment.pb'

  var stardist = StarDist2D.builder(pathModel)
          .threshold(0.5)              // Probability (detection) threshold
          .channels('DAPI')            // Specify detection channel
          .normalizePercentiles(1, 99) // Percentile normalization
          .pixelSize(0.5)              // Resolution for detection
          .build()

  // Run detection for the selected objects
  var imageData = getCurrentImageData()
  var pathObjects = getSelectedObjects()
  if (pathObjects.isEmpty()) {
      Dialogs.showErrorMessage("StarDist", "Please select a parent object!")
      return
  }
  stardist.detectObjects(imageData, pathObjects)
  println 'Done!'


.. figure:: images/stardist_nuclei_luca.jpg
  :class: shadow-image
  :width: 75%
  :align: center

  StarDist applied to region of *LuCa-7color_[13860,52919]_1x1*

.. tip:: 
  
  For a fluorescence image with more than one channel, the channel used for detection needs to be specified either using its number (starting from 0) or name.
  


Customizing detection
=====================

The 'builder' used in the scripts above introduce many ways to easily customize how the StarDist detection is applied and the final outputs.

One of the most important options is the ``pixelSize``, which is defined in terms of the pixel calibration units for the image (often µm, but sometimes 'pixels' if the calibration information is not available).
QuPath will automatically rescale the image as required before input to the model.

The 'best' value will depend upon the resolution of the images used to train the StarDist model.
You may need to experiment with different values.

.. tip::
  
  I find that the pretrained models work best at around 0.5 µm/pixel.


Viewing probabilities
---------------------

Another customization is to include the probability estimates as measurements for each detection.

.. code-block:: groovy
  
  import qupath.ext.stardist.StarDist2D

  // Specify the model file (you will need to change this!)
  var pathModel = '/path/to/he_heavy_augment.pb'

  var stardist = StarDist2D.builder(pathModel)
          .threshold(0.1)              // Prediction threshold
          .normalizePercentiles(1, 99) // Percentile normalization
          .pixelSize(0.5)              // Resolution for detection
          .includeProbability(true)    // Include prediction probability as measurement
          .build()

  // Run detection for the selected objects
  var imageData = getCurrentImageData()
  var pathObjects = getSelectedObjects()
  if (pathObjects.isEmpty()) {
      Dialogs.showErrorMessage("StarDist", "Please select a parent object!")
      return
  }
  stardist.detectObjects(imageData, pathObjects)
  println 'Done!'
  

These probabilities can then be visualized in QuPath through measurement tables or maps.
This can be useful to help choose appropriate threshold values; you could set a much lower detection threshold to 'over-detect' (as in the above script) and use the output probabilities to determine an appropriate cutoff threshold for the future.

.. figure:: images/stardist_nuclei_os1_prob.jpg
  :class: shadow-image
  :width: 75%
  :align: center

  StarDist with probability estimates applied to region of OS-1.ndpi
  
.. tip::
  
  In principle, you could *always* use a low detection threshold and discard false positives later.
  However, QuPath does need to work quite hard to resolve overlapping detections - and so performance should be substantially improved if you can restrict your initial detections to only cells you will want to keep.
  


Cell expansion & measurements
-----------------------------

QuPath's built-in :doc:`cell detection <../tutorials/cell_detection>` can optionally expand nuclei to approximate the full cell area, and then make measurements of different cell compartments (nucleus, cytoplasm and both).

A similar distance-based expansion can also be used with StarDist, with optional measurements.

.. code-block:: groovy

  import qupath.ext.stardist.StarDist2D

  // Specify the model file (you will need to change this!)
  var pathModel = '/path/to/dsb2018_heavy_augment.pb'

  var stardist = StarDist2D.builder(pathModel)
          .threshold(0.5)              // Probability (detection) threshold
          .channels('DAPI')            // Select detection channel
          .normalizePercentiles(1, 99) // Percentile normalization
          .pixelSize(0.5)              // Resolution for detection
          .cellExpansion(5.0)          // Approximate cells based upon nucleus expansion
          .cellConstrainScale(1.5)     // Constrain cell expansion using nucleus size
          .measureShape()              // Add shape measurements
          .measureIntensity()          // Add cell measurements (in all compartments)
          .includeProbability(true)    // Add probability as a measurement (enables later filtering)
          .build()

  // Run detection for the selected objects
  var imageData = getCurrentImageData()
  var pathObjects = getSelectedObjects()
  if (pathObjects.isEmpty()) {
      Dialogs.showErrorMessage("StarDist", "Please select a parent object!")
      return
  }
  stardist.detectObjects(imageData, pathObjects)
  println 'Done!'


.. figure:: images/stardist_cells_luca.jpg
  :class: shadow-image
  :width: 75%
  :align: center

  StarDist + QuPath cell detection and measurement

StarDist stops after nuclei have been detected; everything after that is specific to QuPath.

Nevertheless, the script above provides access to some additional features not (currently) available in QuPath's default cell detection.
These include:

* Slightly different (improved!) measurements
* Measurements also made in the predicted 'membrane'
* Extra cell expansion constraint; in addition to distance, the nucleus can be constrained so that it does not grow to more than a multiple of the nucleus size


.. warning::
  
  The cell expansion currently uses an elaborate, geometry-based method -- rather than the pixel-based approach in the built-in cell detection command.
  
  This gives much smoother results independent of image resolution, but it can produce artifacts in some (hopefully rare) cases.
  
  These artifacts are not present if StarDist is used without cell expansion.
  
  .. figure:: images/stardist_expansion_artifacts.jpg
    :class: shadow-image
    :width: 60%
    :align: center

    Artifacts to look out when using geometry-based cell expansion.



More detection options
----------------------

There are even more options available than those described above.
Here is an example showing most of them:

.. code-block:: groovy

  var stardist = StarDist2D.builder(pathModel)
          .threshold(0.5)              // Probability (detection) threshold
          .channels('DAPI')            // Select detection channel
          .normalizePercentiles(1, 99) // Percentile normalization
          .pixelSize(0.5)              // Resolution for detection
          .tileSize(1024)              // Specify width & height of the tile used for prediction
          .cellExpansion(5.0)          // Approximate cells based upon nucleus expansion
          .cellConstrainScale(1.5)     // Constrain cell expansion using nucleus size
          .ignoreCellOverlaps(false)   // Set to true if you don't care if cells expand into one another
          .measureShape()              // Add shape measurements
          .measureIntensity()          // Add cell measurements (in all compartments)
          .includeProbability(true)    // Add probability as a measurement (enables later filtering)
          .nThreads(4)                 // Limit the number of threads used for (possibly parallel) processing
          .simplify(1)                 // Control how polygons are 'simplified' to remove unnecessary vertices
          .doLog()                     // Use this to log a bit more information while running the script
          .createAnnotations()         // Generate annotation objects using StarDist, rather than detection objects
          .constrainToParent(false)    // Prevent nuclei/cells expanding beyond any parent annotations (default is true)
          .classify("Tumor")           // Automatically assign all created objects as 'Tumor'
          .build()

.. tip::
  
  In the event that you want to measure 'a ring around the nucleus' and avoid all the computational kerfuffle involved in preventing overlaps, use ``ignoreCellOverlaps(true)``.


.. _stardist-advanced:

Advanced options
================


Include preprocessing
---------------------

One of the most useful extra options to the builder is `preprocessing`, which makes it possible to perform some additional pixel operations before StarDist is used.

For example, rather than normalizing each image tile individually (as `normalizePercentiles` will do), we can normalize pixels using fixed values, for example with

.. code-block:: groovy

  var stardist = StarDist2D.builder(pathModel)
        .threshold(0.5)     // Prediction threshold
        .preprocess(        // Extra preprocessing steps, applied sequentially
                ImageOps.Core.subtract(100),
                ImageOps.Core.divide(100)
        )
  //      .normalizePercentiles(1, 99) // Percentile normalization (turned off here)
        .pixelSize(0.5)                // Resolution for detection
        .includeProbability(true)      // Include prediction probability as measurement
        .build()

Furthermore, we can use preprocessing to convert images to become more compatible with pretrained StarDist models.
For example, `dsb2018_heavy_augment.pb` works very well for fluorescence microscopy images, but only supports a single input channel.
However, by applying :ref:`color deconvolution<Separating stains>` as preprocessing we can convert a 3-channel brightfield image to a single-channel image that *looks* much more like a fluorescence image.
If needed, we can add extra things like filters to reduce noise as well.

.. code-block:: groovy

  // Get current image - assumed to have color deconvolution stains set
  var imageData = getCurrentImageData()
  var stains = imageData.getColorDeconvolutionStains()

  // Set everything up with single-channel fluorescence model
  var pathModel = '/path/to/dsb2018_heavy_augment.pb'

  var stardist = StarDist2D.builder(pathModel)
          .preprocess( // Extra preprocessing steps, applied sequentially
              ImageOps.Channels.deconvolve(stains),
              ImageOps.Channels.extract(0),
              ImageOps.Filters.median(2),
              ImageOps.Core.divide(1.5)
           ) 
          .pixelSize(0.5)              
          .includeProbability(true)    
          .threshold(0.5)             
          .build()

.. tip::
  
  These tricks were first described in `this forum post <https://forum.image.sc/t/stardist-extension/37696/6>`_.


Include classification
----------------------

StarDist can do more than simply detect nuclei: it can classify them as well.
There is an example notebook `here <https://github.com/stardist/stardist/blob/master/examples/other2D/multiclass.ipynb>`_ that describes how to train a model capable of both detection and classification.

The QuPath StarDist extension can use these models as well.
It only requires a change to input a map linking StarDist prediction labels to QuPath classifications.

.. code::

  // Define model and resolution
  var pathModel = "/path/to/classification/model.pb"
  double pixelSize = 0.5
  
  // Define a classification map, connecting prediction labels and classification names
  var classifications = [
      0: 'Background',
      1: 'Stroma',
      2: 'Tumor'
  ]

  var stardist = StarDist2D.builder(pathModel)
          .threshold(0.5)              
          .simplify(0)
          .classificationNames(classifications) // Include names so that classifications can be applied
          .keepClassifiedBackground(false)      // Optionally keep detections that are classified as background (default is false)
          .normalizePercentiles(1, 99) 
          .pixelSize(pixelSize)
          .build()

  // Run detection for the selected objects
  var imageData = getCurrentImageData()
  var pathObjects = getSelectedObjects()
  if (pathObjects.isEmpty()) {
      Dialogs.showErrorMessage("StarDist", "Please select a parent object!")
      return
  }
  stardist.detectObjects(imageData, pathObjects)
  println 'Done!'


.. tip::
  
  QuPath will attempt to untangle where the classifications are in the outputs of the model.
  For this to work, the number of rays predicted by StarDist should be greater than the number of distinct classifications.


Use TensorFlow
--------------

It is still possible to use StarDist with TensorFlow rather than OpenCV.
See the `QuPath TensorFlow Extension <http://github.com/qupath/qupath-extension-tensorflow>`_ for details and installation instructions.

You will need alternative pretrained models in TensorFlow's *SavedModel* format.
Unzipped examples from the `stardist-imagej repository <https://github.com/stardist/stardist-imagej/tree/master/src/main/resources/models/2D>`_ should work.

You will also need to give QuPath the path to the *folder* containing the model files in this case, e.g.

.. code-block:: groovy

  var pathModel = '/path/to/dsb2018_heavy_augment' // A folder, not a file



Use CUDA
--------

If you have a recent NVIDIA graphics card, you *might* benefit from running StarDist using CUDA.
This is possible with both OpenCV and TensorFlow -- although I have found it easier to set up with OpenCV.

To do this, build QuPath from source as described in :ref:`building-gpu`.
If your GPU-friendly build of QuPath is able to detect CUDA support through OpenCV, it will be used automatically.



Differences from StarDist Fiji
==============================

While inspired by the Fiji plugin, the QuPath implementation does not use any of the same code - and the method has been adapted and augmented in several ways to be more QuPath-friendly.
These include:

* More customization options (e.g. specifying resolution, input channels)
* Cell boundary estimation by expansion
* Adding measurements (including prediction probabilities)

Another difference is in how overlapping nuclei are handled.
The Fiji plugin allows overlaps, controlled with an overlap threshold parameter.

QuPath does not permit overlapping nuclei.
Rather, it handles overlaps by retaining the nucleus with the highest prediction probability unchanged, and removing overlapping areas from lower-probability detections - discarding these detections only if their area decreases by more than 50%.
