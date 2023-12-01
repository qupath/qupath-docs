(gpu-support)=
# GPU support

Graphics Processing Units (GPUs) can make the use of deep learning *much* faster... but can be notoriously awkward to set up.

Deep Java Library (DJL) supports the use of NVIDIA GPUs for Windows and Linux.
This page explains how to (hopefully) get it working.

:::{admonition} Important!
:class: warning

This is **only** relevant if you're using Windows or Linux with an NVIDA GPU.
:::

:::{admonition} What about Macs?
NVIDIA GPUs are extremely uncommon in Macs (I had one in a 2013 iMac... but no more).
More recent Macs with Apple Silicon *do* have GPU acceleration, but it is quite different.

Currently, Apple Silicon GPU acceleration *can* work with PyTorch via Deep Java Library.
Not all models work, but I have used it very successfully with [wsinfer.md](wsinfer-extension) and seen a substantial improvement in performance.

The good news is that it requires *none of the awkward configuration here*.
When it works, it just works.
The only thing you need to do is set the device to be 'MPS' (for *Metal Performance Shaders*).
:::

## Explaining the problem

Assuming you *have* an NVIDIA GPU in your computer, to use it with Deep Java Library you generally need three things installed:

1. A **GPU driver**
2. **CUDA**
3. **cuDNN**

You can find all of these things via NVIDIA's website.

So why is this hard?

1. The versions can be *really* important.
   * The driver generally just needs to be 'recent'; but if things fail, updating the driver can sometimes fix them.
   * The required CUDA version changes according to which deep learning framework you'll use (e.g. PyTorch, TensorFlow)... and which version of that framework. It is a strict requirement.
   * The required cuDNN version is generally whichever one matches CUDA.
2. Installing the full CUDA toolkit and cuDNN is not exactly straightforward, requiring an NVIDIA developer account.

:::{admonition} Why can't QuPath do this for me?
It's not possible to bundle up everything you need in QuPath, for practical and licensing reasons.
It would make the download huge, and you need to accept NVIDIA's license agreements to use parts that they provide.
:::


## DJL & auto-detecting the GPU

DJL is pretty smart.
When you want to use a deep learning framework, DJL can try to find and download a version that is compatible with your computer.

For example, suppose you want to use PyTorch. 

DJL would check your computer (e.g. Windows, Linux, Mac), detect whether you have CUDA installed, and download [a supported version of PyTorch](https://docs.djl.ai/engines/pytorch/pytorch-engine/index.html#supported-pytorch-versions) with or without GPU support based on that.

*However*, DJL can't currently check that you have the *right* version of CUDA, driver & cuDNN in advance.

So this process only works if you have everything installed correctly first.
If some part of the puzzle doesn't fit, you may get a broken download that doesn't work at all.
Or a version that lacks GPU support.

The resulting errors can be obscure, confusing, and hard to debug.
These docs try to spare you a lot of pain and guesswork.

## Which versions do I need?

When you download cuDNN, you should generally be able to pick a version that matches CUDA -- so getting CUDA right is the hardest thing.

To decipher this, you should know:

* Each QuPath release uses a specific version of DJL.
* Each DJL has a specific *default* version for each deep learning framework.
  * For PyTorch, DJL typically supports a few versions
* Each framework has specific requirements regarding CUDA (and therefore cuDNN).

The following sections attempt to outline the versions (as best I can figure them out):

(gpu-versions-pytorch)=
#### PyTorch

| QuPath | DJL     | PyTorch | CUDA |
|--------|---------|---------|------|
| v0.5.x | 0.24.0  | 2.0.1   | 11.8 |
| v0.4.x | 0.20.0  | 1.13.0  | 11.7 |

(gpu-versions-tf)=
#### TensorFlow

| QuPath | DJL     | TensorFlow | CUDA |
|--------|---------|------------|------|
| v0.5.x | 0.24.0  | 2.10.1     | 11.3 |
| v0.4.x | 0.20.0  | 2.7.4      | 11.2 |

> Note: DJL + TensorFlow will currently not work **at all** on Apple Silicon (no matter whether you have the Intel or Apple Silicon build of QuPath... unless you build TensorFlow from source).


## Conda environments

As you can see, the CUDA requirements are different -- and incompatible -- between PyTorch and TensorFlow, and across QuPath releases.

Installing one version of CUDA on your computer, and trying to make sure it's the right one for exactly what you want to do, seems frustrating and ultimately doomed.

**[Conda environments](https://docs.conda.io)** offer a solution in three steps:

1. Create a conda environment
2. Install the CUDA/cuDNN versions that you need inside the environment
3. Create a QuPath launcher using that environment

The good news is that you can have multiple conda environments, each with different CUDA versions, and each with corresponding QuPath launchers.

This allows you to have GPU support for different QuPath versions and deep learning frameworks on the same computer.

### Getting started with conda (or mamba)

Conda essentially enables you to install software packages in different 'environments', and then switch between them as needed.
It is *mostly* used with Python, but not exclusively.
For more info, see the [conda docs here](https://docs.conda.io).

[Mamba](https://mamba.readthedocs.io) is a tool that allows you to create and manage conda environments.
It has the advantage of generally being a lot faster than conda when trying to figure out which versions of packages are compatible with one another.

In this example, I'll use `mamba` installed on Windows using [the installation instructions here](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html).
These specify installing the *Miniforge* distribution... but it's not really necessary to remember all the different terms and distributions.
For our purposes, `conda` and `mamba` ar interchangeable and the distribution shouldn't matter.

### Creating an environment for PyTorch

You can create a conda (/mamba) environment by typing the following and pressing {kbd}`Enter`:
```
mamba create -n qupath-pytorch
```
Here, `pytorch-qupath` is the name of the environment (you can call it something else).

Then you should *activate* the environment
```
mamba activate qupath-pytorch
```

At this point, you really only need to install CUDA and cuDNN -- but to make things easier, we'll install PyTorch entirely, and rely upon mamba to figure out the necessary dependencies.
This increases the chances we end up with a working combination

To do this, check the [PyTorch + CUDA combination required for QuPath](gpu-versions-pytorch) and then the [PyTorch installation instructions](https://pytorch.org/get-started/previous-versions/) -- replacing `conda` with `mamba` if you like.

If you want PyTorch 1.13.1 (recommended for Windows/Linux, but *not* Apple Silicon):
```
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 -c pytorch
```

If you want PyTorch 2.0.1 (needs a bit more work on Windows/Linux, [see below](djl-gpu-pytorch-201)):
```
mamba install pytorch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 pytorch-cuda=11.8 -c pytorch -c nvidia
```

You can now [verify your PyTorch installation](https://pytorch.org/get-started/locally/#mac-verification) if needed.


### Creating a launcher for QuPath + PyTorch

To create a launcher for QuPath using CUDA from the conda environment we just created, you need to:

1. Run QuPath
2. Install the [QuPath Deep Java Library extension](deep-java-library)
3. Run {menuselection}`Extensions --> Deep Java Library --> Create launch script`
4. Select the path to your conda environment, and specify the PyTorch version

After clicking 'ok', you can choose a location to store the launch script.

On Windows, this should be a `.bat` file that can be launched with a double-click; on Linux it will be a `.sh` file that can be run (for example) from a terminal with `bash /path/to/script.sh`.


:::{admonition} Extra options
:class: tip

There are some extra PyTorch options with DJL.
There are more details in the [DJL docs](https://docs.djl.ai/engines/pytorch/pytorch-engine/index.html).

*In theory* you should be able to point to a PyTorch installation, to use it rather than have DJL download PyTorch entirely.
*In practice* I have found that often fails for me, and it is more reliable to have DJL download PyTorch itself.
:::

### Creating a conda environment for TensorFlow

If needed, we can follow a similar process to create an environment for TensorFlow.

Here, we *won't* install TensorFlow entirely, but rather only CUDA.
This is because DJL's preferred TensorFlow/CUDA combo can be different from what conda will give us.

```
mamba create -n cuda-11-3
mamba activate cuda-11-3

mamba install cudatoolkit=11.3 cudnn
```

You can then create a launch script just as with PyTorch above, ignoring all the optional PyTorch parts.

:::{admonition} TensorFlow & CUDA incompatibilities
:class: warning

Unfortunately, DJL currently doesn't like to load TensorFlow *at all* if it detects an *incompatible* version of CUDA.

Because PyTorch and TensorFlow require different CUDA versions, this means you may not be able to run both side-by-side - rather, you will need two separate launchers.
:::

### Checking everything works

If you get this far, then it's time to return to {ref}`deep-java-library`.
There you can use the QuPath DJL extension to request an engine... and hopefully it'll be the right one.

You can print the engine you get using the following script:

```groovy
println ai.djl.engine.Engine.getEngine("PyTorch")
```

If all has gone well, you should see something like this:

```cmd
INFO: PyTorch graph executor optimizer is enabled, this may impact your inference latency and throughput. See: https://docs.djl.ai/docs/development/inference_performance_optimization.html#graph-executor-optimization
INFO: Number of inter-op threads is 4
INFO: Number of intra-op threads is 4
INFO: PyTorch:2.0.1, capabilities: [
      CUDA,
      CUDNN,
      OPENMP,
      MKL,
      MKLDNN,
]
PyTorch Library: C:\Users\yourname\.djl.ai\pytorch\2.0.1-cu118-win-x86_64
```

If not, the troubleshooting below may help.

## More troubleshooting

Conda environments can help solve *most* of the problems... but not all.
This section contains assorted fixes for other issues as they arise.

(djl-gpu-pytorch-201)=
### Fix for UnsatisfiedLinkError (PyTorch 2.0.1, Windows)

You may find that PyTorch 2.0.1 + CUDA 11.8 doesn't work on Windows.
If you see an error, it may look like this:

```cmd
ERROR: C:\Users\yourname\.djl.ai\pytorch\2.0.1-cu118-win-x86_64\nvfuser_codegen.dll: Can't find dependent libraries in print_engine.groovy at line number 5
java.base/jdk.internal.loader.NativeLibraries.load(Native Method)
    java.base/jdk.internal.loader.NativeLibraries$NativeLibraryImpl.open(NativeLibraries.java:388)
    java.base/jdk.internal.loader.NativeLibraries.loadLibrary(NativeLibraries.java:232)
    java.base/jdk.internal.loader.NativeLibraries.loadLibrary(NativeLibraries.java:174)
    java.base/java.lang.ClassLoader.loadLibrary(ClassLoader.java:2394)
    java.base/java.lang.Runtime.load0(Runtime.java:755)
    java.base/java.lang.System.load(System.java:1953)
    ai.djl.pytorch.jni.LibUtils.loadNativeLibrary(LibUtils.java:353)
```

The 'solution' is to simply delete the file `nvfuser_codegen.dll`.
For more details, see the [DJL bug report on GitHub](https://github.com/deepjavalibrary/djl/issues/2552).

