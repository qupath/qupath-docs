# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'QuPath'
copyright = '2019-2023, QuPath docs authors'
author = 'QuPath authors'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx_rtd_theme',
    'sphinx_design',
    'sphinx.ext.autosectionlabel',
    'sphinx_search.extension'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


html_theme_options = {
    'style_nav_header_background': '#343131'
}

html_css_files = [
    'css/custom.css',
]

master_doc = 'index'

rst_prolog = """
.. |br| raw:: html

  <br/>

.. |vertical_ellipsis| unicode:: 0x22EE

.. |copyright| unicode:: 0xA9
"""

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
#    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]


highlight_language = 'groovy'

html_logo = 'docs/images/qupath_128.png'

html_favicon = 'docs/images/QuPath.ico'

release = '0.4.2'
version = '0.4'

# myst_heading_anchors = 2

myst_substitutions = {

  "rectangle": '<img src="../images/icons/Rectangle.png" />',
  "icon_rectangle": '<img src="../images/icons/Rectangle.png" class="inline-icon" />',

  "ellipse": '<img src="../images/icons/Ellipse.png" />',
  "icon_ellipse": '<img src="../images/icons/Ellipse.png" class="inline-icon" />',

  "line": '<img src="../images/icons/Line.png" />',
  "icon_line": '<img src="../images/icons/Line.png" class="inline-icon" />',

  "polygon": '<img src="../images/icons/Polygon.png" />',
  "icon_polygon": '<img src="../images/icons/Polygon.png" class="inline-icon" />',

  "brush": '<img src="../images/icons/Brush.png" />',
  "icon_brush": '<img src="../images/icons/Brush.png" class="inline-icon" />',

  "wand": '<img src="../images/icons/Wand.png" />',
  "icon_wand": '<img src="../images/icons/Wand.png" class="inline-icon" />',

  "points": '<img src="../images/icons/Points.png" />',
  "icon_points": '<img src="../images/icons/Points.png" class="inline-icon" />',

  "move": '<img src="../images/icons/Move.png" />',
  "icon_move": '<img src="../images/icons/Move.png" class="inline-icon" />',

  "grid": '<img src="../images/icons/Grid.png" />',
  "icon_grid": '<img src="../images/icons/Grid.png" class="inline-icon" />',

  "measure": '<img src="../images/icons/Measure.png" />',
  "icon_measure": '<img src="../images/icons/Measure.png" class="inline-icon" />',

  "table": '<img src="../images/icons/Table.png" />',
  "icon_table": '<img src="../images/icons/Table.png" class="inline-icon" />',

  "cog": '<img src="../images/icons/Cog.png" />',
  "icon_cog": '<img src="../images/icons/Cog.png" class="inline-icon" />',

  "annotations": '<img src="../images/icons/Annotations.png" />',
  "icon_annotations": '<img src="../images/icons/Annotations.png" class="inline-icon" />',

  "detections": '<img src="../images/icons/Detections.png" />',
  "icon_detections": '<img src="../images/icons/Detections.png" class="inline-icon" />',

  "annotations_fill": '<img src="../images/icons/Annotations_fill.png" />',
  "icon_annotations_fill": '<img src="../images/icons/Annotations_fill.png" class="inline-icon" />',

  "detections_fill": '<img src="../images/icons/Detections_fill.png" />',
  "icon_detections_fill": '<img src="../images/icons/Detections_fill.png" class="inline-icon" />',

  "tma_grid": '<img src="../images/icons/TMA_grid.png" />',
  "icon_tma_grid": '<img src="../images/icons/TMA_grid.png" class="inline-icon" />',

  "screenshot": '<img src="../images/icons/Screenshot.png" />',
  "icon_screenshot": '<img src="../images/icons/Screenshot.png" class="inline-icon" />',

  "extract_image": '<img src="../images/icons/Extract_image.png" />',
  "icon_extract_image": '<img src="../images/icons/Extract_image.png" class="inline-icon" />',

  "contrast": '<img src="../images/icons/Contrast.png" />',
  "icon_contrast": '<img src="../images/icons/Contrast.png" class="inline-icon" />',

  # "polyline": '<img src="../images/icons/Polyline.png" />',
  # "icon_polyline": '<img src="../images/icons/Polyline.png" class="inline-icon" />',
}