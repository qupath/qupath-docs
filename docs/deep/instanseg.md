# InstanSeg

(instanseg-extension)=

The [InstanSeg QuPath extension](https://github.com/qupath/qupath-extension-instanseg) provides a new and improved way to perform segmentation of both cells and nuclei in QuPath using deep learning.
It uses pre-trained models using the original [InstanSeg code](https://github.com/instanseg/instanseg).

Developed by the [QuPath group](https://institute-genetics-cancer.ed.ac.uk/research/research-groups-a-z/peter-bankhead-research-group) at the University of Edinburgh.

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
- PyTorch (this can be downloaded while using the extension so don't worry about now)

:::{tip}
A GPU is not required but can dramatically speed up processing.
If you have an NVIDIA GPU and want to use it with InstanSeg, you will need to install a version of CUDA compatible with PyTorch - please see {doc}`gpu`.
:::

## Set-up

InstanSeg can be installed into QuPath as described on [the extension page](qupath-extensions). After this, restart QuPath and you should see the extension within the Extensions menu {menuselection}`Extensions --> InstanSeg`.
The InstanSeg dialog will appear as shown below:

:::{figure} images/instanseg.png
:class: shadow-image small-image

The InstanSeg user interface
:::

:::{note}
Please note that you'll need internet access to download models and PyTorch, if required.
:::

## Using InstanSeg

### 1. Choose directory to store models

InstanSeg uses deep learning models (neural networks) to detect objects in images.
To do this, it needs to download models from the internet (or it can use locally-stored models, more on that later).
Click on the folder icon to choose a directory either containing models you already have, or just where you would like to save future downloaded ones.

### 2. Select a model

Select the dropdown box to see the available models.
Options with a cloud icon will need to be downloaded, as they are not local to your machine.
To do this, select the model and click the download button to fetch them.
If you have local models in your directory, you can also select these from the dropdown box.

You should select a suitable model for the type of image you are working with.
For example, for brightfield images we would usually use the brightfield_nuclei model that was trained on images with haematoxylin and DAB stain, but this model can also be used on images captured using other stains.

:::{note}
Please note that internet in needed to download the models.
:::

### 3. Create or select an annotation

Create an annotation or select pre-existing annotations/tiles/TMA cores you wish to run the model on.
It's recommended to keep the annotation smaller if this is the first time running InstanSeg.
This allows you to test the processing speed before running it on a larger region.
This might take some time, depending on your computer's processing speed and whether you're using a GPU.

### 4. Run the model

When you click `Run`, InstanSeg will check for PyTorch.
If this is not on your machine it will download it for you (this could be > 100 MB, so may take a while).
Once this is done, the model will run and you will see the results in the viewer.

:::{figure} images/instanseg_running.jpg
:class: shadow-image large-image

Running InstanSeg
:::

### 5. Viewing Results

The results will be displayed in the viewer.
The visibility of detections can be turned on or off using the show/hide detection objects button in the toolbar.
Additionally, using the fill/unfill detection objects button and the opacity slider in the toolbar can help distinguish the cells.

:::{figure} images/instanseg_fl_results.jpg
:class: shadow-image large-image

The results of running InstanSeg on a fluorescence image.

:::

:::

## Additional Options

InstanSeg has quite a few options to adapt to your device and preferences.
These can be seen below:

:::{figure} images/instanseg_options.png
:class: shadow-image small-image

The additional options available in InstanSeg
:::

### Preferred Device

The options available will depend upon your computer's capabilities (at least as far as they could be discerned by Deep Java Library):

- **CPU**: This is generally the safest - and slowest - option, because it should be supported on all computers.
- **MPS**: This stands for *Metal Performance Shaders*, and should be available on recent Macs - it is the Mac version of GPU acceleration
- **GPU**: This should appear if you have an NVIDIA GPU, CUDA... and a little bit of luck.

If either MPS or GPU work for you, they should reduce the time required for inference by a *lot*.
However configuration for GPU can be tricky, as it will depend upon other hardware and software on your computer - CUDA in particular.
For more info, see {doc}`gpu`.

:::{admonition} PyTorch & CUDA versions
:class: tip

The InstanSeg extension uses Deep Java Library to manage a PyTorch installation.
It won't automatically find any existing PyTorch you might have installed: Deep Java Library will download its own.

If you have a compatible GPU, and want CUDA support, you'll need to ensure you have an appropriate CUDA installed *before* PyTorch is downloaded.
:::

### Threads

This is the number of CPU/GPU threads to use to fetch and submit image tiles.
1 is usually too few, and high numbers may not be beneficial.
We suggest between 2-4 hence why this is the default.

### Tile Size

Large annotations are broken up into lots of tiles to be processed as doing it all at once may cause memory issues.
Usually 512 or 1024 pixels is a good size.

### Tile Padding

When the tiles are created, they overlap each other by several pixels to ensure that cells are not clipped between the boundaries.
Tile padding allows you to choose how much to overlap by with small padding being faster but more likely to result in clipping; this may result in many cells with unnatural vertical or horizontal edges.
If this occurs, then increase the value and run again.

### Input Channels

The number of channels be used by the model. Some models require a fixed number of channels and others can take an arbitrary number of inputs.
It's possible to use a fluorescence model on a brightfield image by using color deconvolution "stains" as channels, although this is only likely to work well if the stains can be separated very cleanly.
Even if so, results may be disappointing as these are not the types of images the model was trained on.

### Output

This determines whether the model outputs nuclei, cell membranes, or both.
Some models allow for both, but others are specific to one or the other.

### Make measurements

Following detection, QuPath can add common measurements of shape and intensity for each nucleus/cell; this option controls whether that's done automatically.

### Random colors

This will assign a random color to each detection object to help distinguish them, which can be useful for distinguishing between neighbouring objects.

## Scripting

If you want to use InstanSeg in a script, you can use either use the [workflows to scripts](https://qupath.readthedocs.io/en/stable/docs/scripting/workflows_to_scripts.html) method if you have already run a model.
Alternatively, you can use the following script as a template:

```groovy
qupath.ext.instanseg.core.InstanSeg.builder()
    .modelPath("/path/to/some/model")
    .device("cpu") // try "mps" on Apple silicon, or "gpu" if you have an Nvidia GPU
    .makeMeasurements(true)
    .randomColors(false)
    .build()
    .detectObjects()
```

## Citing

If you use this extension in any published work, we ask you to please cite

1. At least one of the two InstanSeg preprints above (whichever is most relevant)
2. The main QuPath paper - details [on the citation page for QuPath](https://qupath.readthedocs.io/en/stable/docs/intro/citing.html)
