(qupath-extensions)=
# Extensions

QuPath supports adding new features via extensions.
These are basically extra plugins that QuPath *can* work without... but usually benefits from having.

Extensions provide two main advantages:

* They make it possible to develop and update new features without needing to update the whole software. The QuPath dev team use extensions for this purpose.
* They enable other developers to add functionality to QuPath without needing to change the core software.


## Finding extensions

We don't yet have a central list for extensions.
The main places to find out about them are:

* these docs (e.g. [StarDist](stardist-extension), [OMERO](omero-extension), [Deep Java Library](deep-java-library) & [Bioimage Model Zoo](bioimage-io) extensions)
* the [user forum](https://forum.image.sc/tag/qupath)
* searching [for QuPath on GitHub](https://github.com/search?q=qupath)


## Installing extensions

Usually whoever has made the extension will provide installation instructions - but generally it's pretty simple.
The extension itself is a (usually small) file with that ends with `.jar`.

If you drag this onto QuPath's main window, QuPath should copy it to your QuPath user directory.
If you don't have a user directory, QuPath will prompt you to select a folder on your computer to use.
You can change it later under {menuselection}`Edit --> Preferences...` if you want to.

Often the extension will be ready to use immediately, but it's generally a good idea to restart QuPath in case it needs to do any extra work at startup.

## Removing extensions

To remove an extension, you just need to find the `.jar` file in the user directory and delete it.
This will probably only work if QuPath isn't running.

If you aren't sure where it is, use {menuselection}`Extensions --> Installed extensions` to find the location.
You can click the little arrow that appears next to the extension you want to get rid of, and the full file path should appear.
If you double-click that, you should be transported to the folder automatically.

At this point, it's best to close QuPath and delete whichever extension files you don't want.

:::{admonition} Did I install that?!
QuPath comes with several built-in extensions (for ImageJ, OpenSlide, Bio-Formats and more).
These are found in the main QuPath installation, and not the regular extensions directory. 

You *could* remove them and QuPath should still work... but it's best not to if you want to have all the features available.
:::

## Updating extensions

QuPath doesn't yet have a nice way to manage extensions, and is (unfortunately) not yet smart enough to know when duplicate extensions are present.
Therefore if you want to update any extensions, you should manually remove the old version (as described above) and then install the new one.
