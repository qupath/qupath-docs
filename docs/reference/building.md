(building)=
(building-from-source)=
# Building from source

Building software can be tricky, but hopefully this won't be - thanks to [Gradle].

:::{admonition} You might not need this
Most people using QuPath won't need to build QuPath from source!
Just download an existing installer from [qupath.github.io](https://qupath.github.io) and use that instead.

These instructions are for when you
  1. need to change QuPath's code yourself
  2. want to try the *very latest code* before a new release is available
:::

## Building from the command line

If you're moderately comfortable working from a command line, there's not much required to build QuPath:

1. Install git, e.g. from <https://git-scm.com>
2. Install OpenJDK {{java_version}} or later, e.g. from [adoptium.net](https://adoptium.net/)
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

:::{admonition} Dot or not?
:class: warning

You'll need to type `gradlew` if you're using a standard command prompt on Windows.

You'll need `./gradlew` if you're using macOS, Linux, or Windows with some other shell prompt.
:::

It will take a few minutes to download everything required and build the software.
If all goes well, you should see a triumphant message that the build was successful.

:::{figure} images/building-success.png
:class: shadow-image mid-image

Example of command line build success
:::

**That's it!**
You can find QuPath inside the `./build/dist/` subdirectory.

:::{admonition} Which Java version do I need?
:class: tip

If you already have Java installed, you might be able to skip Step 2.
Most Java versions >= 17 should work to launch Gradle, which will then automatically download the version it needs.
However, since QuPath currently requires OpenJDK {{java_version}}, we recommend just installing that and saving Gradle the extra effort.

Note that some problems have been reported using a version of OpenJDK based on OpenJ9, such as may be provided by some package managers.
Switching to an OpenJDK distribution based on HotSpot may help -- see [here](https://github.com/qupath/qupath/issues/484) for details.
:::


## Running with Gradle

You can also run QuPath from the command line via Gradle, without needing to create the package.

To do this, replace `jpackage` above with `run` (and `clean` is optional).
The command would then be simply

::::{tab-set}

:::{tab-item} Windows
:sync: win

``` bash
gradlew run
```
:::

:::{tab-item} macOS/Linux
:sync: nix

``` bash
./gradlew run
```
:::
::::

## Creating installers

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


:::{admonition} Simplifying builds with gradle.properties
:class: tip

If you often add `-P` flags when building QuPath, you can store these in the base QuPath directory in a file called `gradle.properties`.
This also gives a place to add more custom flags that can change the build.

For example, on my Mac I might put the following into `gradle.properties`:
```
org.gradle.parallel=true
org.gradle.java.home=/Library/Java/JavaVirtualMachines/temurin-|javaVersion|.jdk/Contents/Home
djl.engines=pytorch,mxnet,onnxruntime
djl.zoos=all
```

This tries to speed up the build process by parallelization, specifies which JDK to use, and selects some [Deep Java Library](deep-java-library) engines that I would like to include.

Then I only need to call
```
./gradlew jpackage
```
rather than some elaborate command that includes all these options.
:::

## Building a specific version

You can circumvent the need to use git entirely by downloading the QuPath code associated with a specific release from <http://github.com/qupath/qupath/releases>

Simply choose the *Source code (zip)* or *Source code (tar.gz)* option.
You can then build it from a command prompt as described above.

Alternatively, you can get the code associated with a specific QuPath release using git tags.
For example, to get the code for QuPath {{ env.config.release }} use the command

```{eval-rst}
.. parsed-literal::
   git checkout tags/v\ |release|\  -b\  v\ |release|
```

You can then try building it as above.

:::{admonition} Build commands might be different!
:class: warning

Some older QuPath versions might require different build commands (e.g. the steps for v0.2.3 are slightly different from v0.3.0).
Check out the docs associated with the specific version if this is the case.
:::


## Building with Fiji
By default, QuPath embeds a version of [ImageJ](https://imagej.net/software/imagej/).
This allows you to [send image regions to ImageJ, and even use custom ImageJ plugins](ImageJ).

[Fiji](https://fiji.sc) is a special distribution of ImageJ that contains a *lot* of custom plugins, and many extra features and other changes.

Thanks to [help from Curtis Rueden](https://forum.image.sc/t/embedding-fiji-inside-qupath/105065), since QuPath v0.6.0 it's possible to build QuPath with Fiji using

::::{tab-set}

:::{tab-item} Windows
:sync: win

``` bash
./gradlew jpackage -Pfiji
```
:::

:::{tab-item} macOS/Linux
:sync: nix

``` bash
./gradlew jpackage -Pfiji
```
:::
::::

Note that this will take some time to download everything it needs, and the package will be a *lot* bigger.
We also can't guarantee *everything* will work perfectly -- but most things we've tried seem to.

:::{figure} images/qupath-fiji.jpg
:class: shadow-image mid-image

QuPath built with Fiji
:::

## Other options

A few other ways to obtain and/or build QuPath's code are described below.
These might be better if you 
1. don't like the command line much, or
2. want to make changes to the software.

### GitHub Desktop

If you're using either Mac or Windows, [GitHub Desktop] provides a friendly way to get the QuPath code.
The main steps are

- Install [Visual Studio Code] (a text editor -- not essential, but helpful)
- Install [GitHub Desktop]
- Navigate to [https://github.com/qupath/qupath](https://github.com/qupath/qupath) in a browser
- Press {guilabel}`Clone or download` and choose {guilabel}`Open in Desktop`

:::{figure} images/building-clone.png
:class: shadow-image mid-image

Cloning QuPath using GitHub
:::

You can now open a command prompt in the correct directory directly from GitHub Desktop by choosing {menuselection}`Repository --> Open in Command Prompt`.

:::{admonition} Installing Git or not?
At this point you may be asked if you want to install Git.

You don't have to (I think...), but if you do then you'll be ask a lot of questions during the installation.
One of them is to choose a text editor, where you can select *Visual Studio Code*.
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

:::{figure} images/building-fetch.png
:class: shadow-image full-image

The GitHub Desktop interface
:::

If the option is {guilabel}`Fetch origin`, when you press the button the text will switch to {guilabel}`Pull origin` if any changes are available, with info about the number of changes.

You can press it again to pull those changes, and then rebuild QuPath using `gradlew`.

:::{figure} images/building-pull.png
:class: shadow-image full-image

Pulling changes from GitHub
:::
::::


### Running from an IDE

You should be able to import QuPath into any IDE (e.g. *IntelliJ*, *Eclipse*) that supports Gradle.

#### IntelliJ IDEA

The QuPath devs mostly use [IntelliJ IDEA] for QuPath development.
This allows us to run the software in debug mode -- and even change the code while it is running.

To do this, you can either:

* download and build QuPath once as described above, then use {menuselection}`Open` from within IntelliJ, and navigate to the directory containing the QuPath code, or
* use {menuselection}`Get from VCS` in IntelliJ to download the code directly from GitHub using git.
To do this, you should use the URL `https://github.com/qupath/qupath.git` (or the URL to your own git repository housing the QuPath code).

If you download the code using this approach, you should make sure you have installed a Java JDK before proceeding any further (see instructions above).

:::{figure} images/building-intellij-import.png
:class: shadow-image mid-image

IntelliJ start up window
:::

After opening the QuPath project (usually accepting any default import options is fine), {menuselection}`Run --> Debug (Alt + Shift + F9)`.
Then select {guilabel}`Edit Configurations...` from the drop-down menu, and {menuselection}`Add new configuration --> Gradle`.
Finally, enter `run` as the task, as in the image below.

:::{figure} images/building-intellij-launch.png
:class: shadow-image mid-image

Configuring QuPath to run in debug mode
:::

Now press {guilabel}`Apply` and then {guilabel}`Debug` in this window.

You can now use {menuselection}`Debug --> QuPath (Alt + Shift + F9)` to launch
QuPath with the same configuration in the future.

The useful thing about using debug mode is that you can make changes to the
QuPath code, and use {menuselection}`Run --> Debugging Actions --> Reload Changed Classes`
to reload the changes *while QuPath is running*.
Provided they aren't *too* extreme, the changes will be incorporated into the software without needing to relaunch it.
However, any major changes that alter method signatures (e.g. adding or removing arguments, or changing return types) will require QuPath to be relaunched.

[Visual Studio Code]: https://code.visualstudio.com
[IntelliJ IDEA]: https://www.jetbrains.com/idea/
[github desktop]: https://desktop.github.com/
[gradle]: http://gradle.org
[qupath's github repository]: https://github.com/qupath/qupath
[wix toolset]: https://wixtoolset.org/
