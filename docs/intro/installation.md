# Installation

## Which QuPath download do I need?

### QuPath for Windows

On **Windows**, you have two options when downloading QuPath:

* **Windows installer (msi)** use this if you want to install QuPath, so that it appears in the {guilabel}`Start` menu like most apps
* **Windows portable (exe)** use this if you want to just unzip a folder containing QuPath, and run it from there - with no further installation needed

(qupath-versions-for-mac)=
### QuPath for Mac

On **macOS** you also have two options when downloading QuPath:

* **macOS Intel (pkg)** this should work on all recent Macs - both with Intel processors or Apple Silicon. If you aren't sure, this is the default option to choose.
  * To run the Intel version on Apple silicon, you'll need to have Rosetta 2 installed. There is a good chance you already have it (e.g. if you're using any other software written for Intel processors), but if not there are [more details on Apple's website](https://support.apple.com/en-gb/HT211861).
* **macOS Apple silicon (pkg)** this *only* runs on recent Macs using Apple Silicon (e.g. M1, M2 or M3 processors).
  * The big *advantage* is that it runs substantially faster than the Intel version on supported computers.
  * The big *disadvantage* is that Bio-Formats doesn't yet support Apple silicon - which means that a small number of file formats won't work. The most relevant of these are .czi images from Zeiss Axioscans using JPEG-XR compression.

If you have a Mac with Apple silicon, it's possible to install both the Intel and Apple silicon versions of QuPath and run them both.
The type of build is included in the .app file name (either x64 for Intel, or aarch64 for Apple silicon) to help you distinguish between them.


## Download & install

QuPath isn't currently a signed application.
This means that, after you download it for your platform (Windows, Linux, macOS) from [GitHub](https://github.com/qupath/qupath/releases/latest), you may need to take a few extra steps to get it to run:

- On **Windows**, if you downloaded an `.msi` file then double-click on it to launch the installer
  - If you see a warning, choosing {guilabel}`More info` and {guilabel}`Run anyway` should let you proceed
- On **Windows**, if you downloaded a `.zip` then extract its contents and run the `QuPath.exe` file
- On **macOS**, right-click the `.pkg` file, then choose 'Open' (you might need to do this twice)
  - If you're using an M1/M2/M3 Mac, please check out the [notes on Apple silicon](apple-silicon)
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
:class: shadow-image mid-width

Windows warning
:::

If you would like to get past this screen, press *'More info'* and the option to *'Run anyway'* appears.

:::{figure} images/installing_windows_warning_run_anyway.png
:class: shadow-image mid-width

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
:class: shadow-image mini-image

Gatekeeper on macOS on double-click
:::

You should then see an option to open QuPath that should work.

:::{figure} images/mac-warning-04-override.png
:class: shadow-image mini-image

Gatekeeper on macOS after right-clicking and selecting 'Open'
:::

You may also need to right-click and choose open the first time you run the QuPath app after installation.
Double-clicking should work as normal once it has been run once.

:::{warning}
Since macOS (presumably) has your best interests at heart, circumventing its security settings routinely is probably not advisable.

However, as an open source project, we don't currently have the time and resources needed to distribute QuPath as a signed/notarized app and avoid these warnings.
:::


### Linux

QuPath for Linux was compiled on Ubuntu, with best efforts made to include all dependencies.
