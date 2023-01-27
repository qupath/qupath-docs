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

Bio-Formats supports most images that can be read by OpenSlide, but not all - and therefore QuPath continues to include both libraries.

However, file formats are tricky and tend to have lots of variants. Just because a format is listed as being supported by Bio-Formats or OpenSlide doesn't mean files in that format will always open (properly) in QuPath. The following sections contain some extra details and caveats, partly based on user feedback about what does and doesn't work.

:::{important}
If you're using a QuPath build for **Apple silicon** (i.e. a recent Mac with M1/M2 processor), then you might not have OpenSlide available by default.
Check out <https://github.com/petebankhead/homebrew-qupath> for instructions how to install this.

The same link can also help if you're using another Mac or Linux computer and want to update the version of OpenSlide that QuPath uses.
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

:::{note}
OpenSlide has not been updated for several years, whereas Bio-Formats is actively maintained by the OME team.

**However**, before relying on Bio-Formats to continue supporting and adding proprietary formats forever, one should read the [OME position regarding file formats](https://blog.openmicroscopy.org/community/file-formats/2019/06/25/formats/).
:::

### Specific formats

#### BIF (Ventana)

Both OpenSlide and (more recently) Bio-Formats now support BIF images.
If you have trouble with one library, you might try reading the images with the other.

There have previously been problems with misaligned tiles (see [here](https://github.com/qupath/qupath/issues/323)).

#### CZI (Zeiss)

Since the release of [Bio-Formats v5.3.0](https://www.openmicroscopy.org/site/support/bio-formats5.3/about/whats-new.html) QuPath has been able to work with `.czi` files.

To open CZI files that use JPEG-XR compression on **Windows**, you may also need to install the *Visual Studio 2015 C++ Redistributable* - see [here](https://www.openmicroscopy.org/site/support/bio-formats/formats/zeiss-czi.html) for more information.


#### DICOM

Bio-Formats 6.8.0 introduced support for DICOM whole slide images.
This is available in QuPath from v0.4.0.


#### iSyntax (Philips)

iSyntax is a proprietary format, not compatible with QuPath.
We are unaware of any open source library capable of reading iSyntax files.

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

#### TIFF

TIFF is a file format commonly used for whole slide images, but it is important to recognize that not all TIFFs are the same.
Internally, the data in a TIFF file can be represented quite differently in terms of layout and compression.

Consequently, although OpenSlide and Bio-Formats support many TIFF files, it is quite possible to encounter variants that cannot be opened with QuPath.

Perhaps the most common reason for this is that the file does not contain pyramidal layers, or these layers cannot be automatically recognized.
This is one reason why well-supported, open formats should generally be preferred (e.g. OME-TIFF).

## Open URI

QuPath is not limited to working with image files stored locally.

{menuselection}`File --> Open URI...` provides a way to access some images stored elsewhere, *however* extensions are needed to support different kinds of image server.
A few such extensions exist already, hopefully more will be created in the future by QuPath users.

### OMERO

QuPath includes a built-in extension to work with whole slide images hosted through [OMERO](https://www.openmicroscopy.org/omero/).

To use it, simply find the image you want through the OMERO web viewer, copy the URI, and paste it into the {menuselection}`File --> Open URI...` dialog in QuPath.

There is some additional documentation from the OMERO team in the [OMERO Guide](https://omero-guides.readthedocs.io/en/latest/qupath/docs/).

:::{warning}
OMERO support is via the web API.
This results in several limitations:

- Only RGB images are supported
- Image tiles are JPEG compressed

Essentially, QuPath is requesting image tiles in the same way as the OMERO web viewer.
:::

:::{tip}
QuPath's OMERO support will be improved in future releases.
It is already possible to add URLs in a variety of formats that OMERO can provide.

This makes it possible to import multiple images -- even including some annotations -- to a QuPath {doc}`project <../tutorials/projects>` in one go.
:::

### Community extensions

Extensions have been developed to link QuPath with other image management systems, including:

- **Google Cloud API:** <https://github.com/GoogleCloudPlatform/qupath-chcapi-extension>
- **SlideScore:** <https://github.com/SlideScore/qupath-extension-slidescore>

Note that these are external extensions that have not been tested and cannot be supported by the QuPath developers -- if you have any questions about their use, it is best to contact whoever maintains the relevant extension.

[qupath issues page]: https://github.com/qupath/qupath/issues?utf8=%E2%9C%93&q=label%3A%22file+formats%22
