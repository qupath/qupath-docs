# Extensions

(qupath-extensions)=

QuPath supports adding new features via extensions.
These are basically extra plugins that QuPath *can* work without... but often benefits from having.

Extensions provide two main advantages:

* They make it possible to develop and update new features without needing to update the whole software.
  The QuPath dev team use extensions for this purpose.
* They enable other developers to add functionality to QuPath without needing to change the core software.


## Finding extensions

We don't yet have a central list for extensions.
The main places to find out about them are:

* These docs --- some examples include:
  <!-- * [Instanseg](instanseg-extension) -->
  * [StarDist](stardist-extension)
  * [WSInfer](wsinfer-extension)
  * [OMERO](omero-extension)
  * [Deep Java Library](deep-java-library)
  * [Bioimage Model Zoo](bioimage-io)
* The [user forum](https://forum.image.sc/tag/qupath)
* Searching [for QuPath on GitHub](https://github.com/search?q=qupath)

You can view and manage QuPath extensions using the extension manager,
found using {menuselection}`Extensions --> Manage extensions`.

This will open the extension manager window, which will show you a list of installed extensions, and provide options for installing, updating, or removing extensions.

:::{figure} images/extension_manager_empty.png
:class: shadow-image mid-image

The extension manager window
:::

## Installing extensions

Usually whoever has made the extension will provide installation instructions -- but generally it's pretty simple.

For many extensions, you can simply drag & drop the URL of the GitHub repository
from your web browser onto QuPath's main window.
A prompt should appear asking if you want to proceed, and if you do, QuPath will download the extension and install it for you, including some necessary configuration along the way.

Alternatively, if you know the owner and name of the GitHub repository housing an extension, you can enter these in the extension manager and click the download button.
Again, QuPath will ask if you wish to download and install the extension and present you with the versions currently available for that extension.

If you don't have a user directory, QuPath will prompt you to select a folder on your computer to use.
You can change it later under {menuselection}`Edit --> Preferences...` if you want to.

:::{figure} images/extension_manager_installing.png
:class: shadow-image mid-image

Installing the Deep Java Library extension using the extension manager
:::

:::{figure} images/extension_manager_installing_version.png
:class: shadow-image mini-image

An example of extension version options for WSInfer
:::

If both of these extension installation options don't work, you can try downloading the extension manually.
The extension itself is a (usually small) file with that ends with `.jar`, often available from the `Releases` section of the GitHub repository.
If you drag this onto QuPath's main window, QuPath should copy it to your QuPath user directory.

Often the extension will be ready to use immediately, but it's generally a good idea to restart QuPath in case it needs to do any extra work at startup.

## Removing extensions

To remove an extension, you can click the {guilabel}`—` button within the
extension manager -- visible in the example below on the
"Deep Java Library extension".
When clicked, this will prompt QuPath to remove the file on disk relating to this extension.

You should then close and restart QuPath.
Some effects of the extension's code may linger otherwise.

:::{figure} images/extension_manager_installed.png
:class: shadow-image mid-image

Viewing installed extensions in the extension manager, with the option to remove or update them, or to visit the extension's GitHub repository
:::

If this doesn't work, you just need to find the `.jar` file in the user directory and delete it. You can find the user directory using {menuselection}`Extensions --> Manage extensions --> Open extension directory`.
This will probably only work if QuPath isn't running.

At this point, it's best to close QuPath and delete whichever extension files you don't want.

:::{admonition} Did I install that?!
:class: warning

QuPath comes with several built-in extensions (for ImageJ, OpenSlide, Bio-Formats and more). These are found in the main QuPath installation, and not the regular extensions directory.
These are each identified in the extension manager as a "Core extension (part of QuPath)".

You *could* remove them and QuPath should still work... but it's best not to if you want to have all the features available.
:::

## Updating extensions

Not all QuPath extensions can be managed automatically as described above.
If you run into issues installing, updating or removing extensions, it may be best to manually manage the files in the extensions directory.

:::{admonition} Automagic extension updates
For the technically-minded, to enable automatic updates, the main class of an extension should implement the `GitHubProject` interface.
This is used to define the GitHub repository and owner, which is then used to check for updates. If this isn't implemented, QuPath is unable to identify where it should search for updates.
:::