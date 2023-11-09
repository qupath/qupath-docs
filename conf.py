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
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]


highlight_language = 'groovy'

html_logo = 'docs/images/qupath_128.png'

html_favicon = 'docs/images/QuPath.ico'

release = '0.5.0'
version = '0.5'

# myst_heading_anchors = 2

myst_substitutions = {

    "rectangle": '<img src="../images/icons/RECTANGLE_TOOL.png" />',
    "icon_rectangle": '<img src="../images/icons/RECTANGLE_TOOL.png" class="inline-icon" />',
    "tool_rectangle": '<img src="../images/icons/RECTANGLE_TOOL.png" class="tool-icon" />',

    "ellipse": '<img src="../images/icons/ELLIPSE_TOOL.png" />',
    "icon_ellipse": '<img src="../images/icons/ELLIPSE_TOOL.png" class="inline-icon" />',
    "tool_ellipse": '<img src="../images/icons/ELLIPSE_TOOL.png" class="tool-icon" />',

    "line": '<img src="../images/icons/LINE_TOOL.png" />',
    "icon_line": '<img src="../images/icons/LINE_TOOL.png" class="inline-icon" />',
    "tool_line": '<img src="../images/icons/LINE_TOOL.png" class="tool-icon" />',

    "polygon": '<img src="../images/icons/POLYGON_TOOL.png" />',
    "icon_polygon": '<img src="../images/icons/POLYGON_TOOL.png" class="inline-icon" />',
    "tool_polygon": '<img src="../images/icons/POLYGON_TOOL.png" class="tool-icon" />',

    "polyline": '<img src="../images/icons/POLYLINE_TOOL.png" />',
    "icon_polyline": '<img src="../images/icons/POLYLINE_TOOL.png" class="inline-icon" />',
    "tool_polyline": '<img src="../images/icons/POLYLINE_TOOL.png" class="tool-icon" />',

    "brush": '<img src="../images/icons/BRUSH_TOOL.png" />',
    "icon_brush": '<img src="../images/icons/BRUSH_TOOL.png" class="inline-icon" />',
    "tool_brush": '<img src="../images/icons/BRUSH_TOOL.png" class="tool-icon" />',

    "wand": '<img src="../images/icons/WAND_TOOL.png" />',
    "icon_wand": '<img src="../images/icons/WAND_TOOL.png" class="inline-icon" />',
    "tool_wand": '<img src="../images/icons/WAND_TOOL.png" class="tool-icon" />',

    "points": '<img src="../images/icons/POINTS_TOOL.png" />',
    "icon_points": '<img src="../images/icons/POINTS_TOOL.png" class="inline-icon" />',
    "tool_points": '<img src="../images/icons/POINTS_TOOL.png" class="tool-icon" />',

    "move": '<img src="../images/icons/MOVE_TOOL.png" />',
    "icon_move": '<img src="../images/icons/MOVE_TOOL.png" class="inline-icon" />',
    "tool_move": '<img src="../images/icons/MOVE_TOOL.png" class="tool-icon" />',

    "selection_mode": '<img src="../images/icons/SELECTION_MODE.png" />',
    "icon_selection_mode": '<img src="../images/icons/SELECTION_MODE.png" class="inline-icon" />',
    "tool_selection_mode": '<img src="../images/icons/SELECTION_MODE.png" class="tool-icon" />',

    "help": '<img src="../images/icons/HELP.png" />',
    "icon_help": '<img src="../images/icons/HELP.png" class="inline-icon" />',
    "tool_help": '<img src="../images/icons/HELP.png" class="tool-icon" />',

    "log": '<img src="../images/icons/LOG_VIEWER.png" />',
    "icon_log": '<img src="../images/icons/LOG_VIEWER.png" class="inline-icon" />',
    "tool_log": '<img src="../images/icons/LOG_VIEWER.png" class="tool-icon" />',

    "grid": '<img src="../images/icons/GRID.png" />',
    "icon_grid": '<img src="../images/icons/GRID.png" class="inline-icon" />',

    "measure": '<img src="../images/icons/MEASURE.png" />',
    "icon_measure": '<img src="../images/icons/MEASURE.png" class="inline-icon" />',

    "table": '<img src="../images/icons/TABLE.png" />',
    "icon_table": '<img src="../images/icons/TABLE.png" class="inline-icon" />',

    "cog": '<img src="../images/icons/COG.png" />',
    "icon_cog": '<img src="../images/icons/COG.png" class="inline-icon" />',

    "annotations": '<img src="../images/icons/ANNOTATIONS.png" />',
    "icon_annotations": '<img src="../images/icons/ANNOTATIONS.png" class="inline-icon" />',

    "detections": '<img src="../images/icons/DETECTIONS.png" />',
    "icon_detections": '<img src="../images/icons/DETECTIONS.png" class="inline-icon" />',

    "annotations_fill": '<img src="../images/icons/ANNOTATIONS_FILL.png" />',
    "icon_annotations_fill": '<img src="../images/icons/ANNOTATIONS_FILL.png" class="inline-icon" />',

    "detections_fill": '<img src="../images/icons/DETECTIONS_FILL.png" />',
    "icon_detections_fill": '<img src="../images/icons/Detections_fill.png" class="inline-icon" />',

    "tma_grid": '<img src="../images/icons/TMA_GRID.png" />',
    "icon_tma_grid": '<img src="../images/icons/TMA_GRID.png" class="inline-icon" />',

    "screenshot": '<img src="../images/icons/SCREENSHOT.png" />',
    "icon_screenshot": '<img src="../images/icons/SCREENSHOT.png" class="inline-icon" />',

    "extract_image": '<img src="../images/icons/EXTRACT_REGION.png" />',
    "icon_extract_image": '<img src="../images/icons/EXTRACT_REGION.png" class="inline-icon" />',

    "contrast": '<img src="../images/icons/CONTRAST.png" />',
    "icon_contrast": '<img src="../images/icons/CONTRAST.png" class="inline-icon" />',

    "play": '<img src="../images/icons/PLAYBACK_PLAY.png" />',
    "icon_play": '<img src="../images/icons/PLAYBACK_PLAY.png" class="inline-icon" />',

    "stop": '<img src="../images/icons/TRACKING_STOP.png" />',
    "icon_stop": '<img src="../images/icons/TRACKING_STOP.png" class="inline-icon" />',

    "record": '<img src="../images/icons/TRACKING_RECORD.png" />',
    "icon_record": '<img src="../images/icons/TRACKING_RECORD.png" class="inline-icon" />',

}
