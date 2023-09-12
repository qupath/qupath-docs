(wsinfer-extension)=
# WSinfer

The [WSInfer QuPath extension](https://github.com/qupath/qupath-extension-wsinfer/) enables easy and interactive model inference without the need for scripting. It is a collaboration between the QuPath group and Stony Brook University.

:::{admonition} Cite the paper!
If you use WSInfer in a publication, be sure to cite the original WSInfer paper found [here](https://arxiv.org/abs/2309.04631).
:::

## Requirements

- QuPath [version 0.4](https://qupath.github.io/) (installation instructions [here](https://qupath.readthedocs.io/en/0.4/docs/intro/installation.html)).
- At least one whole slide image (see acknowledgements )
- [WSInfer QuPath Extension](https://github.com/qupath/qupath-extension-wsinfer/releases)
- PyTorch (this can be downloaded while using the extension should you not already have it installed)

## Set-up

With QuPath installed and running, drag and drop the WSInfer extension into the application and restart QuPath.
Once installed, open up an image and run the extension via {menuselection}`Extensions --> WSInfer` and you should see the window below

:::{figure} images/wsinfer.png
:align: center
:class: shadow-image
:width: 40%

The WSInfer user interface
:::

:::{note}
Please note that internet access will be needed for starting the extension and downloading the models.
:::

## Whole Slide Inference

### 1. Select a model

Select the a model from the dropdown menu and click the download icon button to start the download and wait to be notified the download is complete.

### 2. Create or select an annotation

Create an annotation or select a pre-existing annotations/tiles you wish to run the model on. It's recommended that if this is the first time running WSInfer to keep the annotation smaller to test the processing speed before running it on a larger region (it can take some time depending on your computers processing speed).

:::{note}
The WSInfer models are created with certain tile sizes so when running on pre-made detections or tiles please proceed with caution.
:::

### 3. Run

Check you have an annotation selected and click run and if all the requirements are present then the processing will begin. If you don't have PyTorch yet then you will be prompted to download it which due to its size will take some time.

### 4. View Results

Once the progress bar is complete the results can be visualized using the tools in the {guilabel}`View Results` section. {guilabel}`Measurement Maps` tool presents the score of each tile by color and can be interacted with using the 3 toggle buttons to either show, hide or fill the annotations and detections. The slider can be used to increase or decrease the fill opacity so the tissue features can be seen under the WSInfer scores.

The {guilabel}`Results Table` provides details for each tile and the option to export for further analysis.

## Additional Options

For those looking to make the processing faster, WSInfer can be run using either CPU, GPU or MPS. By default the CPU is selected since the GPU, CUDA and MPS versions are yet to be fully explored.
From this section the model directory and number of parallel workers can also be found and edited as seen in the image below.

:::{figure} images/wsinfer_options.png
:align: center
:class: shadow-image
:width: 40%

WSInfer's additional options
:::
