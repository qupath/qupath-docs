(instanseg-extension)=
# InstanSeg

The [InstanSeg QuPath extension](https://github.com/qupath/qupath-extension-instanseg) provides a new and improved way to perform segmentation of both cells and nuclei in QuPath using deep learning. It uses pre-trained models using the original [InstanSeg code](https://github.com/instanseg/instanseg).

Developed by Thibaut Goldsborough and other members of the [QuPath group]() at The Edinburgh University.

:::{admonition} Cite the paper!
:class: warning
If you use InstanSeg and/or this extension in a publication, please make sure to cite our paper.

**For brighfield images:**

Goldsborough, Thibaut, et al. InstanSeg: an embedding-based instance segmentation algorithm optimized for accurate, efficient and portable cell segmentation. *arXiv preprint* arXiv:2408.15954 (2024). <https://arxiv.org/abs/2408.15954>

**For fluorescence images:**

Goldsborough, Thibaut, et al. A novel channel invariant architecture for the segmentation of cells and nuclei in multiplexed images using InstanSeg. *bioRxiv* (2024): 2024-09. <https://www.biorxiv.org/content/10.1101/2024.09.04.611150v1>

(And if you use it in combination with QuPath, be sure to [cite the QuPath paper too!](citing))
:::

## Requirements

- QuPath [version 0.6](https://qupath.github.io/) (installation instructions [here](https://qupath.readthedocs.io/en/0.4/docs/intro/installation.html))
- At least one whole slide image
- [InstanSeg QuPath Extension](https://github.com/qupath/qupath-extension-instanseg)
- Internet access to download models and pytorch if needed
- - PyTorch (this can be downloaded while using the extension so don't worry about now)

:::{tip}
A GPU is not required but can dramatically speed up processing.
If you have an NVIDIA GPU and want to use it with InstanSeg, you will need to install a version of CUDA compatible with PyTorch - please see {doc}`gpu`.
:::

## Set-up
InstanSeg can be dragged and dropped into QuPath when its running. After this, restart QuPath and you should see the extension within the Extensions menu {menuselection}`Extensions --> InstanSeg`.
The InstanSeg dialog will appear as shown below:

:::{figure} images/instanseg.png
:class: shadow-image small-image

The InstanSeg user interface
:::

:::{note}
Please note that you'll need internet access to start the extension and download the models and PyTorch if required.
:::

## Using InstanSeg

### 1. Choose directory to store models

Click on the folder icon to choose a directory to which either contains models you already have or just where you would like to save future download ones.

### 2. Select a model

Select the dropdown box to see the models available. Options with a cloud icon will need to be downloaded as they are not local to your machine. To do this select the model and click the download button to fetch them. If you have local models in your directory you can also select these from the dropdown box. Be sure to select the relevant model for the type of image you are working with (unless you are being experimental!). The model being used here is for brightfield images and is being used on a haematoxylin and dab stain but could be used on other stains.

:::{note}
Please note that internet in needed to download the models.
:::

### 3. Create or select an annotation

Create an annotation or select a pre-existing annotations/tiles you wish to run the model on. It's recommended that if this is the first time running InstanSeg to keep the annotation smaller to test the processing speed before running it on a larger region. This might take some time, depending on your computers processing speed.

### 4. Run the model

When you select run, InstanSeg will check for PyTorch. If this is not on your machine it will download it for you (this may well be > 100 MB, so may take a while). Once this is done the model will run and you will see the results in the viewer.

:::{figure} images/instanseg_running.png
:class: shadow-image large-image

The running the InstanSeg model
:::

### 5. Viewing Results

The results will be displayed in the viewer. The cells detections can be turned on or off using the show/hide detection objects button in the toolbar. Additionally to help distinguished the cells an overlay can be placed over the cells using the fill/unfill detection objects button and the opacity adjusted using the slider also in the toolbar.

:::{figure} images/instanseg_bf_results.png
:class: shadow-image large-image

The results of the InstanSeg model on a brightfield image.

:::

:::{figure} images/instanseg_fl_results.png
:class: shadow-image large-image

The results of the InstanSeg model on a fluorescence image.

:::

## Additional Options
InstanSeg has quite a few options to adapt to your device and preferences. These can be seen below:

:::{figure} images/instanseg_options.png
:class: shadow-image small-image

The additional options available in InstanSeg
:::

### Preferred Device
The options available will depend upon your computer's capabilities (at least as far as they could be discerned by Deep Java Library):

* **CPU**: This is generally the safest - and slowest - option, because it should be supported on all computers.
* **MPS**: This stands for *Metal Performance Shaders*, and should be available on recent Apple silicon - it is the Mac version of GPU acceleration
* **GPU**: This should appear if you have an NVIDIA GPU, CUDA... and a little bit of luck.

If either MPS or GPU work for you, they should reduce the time required for inference by a *lot*.
However configuration for GPU can be tricky, as it will depend upon other hardware and software on your computer - CUDA in particular.
For more info, see {doc}`gpu`.

:::{admonition} PyTorch & CUDA versions
:class: tip

The WSInfer extension is using Deep Java Library to manage its PyTorch installation.
It won't automatically find any existing PyTorch you might have installed: Deep Java Library will download its own.

If you have a compatible GPU, and want CUDA support, you'll need to ensure you have an appropriate CUDA installed *before* PyTorch is downloaded.
:::

### Threads

This is the number of CPU/GPU threads to use to fetch and submit image tiles. 1 is usually to little and high numbers may not be beneficial. We suggest between 2-4 hence why this is the default.

### Tile Size

Large annotations are broken up into lots of tiles to be processed as doing it all at once may cause memory issues. Usually 512 or 1024 pixels is a good size.

### Tile Padding

When the tiles are created, they overlap each other by a certain amount to ensure the cells are not clipped between the boundaries. Tile padding allows you to choose how much to overlap by with small padding being faster but more likely to result in clipping. If this occurs then increase the value and run again.

### Input Channels

Quite simply the number of channels be used by the model. Some models have a fixed number and others dont care. Its possible to use a fluorescence model on a brightfield image by using color deconvolution "stains" as channels however results may vary.

### Output

This determined whether the model outputs nuclei or cell membranes or both. Some models allow for both and can be used in various combinations but others are specific to one or the other.

### Make measurements

Following detection some measurements are created for each nuclei/cell but this isn't always required so can be toggled off.

### Random colors

This will assign a random color to each detection object to help distinguish them which can be useful for distinguishing between neighbouring objects.

## Scripting

If you want to use InstanSeg in a script, you can use either use the [workflows to scripts](https://qupath.readthedocs.io/en/stable/docs/scripting/workflows_to_scripts.html) method if you have already run a model. 
Alternatively, you can use the following script as a template:

```groovy
qupath.ext.instanseg.core.InstanSeg.builder()
    .modelPath("/path/to/some/model")
    .device("mps")
    .nThreads(4)
    .tileDims(512)
    .interTilePadding(32)
    .inputChannels([ColorTransforms.createChannelExtractor("Red"), ColorTransforms.createChannelExtractor("Green"), ColorTransforms.createChannelExtractor("Blue")])
    .outputChannels()
    .makeMeasurements(true)
    .randomColors(false)
    .build()
    .detectObjects()
```

## Citing

If you use this extension in any published work, we ask you to please cite

1. At least one of the two InstanSeg preprints above (whichever is most relevant)
2. The main QuPath paper - details [here](https://qupath.readthedocs.io/en/stable/docs/intro/citing.html)