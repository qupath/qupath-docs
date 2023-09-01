# Installation

## Download & install

QuPath isn't currently a signed application.
This means that, after you download it for your platform (Windows, Linux, macOS) from [GitHub](https://github.com/qupath/qupath/releases/latest), you may need to take a few extra steps to get it to run:

- On **Windows**, if you downloaded an `.msi` file then double-click on it to launch the installer
  - If you see a warning, choosing {guilabel}`More info` and {guilabel}`Run anyway` should let you proceed
- On **Windows**, if you downloaded a `.zip` then extract its contents and run the `QuPath.exe` file
- On **macOS**, right-click the `.pkg` file, then choose 'Open' (you might need to do this twice)
  - If you're using an M1/M2 Mac, please check out the [notes on Apple silicon](apple-silicon)
- On **Linux**, download and extract the `.tar.xz` file
  - You'll probably have to use `chmod u+x /path/to/QuPath/bin/QuPath` to make the launcher executable

See {ref}`Troubleshooting` for more information.

:::{admonition} What is *QuPath (console).exe*?
On Windows, you will see two executable files: *QuPath.exe* and *QuPath (console).exe* -- perhaps with version numbers incorporated.

You can use either.
The only difference between these is that the *console* version also shows a console that prints text as QuPath runs.
This is useful when using the {ref}`Command line`.
:::


## Troubleshooting

If you have trouble installing at all, please see below...

### Windows (.zip)

If QuPath does not start, make sure that you are not trying to run it directly from within the `.zip` file that you downloaded.
It is important to first *extract* the files into their own 'QuPath' folder, and then run `QuPath.exe` from within that.

### Windows (.msi)

#### The QuPath installer gives a scary warning

It is expected that Windows will give a scary-looking warning whenever the QuPath installer is first run, as it tries to protect you from software it does not know.

:::{figure} images/installing_windows_warning.png
:align: center
:class: shadow-image
:width: 60%

Windows warning
:::

If you would like to get past this screen, press *'More info'* and the option to *'Run anyway'* appears.

:::{figure} images/installing_windows_warning_run_anyway.png
:align: center
:class: shadow-image
:width: 60%

Windows warning run anyway
:::

#### The QuPath installer does not start

If the QuPath installer does not start at all, you may not have administrator privileges on your computer - and therefore cannot install it.  Try downloading the `.zip` file instead, which should not need such privileges.

:::{important}
Running QuPath on 32-bit Windows is not supported.
:::

### macOS

Mac users may also see security messages when running the QuPath pkg installer.

#### QuPath cannot be opened

If you see the message that QuPath cannot be opened because the developer cannot be verified, you can try right-clicking on the QuPath icon and select *Open* from the popup menu that appears.

:::{figure} images/mac-warning-04.png
:align: center
:class: shadow-image
:width: 40%

Gatekeeper on macOS on double-click.
:::

You should then see an option to open QuPath that should work.

:::{figure} images/mac-warning-04-override.png
:align: center
:class: shadow-image
:width: 40%

Gatekeeper on macOS after right-clicking and selecting 'Open'.
:::

You may also need to right-click and choose open the first time you run the QuPath app after installation.
Double-clicking should work as normal once it has been run once.

:::{warning}
Since macOS (presumably) has your best interests at heart, circumventing its security settings routinely is probably not advisable.

However, as an open source project, we don't currently have the time and resources needed to distribute QuPath as a signed/notarized app and avoid these warnings.
:::


(apple-silicon)=
#### Apple Silicon

To use the 'default' (Intel) build of QuPath on a recent Mac with an Apple Silicon processor, you'll need to have Rosetta 2 installed.
There is a good chance you already have it (e.g. if you're using any other software written for Intel processors), but if not there are [more details on Apple's website](https://support.apple.com/en-gb/HT211861).

QuPath v0.4.0 *also* introduces a new (experimental) QuPath build specifically for Apple Silicon, which doesn't require Rosetta 2.
If you have a new Mac with an M1/M2 processor, this is likely to run much faster than the alternative Intel build - but unfortunately has some significant disadvantages:

* OpenSlide is missing. You can add it separately with the help of [Homebrew](https://brew.sh) - see <https://github.com/petebankhead/homebrew-qupath> for details
* Images opened with Bio-Format may not work if they require a native library, e.g.
  * some .ndpi files (e.g. the OS-1/OS-2/OS-3.ndpi sample images)
  * some .czi files (with JPEG-XR compression)
* TensorFlow for Java doesn't work. But it doesn't work on Apple Silicon even if you use the Intel build (this will hopefully be fixed by the TensorFlow Java maintainers in the future).

### Linux

QuPath for Linux was compiled on Ubuntu, with best efforts made to include all dependencies, although in the case of OpenSlide this wasn't entirely successful.
You may need to install OpenSlide separately through your package manager.

Known issues are:

* Black/white tiles can appear in some images reading using OpenSlide; updating libpixman can resolve this (see [Issue #355](https://github.com/qupath/qupath/issues/355)), or alternatively you can try the alternative bash script `/path/to/QuPath/bin/QuPath.sh` to launch the software.
* QuPath (like other Java applications) cannot be started if its installation path contains a directory named `bin`; moving to another directory resolves this (see [Issue #614](https://github.com/qupath/qupath/issues/614))
* Some sub-dependencies might not be found (reported [on the forum](https://forum.image.sc/t/qupath-v0-4-0-now-available/74887/7))

If you still have trouble getting OpenSlide to work, you could also try [installing OpenSlide Java using Homebrew](https://github.com/petebankhead/homebrew-qupath).
