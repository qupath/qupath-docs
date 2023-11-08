(wsinfer-extension)=
# WSInfer

The [WSInfer QuPath extension](https://github.com/qupath/qupath-extension-wsinfer/) makes it possible to do patch-based deep learning inference for digital pathology, without any need for scripting.

It's a collaboration between the QuPath group (the extension) and Stony Brook University ([WSInfer](https://wsinfer.readthedocs.io/en/latest/)).

:::{admonition} Cite the paper!
:class: warning
If you use WSInfer and/or this extension in a publication, please make sure to cite our preprint at <https://arxiv.org/abs/2309.04631>
:::

## Requirements

- QuPath [version 0.4](https://qupath.github.io/) (installation instructions [here](https://qupath.readthedocs.io/en/0.4/docs/intro/installation.html)).
- At least one whole slide image
- [WSInfer QuPath Extension](https://github.com/qupath/qupath-extension-wsinfer/releases)
- PyTorch (this can be downloaded while using the extension)

A GPU is not required but will dramatically speed up processing. WSInfer uses Deep Java Library, so if you have a GPU and need guidance configuring support, please see [the Deep Java Library page](deep-java-library-gpu).

## Set-up

With QuPath installed and running, drag and drop the WSInfer extension into the application and restart QuPath.
Once installed, open up an image and run the extension via {menuselection}`Extensions --> WSInfer`.
You should see the window below:

:::{figure} images/wsinfer.png
:align: center
:class: shadow-image
:width: 40%

The WSInfer user interface
:::

:::{note}
Please note that you'll need internet access to start the extension and download the models.
:::

## Whole Slide Inference

### 1. Select a model

Select the a model from the dropdown menu and click the download icon button to start the download.
You should see a notification when the download is complete.

### 2. Create or select an annotation

Create an annotation or select a pre-existing annotations/tiles you wish to run the model on.
It's recommended that if this is the first time running WSInfer to keep the annotation smaller to test the processing speed before running it on a larger region.
This might take some time, depending on your computers processing speed.

:::{admonition} Select tiles or annotations?
WSInfer assign classifications to [tile objects](concepts-tiles).

Most of the time, you should draw/select annotations on the image before running WSInfer.
The WSInfer extension will then create the tiles that it needs.

The size of the tiles created automatically will match the size of the patch WSInfer is using to for inference.
That's why the tile sizes generated for different models can be different: it depends what size of patch was used to train the model.

*Sometimes* you might want to reuse existing tiles, and append the measurements made by WSInfer to them.
This is especially useful if you want to run WSInfer multiple times using different models.
This is why there is also an option to select tiles, as an alternative to selecting annotations.

When you do that, WSInfer won't create new tiles - *but it will still use patches based on the resolution and patch size used to train the model*.
These patches don't necessarily have to correspond exactly to the tiles shown in QuPath - they might be bigger or smaller - but they should still be centered on the same pixels.
:::

### 3. Run

Check you have an annotation selected and click run and if all the requirements are present then the processing will begin.
If you don't have PyTorch yet, you will be prompted to download it (this may well be > 100 MB, so may take a while).

### 4. View Results

Once the progress bar is complete the results can be visualized using the tools in the {guilabel}`View Results` section.

The {guilabel}`Measurement Maps` tool presents the score of each tile by color and can be interacted with using the 3 toggle buttons to either show, hide or fill the annotations and detections.

The slider can be used to increase or decrease the fill opacity so the tissue features can be seen under the WSInfer scores.

The {guilabel}`Results Table` provides details for each tile and the option to export for further analysis.

## Additional Options

You can also use the additional options to specify where models should be stored, and also the number of parallel threads used to read patches from the image (usually 1 or 2).

:::{figure} images/wsinfer_options.png
:align: center
:class: shadow-image
:width: 40%

WSInfer's additional options
:::

However the most (potentially) exciting additional option is the {guilabel}`Preferred device`: the one that promises to (maybe) make things run much faster.

The options available will depend upon your computer's capabilities (at least as far as they could be discerned by Deep Java Library):

* **CPU**: This is generally the safest - and slowest - option, because it should be supported on all computers.
* **MPS**: This stands for *Metal Performance Shaders*, and should be available on recent Apple Silicon - it is the Mac version of GPU acceleration
* **GPU**: This should appear if you have an NVIDIA GPU, CUDA... and a little bit of luck.

If either MPS or GPU work for you, they should reduce the time required for inference by a *lot*.
However configuration for GPU can be tricky, as it will depend upon other hardware and software on your computer.

QuPath v0.4.x uses PyTorch 1.13.x by default, which is expected to work with CUDA 11.6 or 11.7.
For more info, see [the Deep Java Library page](deep-java-library-gpu).

:::{admonition} PyTorch & CUDA versions
:class: tip

The WSInfer extension is using Deep Java Library to manage its PyTorch installation.
It won't automatically find any existing PyTorch you might have installed: Deep Java Library will download its own.

If you have a compatible GPU, and want CUDA support, you'll need to ensure you have an appropriate CUDA installed *before* PyTorch is downloaded.
:::


## Scripting

The QuPath WSInfer extension is scriptable, which makes it much easier to apply across multiple images.

When a model is run, the command parameters are stored in the [workflow](workflows) so that a [script can be generated automatically](workflows-to-scripts).

An example script would be

```groovy
selectAnnotations()
qupath.ext.wsinfer.WSInfer.runInference("kaczmarj/pancancer-lymphocytes-inceptionv4.tcga")
```

where the `selectAnnotation()` line was added when I pressed the {guilabel}`Annotations` button in the WSInfer dialog, and the following line runs the specified models (creating tiles automatically).

To process in batch, I would need to

* Add my images to a QuPath project
* Annotate the regions of interest in the images (and save the data)
* Open the above script in QuPath's script editor
* Choose {menuselection}`Run --> Run for project`, and select the images I want to process


### Identifying TILs (overlaying predictions of two models)

The script below applies a lymphocyte patch classification model and then a breast tumor classification model on the same patches. This may assist in identifying tumor-infiltrating lymphocytes (TILs).

```groovy
/**
 * Script showing an end-to-end workflow using the WSInfer extension.
 *
 * Before starting, you should create an annotation for the main area of interest
 * (either by manually drawing or with a thresholder, e.g.
 * https://qupath.readthedocs.io/en/stable/docs/tutorials/thresholding.html)
 *
 * You should then update the variables in the first part of the script.
 *
 * Running the script will then:
 * - Apply two models sequentially, creating tiles and adding predictions as 'measurements'
 * - Use one measurement to assign a 'base' classification to each tile
 * - Use a second measurement to assign a 'positive/negative' classification to each tile
 *
 * The outcome is that tiles are produced and classified in 4 ways, e.g. as
 * 'Tumor: Positive', 'Tumor: Negative', 'Other: Positive', 'Other: Negative'
 *
 * QuPath will then automatically create summary measurements within all annotations,
 * giving the positive percentages for each base class.
 */

//--------

// The first model determines the tile size (resolution)
String firstModel = "kaczmarj/pancancer-lymphocytes-inceptionv4.tcga"

// The second model appends predictions to the tiles created by the first model
String secondModel = "kaczmarj/breast-tumor-resnet34.tcga-brca"

// The 'base' measurement is thresholded to classify tiles of interest
baseMeasurementName = "Tumor"
baseThreshold = 0.5
aboveBaseThresholdClass = "Tumor"
belowBaseThresholdClass = "Other"

// The 'positive' measurement is used to subclassify as positive or negative
String positiveMeasurementName = "Lymphocytes"
double positiveThreshold = 0.5

// Run the first model across all annotations, generating tiles
selectAnnotations()
qupath.ext.wsinfer.WSInfer.runInference(firstModel)

// Run the second model across all tiles that were created
selectTiles()
qupath.ext.wsinfer.WSInfer.runInference(secondModel)

// Apply the base classification
def tiles = getTileObjects()
tiles.each { t ->
    if (t.measurements[baseMeasurementName] > baseThreshold)
        t.classifications = [aboveBaseThresholdClass]
    else
        t.classifications = [belowBaseThresholdClass]
}

// Apply the intensity classification
setIntensityClassifications(tiles, positiveMeasurementName, positiveThreshold)

// Reset select so that we can see object colors
resetSelection()
```
