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

QuPath v0.5 for Mac is available as both Intel (x64) and Apple Silicon (aarch64) builds.

Users of recent Macs with M1/M2 processors are likely to find QuPath runs faster with the Apple Silicon builds (~30%).

One important caveat is that Bio-Formats - the open-source library QuPath uses to read many image types - does not yet *fully* support Apple Silicon, which affects a small number of formats.
This is most relevant for users hoping to work with .czi images (from Zeiss microscopes/scanners) that use JPEG-XR compression.
It also affects .ndpi files (from Hamamatsu scanners), but less crucially because QuPath will use OpenSlide to read these by default anyway.

If the limitation causes you trouble, you can also run the Intel build on Apple Silicon - with full Bio-Formats support.
To do this, you'll need to have Rosetta 2 installed.
There is a good chance you already have it (e.g. if you're using any other software written for Intel processors), but if not there are [more details on Apple's website](https://support.apple.com/en-gb/HT211861).

The type of build is included in the .app file name (either x64 or aarch64).
This makes it easier for Mac users to install both Intel and Apple Silicon builds side-by-side.


### Linux

QuPath for Linux was compiled on Ubuntu, with best efforts made to include all dependencies, although in the case of OpenSlide this wasn't entirely successful.
You may need to install OpenSlide separately through your package manager.

Known issues are:

* Black/white tiles can appear in some images reading using OpenSlide; updating libpixman can resolve this (see [Issue #355](https://github.com/qupath/qupath/issues/355)), or alternatively you can try the alternative bash script `/path/to/QuPath/bin/QuPath.sh` to launch the software.
* QuPath (like other Java applications) cannot be started if its installation path contains a directory named `bin`; moving to another directory resolves this (see [Issue #614](https://github.com/qupath/qupath/issues/614))
* Some sub-dependencies might not be found (reported [on the forum](https://forum.image.sc/t/qupath-v0-4-0-now-available/74887/7))

If you still have trouble getting OpenSlide to work, you could also try [installing OpenSlide Java using Homebrew](https://github.com/petebankhead/homebrew-qupath).
