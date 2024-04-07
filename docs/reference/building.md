(building)=
(building-from-source)=
# Building from source

Building software can be tricky, but hopefully this won't be - thanks to [Gradle].

:::{note} Do you need this?!
Most people using QuPath won't need to build QuPath from source!
Just download an existing installer from [qupath.github.io](https://qupath.github.io) and use that instead.
:::

## Building from the command line

If you're moderately comfortable working from a command line, there's not much required to build QuPath:

1. Install git, e.g. from <https://git-scm.com>
2. Install OpenJDK 17, e.g. from [adoptium.net](https://adoptium.net/en-GB/temurin/releases/?version=17)
3. Open a command prompt in an empty directory and run the following:


::::{tab-set}

:::{tab-item} Windows
:sync: win

``` bash
git clone https://github.com/qupath/qupath
cd qupath
gradlew clean jpackage
```
:::

:::{tab-item} macOS/Linux
:sync: nix

``` bash
git clone https://github.com/qupath/qupath
cd qupath
./gradlew clean jpackage
```
:::
::::

It will take a few minutes to download everything required and build the software.
If all goes well, you should see a triumphant message that the build was successful.

:::{figure} images/building-success.png
:align: center
:class: shadow-image
:width: 50%

Example of command line build success
:::

**That's it!**
You can find QuPath inside the `./build/dist/` subdirectory.

:::{admonition} Which Java version do I need?
:class: tip

If you already have Java installed, you might be able to skip Step 2.
Most Java versions >= 8 should work to launch Gradle, which will then automatically download the version it needs.
However, since QuPath currently requires OpenJDK 16, we recommend just installing that and saving Gradle the extra effort.

Note that some problems have been reported using a version of OpenJDK based on OpenJ9, such as may be provided by some package managers.
Switching to an OpenJDK distribution based on HotSpot may help -- see [here](https://github.com/qupath/qupath/issues/484) for details.
:::

:::{admonition} Notes for Apple silicon
:class: warning

If you're working on a recent Mac with Apple silicon, the easiest thing to do is use a Java JDK for Intel.
Everything will run a bit slower through Rosetta2 -- but the difference might not be noticeable.

If you use a JDK for Apple silicon, most things should work - but note the caveats [described on the installation page](apple-silicon);

You can add OpenSlide support from the start by:
* Installing [OpenSlide Java using Homebrew](https://github.com/petebankhead/homebrew-qupath)
* Building QuPath with the command `./gradlew clean jpackage -P openslide=/opt/homebrew/opt/openslide-java/lib/openslide-java/openslide.jar`

This should then use your local OpenSlide installation.
The disadvantage is that it won't be found if you transfer QuPath to another computer.
:::

### Customizing the build

#### Creating installers

If you need to create an installer for QuPath, you can use

::::{tab-set}

:::{tab-item} Windows
:sync: win

``` bash
gradlew clean jpackage -P package=installer
```
:::

:::{tab-item} macOS/Linux
:sync: nix

``` bash
./gradlew clean jpackage -P package=installer
```
:::
::::

Note that for this to work on Windows you'll need to install [WIX Toolset].

(building-gpu)=

#### Adding GPU support

A common question is whether QuPath uses a GPU to accelerate processing.
The answer, currently, is 'no'.

However, it is possible to build QuPath with support for CUDA via OpenCV and JavaCPP by using the `-Pcuda` or `-Pcuda-redist` options.

::::{tab-set}

:::{tab-item} Windows
:sync: win

``` bash
gradlew clean jpackage -Pcuda-redist
```
:::

:::{tab-item} macOS/Linux
:sync: nix

``` bash
./gradlew clean jpackage -Pcuda-redist
```
:::
::::

You should use `-Pcuda` if you want to use your own CUDA installation (which needs to be the correct version to match JavaCPP's OpenCV distribution), and `-Pcuda-redist` if you want to download the necessary files automatically.
Before doing so you should check out the licensing terms for CUDA at <https://github.com/bytedeco/javacpp-presets/tree/master/cuda>

Two important things to note are:

- This only works on Windows or Linux with recent NVIDIA GPUs and drivers
- Currently, only {ref}`StarDist` is likely to see any benefit (no other QuPath code explicitly uses the GPU)

:::{admonition} Simplifying builds with gradle.properties
:class: tip

If you often add `-P` flags when building QuPath, you can store these in the base QuPath directory in a file called `gradle.properties`.
This also gives a place to add more custom flags that can change the build.

For example, on my Apple silicon Mac I might put the following into `gradle.properties`:
```
org.gradle.parallel=true
org.gradle.java.home=/Library/Java/JavaVirtualMachines/temurin-17.jdk/Contents/Home
openslide=/opt/homebrew/Cellar/openslide-java/0.12.2/lib/openslide-java/openslide.jar
djl.engines=pytorch,mxnet,onnxruntime
djl.zoos=all
```

This tries to speed up the build process by parallelization, specifies which JDK to use, provides a path to OpenSlide, and specifies some [Deep Java Library](deep-java-library) engines that I would like to include.

Then I only need to call
```
./gradlew jpackage
```
rather than some elaborate command.
:::

#### Building a specific version

QuPath releases are associated with different git tags.
You can get the code associated with QuPath {{ env.config.release }} by using the command

```{eval-rst}
.. parsed-literal::
   git checkout tags/v\ |release|\  -b\  v\ |release|
```

You can then try building it as above, however *note that some different versions may require different build commands* (e.g. the steps for v0.2.3 are slightly different from v0.3.0).
Check out the docs associated with the specific version if this is the case.

## Other options

A few other ways to obtain and/or build QuPath's code are described below.
These might be better if you a) don't like the command line much, or b) want to make changes to the software.

### GitHub Desktop

If you're using either Mac or Windows, [GitHub Desktop] provides a friendly way to get the QuPath code.
The main steps are

- Install [Atom] (a text editor -- not essential, but helpful)
- Install [GitHub Desktop]
- Navigate to [https://github.com/qupath/qupath](https://github.com/qupath/qupath) in a browser
- Press {guilabel}`Clone or download` and choose {guilabel}`Open in Desktop`

:::{figure} images/building-clone.png
:align: center
:class: shadow-image
:width: 50%

Cloning QuPath using GitHub 
:::

You can now open a command prompt in the correct directory directly from GitHub Desktop by choosing {menuselection}`Repository --> Open in Command Prompt`.

:::{admonition} Installing Git or not?
At this point you may be asked if you want to install Git.

You don't have to (I think...), but if you do then you'll be ask a lot of questions during the installation.
One of them is to choose a text editor, where you can select *Atom*.
:::

Finally, the command needed to build QuPath is then the same as above:

::::{tab-set}

:::{tab-item} Windows
:sync: win

``` bash
gradlew clean jpackage
```
:::

:::{tab-item} macOS/Linux
:sync: nix

``` bash
./gradlew clean jpackage
```
:::
::::


::::{admonition} Updating the code
Once you've built QuPath once, updating it to use the latest source code in *GitHub Desktop* should be easier.
The right-most button on the main toolbar serves two purposes: to {guilabel}`Fetch` information about the latest changes (from GitHub) and to {guilabel}`Pull` the changes down to your computer.

:::{figure} images/building-branches.png
:align: center
:class: shadow-image
:width: 90%

The GitHub Desktop interface
:::

If the option is {guilabel}`Fetch origin`, when you press the button the text will switch to {guilabel}`Pull origin` if any changes are available, with info about the number of changes.

You can press it again to pull those changes, and then rebuild QuPath using `gradlew`.

:::{figure} images/building-pull.png
:align: center
:class: shadow-image
:width: 50%

Pulling changes from GitHub
:::
::::

### Download release

You can circumvent the need to use git entirely by downloading the QuPath code associated with a specific release from <http://github.com/qupath/qupath/releases>

Simply choose the *Source code (zip)* or *Source code (tar.gz)* option.
You can then build it from a command prompt as described above.

### Running from an IDE

You should be able to import QuPath into any IDE (e.g. *IntelliJ*, *Eclipse*) that supports Gradle.

#### IntelliJ IDEA

I personally use [IntelliJ IDEA] for QuPath development, which allows me to run
the software in debug mode -- and even change the code while it is running.

To do this, you can either:

* download and build QuPath once as describe above,
  and use {menuselection}`Open` from within IntelliJ, and
  navigate to the directory containing the QuPath code, or
* use {menuselection}`Get from VCS` in IntelliJ to download the code
  directly from GitHub using git. To do this, you should use the URL
  `https://github.com/qupath/qupath.git` (or the URL to your own git repository
  housing the QuPath code).  
  If you download the code using this method, you should make sure you have
  installed a Java JDK before proceeding any further (see instructions above).

:::{figure} images/building-intellij-import.png
:align: center
:class: shadow-image
:width: 75%

IntelliJ start up window
:::

After opening the QuPath project (usually accepting any
default import options is fine), {menuselection}`Run --> Debug (Alt + Shift + F9)`,
and select "Edit Configurations..." from the drop-down menu, and 
{menuselection}`Add new configuration --> Gradle`. Then, enter `run` as the task,
as in the image below.

:::{figure} images/building-intellij-launch.png
:align: center
:class: shadow-image
:width: 100%

Configuring QuPath to run in debug mode
:::

Now press {menuselection}`Apply` and then {menuselection}`Debug` in this window.

You can now use {menuselection}`Debug --> QuPath (Alt + Shift + F9)` to launch
QuPath with the same configuration in the future.

The useful thing about using debug mode is that you can make changes to the
QuPath code, and use
{menuselection}`Run --> Debugging Actions --> Reload Changed Classes`
to reload the changes *while QuPath is running* and, providing they aren't *too*
extreme, they will be incorporated into the software without needing to relaunch it.
For example, any changes that alter method signatures (e.g. adding or removing
arguments, or changing return types) will require a restart.

[atom]: https://atom.io/
[IntelliJ IDEA]: https://www.jetbrains.com/idea/
[github desktop]: https://desktop.github.com/
[gradle]: http://gradle.org
[qupath's github repository]: https://github.com/qupath/qupath
[wix toolset]: https://wixtoolset.org/
