(supported-image-formats)=
# Supported image formats

## Image files

QuPath can be used with a wide range of image formats, including many whole slide formats, thanks to two essential open source libraries:

- **Bio-formats**: <https://docs.openmicroscopy.org/bio-formats>
- **OpenSlide**: <https://openslide.org>

:::{sidebar} Pyramidal images
QuPath is designed to handle *pyramidal images*.
These are large images with the same data stored at multiple resolutions, so the whole thing does not need to be read into memory at once.
<br />
Whole slide images in pathology are typically pyramidal - although other microscopy images may be as well.

```{image} images/pyramid_small.png
```
:::

Both libraries have their own distinct advantages:

- OpenSlide is typically fast, lightweight and programmer-friendly (especially through Python), but is restricted to *only* 2D, 8-bit, RGB images.
- Bio-Formats can support a much wider range of image types, including multidimensional data (e.g. z-stacks, time series and multiplexed images).

Bio-Formats supports most images that can be read by OpenSlide, but not all.
Also, when both libraries support the same file format, OpenSlide tends to be *slightly* faster.
Therefore QuPath continues to include both libraries.

However, file formats are tricky and tend to have lots of variants.
Just because a format is listed as being supported by Bio-Formats or OpenSlide doesn't mean files in that format will always open (properly) in QuPath.
The following sections contain some extra details and caveats, partly based on user feedback about what does and doesn't work.

:::{important}
:class: warning

If you're using a QuPath build for **Apple silicon** (i.e. a recent Mac with M1/M2/M3/M4 processor), then you might find that *.ndpi* and *.czi* images don't work with Bio-Formats.

There are more details and workaround on the [installation page](qupath-versions-for-mac).
:::

### Reporting problems

Despite the fantastic work of the Bio-Formats and OpenSlide developers, the use of proprietary formats throughout the field means that images often turn up that can't be opened within QuPath.

In some cases, this is simply because the format isn't supported.

```{eval-rst}
.. list-table::
  :header-rows: 1

  * - Library
    - Supported formats
    - Issues page
  * - Bio-Formats
    - `Link <https://docs.openmicroscopy.org/bio-formats/latest/supported-formats.html>`__
    - `GitHub <https://github.com/ome/bioformats/issues>`__
  * - OpenSlide
    - `Link <https://openslide.org>`__
    - `GitHub <https://github.com/openslide/openslide/issues>`__
```

You can also check the [QuPath issues page] for past discussions.

:::{admonition} I've found a bug!
If you find a file that doesn't open properly in QuPath, despite being listed as supported by OpenSlide or Bio-Formats, that's *usually* not something we can fix in QuPath.
Most of the time, a change needs to be made in the library that is reading the file.

**However**, before relying on Bio-Formats to continue supporting and adding proprietary formats forever, you should read the [OME position regarding file formats](https://blog.openmicroscopy.org/community/file-formats/2019/06/25/formats/).
:::

### Specific formats

#### BIF (Ventana)

Both OpenSlide and (more recently) Bio-Formats now support BIF images.
If you have trouble with one library, you might [try reading the images with the other](project-add-images).

There have previously been [problems with misaligned tiles](https://github.com/qupath/qupath/issues/323).

#### CZI (Zeiss)

Since the release of [Bio-Formats v5.3.0](https://www.openmicroscopy.org/site/support/bio-formats5.3/about/whats-new.html) QuPath has been able to work with `.czi` files.
However, for CZI images using JPEG-XR compression (which is common for whole slide images) there are caveats:
* On **Windows**, you may need to install the *Visual Studio 2015 C++ Redistributable* - see [here](https://www.openmicroscopy.org/site/support/bio-formats/formats/zeiss-czi.html) for more information.
* Bio-Formats doens't currently support JPEG-XR for [Apple silicon](qupath-versions-for-mac). You'll either need to convert the images outside of QuPath, or switch to using the Intel build of QuPath for macOS.


#### DICOM

Bio-Formats 6.8.0 introduced support for DICOM whole slide images.
This is available in QuPath from v0.4.0.

OpenSlide 4.0 also added support for DICOM whole slide images.
This is available in QuPath from v0.5.0.


#### iSyntax (Philips)

iSyntax is a proprietary format, not compatible with QuPath.
We aren't aware of any QuPath-compatible open source library capable of reading iSyntax files.

:::{tip}
See [here](https://www.glencoesoftware.com/blog/2019/12/09/converting-whole-slide-images-to-OME-TIFF.html) for a blog post from Glencoe Software about converting iSyntax to OME-TIFF.
:::

#### MRXS (3D HISTECH)

OpenSlide has *some* limited support for MRXS images, but many do not work.
Specifically, 2D, 8-bit, RGB images that do *not* use JPEG-XR compression seem to be ok.
Anything else (e.g. 16-bit fluorescence) is not.

QuPath may still be able to open a low-resolution thumbnail for an unsupported MRXS image, but unfortunately not the full data.

The reasons why Bio-Formats and OpenSlide do not offer better MRXS support may be gleaned from the following links:

- <https://blog.openmicroscopy.org/file-formats/community/2016/01/06/format-support/>
- <https://lists.andrew.cmu.edu/pipermail/openslide-users/2012-July/000377.html>

:::{tip}
See [here](https://www.glencoesoftware.com/blog/2019/12/09/converting-whole-slide-images-to-OME-TIFF.html) for a blog post from Glencoe Software about converting .mrxs to OME-TIFF.
:::

#### NDPI (Hamamatsu)

NDPI is generally quite well supported by both Bio-Formats and OpenSlide.
Note that z-stacks are only supported by Bio-Formats; with OpenSlide, only one plane will be opened.

There is a variation of `.ndpi` with the file extension `.ndpis`.
This is typically used for fluorescence images and only supported by Bio-Formats.

If you're using the [Apple silicon build](qupath-versions-for-mac), Bio-Formats can't read most `.ndpi` or `.ndpis` files. 
Fortunately, OpenSlide's `.ndpi` support means this isn't usually isn't a problem - at least for 2D brightfield images.

#### TIFF

TIFF is a file format commonly used for whole slide images, but it's important to recognize that not all TIFFs are the same.
Internally, the data in a TIFF file can be represented quite differently in terms of layout and compression.

Although OpenSlide and Bio-Formats support many TIFF files, it is quite possible to encounter variants that cannot be opened with QuPath.

Perhaps the most common reason for this is that the file does not contain pyramidal layers, or these layers cannot be automatically recognized.
This is one reason why well-supported, open formats should generally be preferred (e.g. OME-TIFF).

#### OME-Zarr
QuPath version 0.6.0 introduced support for reading and writing [OME-Zarr](https://link.springer.com/article/10.1007/s00418-023-02209-1) images.
This file type was developed by the OME team in collaboration with many individuals and institutes to address the need for a scalable and cloud-friendly large image format.

## Open URI

QuPath is not limited to working with image files stored locally.

{menuselection}`File --> Open URI...` provides a way to access some images stored elsewhere, *however* extensions are needed to support different kinds of image server.
A few such extensions exist already, hopefully more will be created in the future by QuPath users.

### OMERO

QuPath doesn't strictly require images to be files on your local computer.
For example, it can access images hosted through [OMERO](https://www.openmicroscopy.org/omero/).

Check out the [QuPath OMERO extension](omero-extension) page for more details - this received a *major* update for QuPath v0.6.0.

There is some additional documentation from the OMERO team in the [OMERO Guide](https://omero-guides.readthedocs.io/en/latest/qupath/docs/) (at the time of writing, this is for an earlier version of the extension).

### Community extensions

Extensions have been developed to link QuPath with other image management systems, including:

- **Google Cloud API:** <https://github.com/GoogleCloudPlatform/qupath-chcapi-extension>
- **SlideScore:** <https://github.com/SlideScore/qupath-extension-slidescore>

Note that these are external extensions that have not been tested and cannot be supported by the QuPath developers -- if you have any questions about their use, it is best to contact whoever maintains the relevant extension.

[qupath issues page]: https://github.com/qupath/qupath/issues?utf8=%E2%9C%93&q=label%3A%22file+formats%22
