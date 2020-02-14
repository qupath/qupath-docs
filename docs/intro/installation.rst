************
Installation
************

==================
Download & install
==================

Download QuPath for your platform (Windows, Linux, macOS) from `GitHub <https://github.com/qupath/qupath/releases/latest>`_ and install 'as normal':

* On **Windows**, if you downloaded an ``.msi`` file then double-click on it to launch the installer
* On **Windows**, if you downloaded a ``.zip`` then extract its contents and run the ``QuPath.exe`` file
* On **macOS**, double-click on the ``.dmg`` file and drag ``QuPath.app`` to wherever you want to keep it
* On **Linux**, download and extract the ``.tar.xz`` file


=============
Setup options
=============

When running QuPath for the first time, you will be prompted to specify some setup options.

.. figure:: images/setup_memory.jpg
  :class: shadow-image
  :width: 75%
  :align: center

  Setup options shown on startup

The default is that QuPath will request 50% of the total memory available.
This is generally a reasonable choice, but be aware that the amount of memory available to QuPath is one of the main factors influencing how well the software will perform - and how complex the analysis can be.

.. sidebar:: Why does the 'Region' matter?

  See `here <https://github.com/qupath/qupath/issues/18>`_ for a note explaining why the *Region* setting exists.

You can also specify the *Region*, where it is recommended to leave the default of *English (United States)* for consistency.

This will help ensure behavior should match with what is shown in this documentation, and seen by other users on the forum.

.. tip::
  You can revisit the setup options later under :menuselection:`Help --> Show setup options`

.. tip::
  If you encounter trouble, :menuselection:`Edit --> Reset preferences` can be more effective than reinstalling.


============================
Troubleshooting installation
============================


Windows (.zip)
==============

If QuPath does not start, make sure that you are not trying to run it directly from within the ``.zip`` file that you downloaded.
It is important to first *extract* the files into their own 'QuPath' folder, and then run ``QuPath.exe`` from within that.


Windows (.msi)
==============

The QuPath installer gives a scary warning
------------------------------------------

It is expected that Windows will give a scary-looking warning whenever the QuPath installer is first run, as it tries to protect you from software it does not know.

.. figure:: images/installing_windows_warning.png
  :class: shadow-image
  :align: center

  Windows warning

If you would like to get past this screen, press *'More info'* and the option to *'Run anyway'* appears.

.. figure:: images/installing_windows_warning_run_anyway.png
  :class: shadow-image
  :align: center

  Windows warning run anyway


The QuPath installer does not start
-----------------------------------

If the QuPath installer does not start at all, you may not have administrator privileges on your computer - and therefore cannot install it.  Try downloading the ``.zip`` file instead, which should not need such privileges.

.. NOTE::
    Running QuPath on 32-bit Windows is not supported.


macOS
=====
Mac users may see a similar security message to that experienced by Windows users running the QuPath installer:

.. figure:: images/installing_macOS_open.png
  :align: center

  Gatekeeper on macOS on double-click.

If this happens, you can try right-clicking on the QuPath icon and select *Open* from the popup menu that appears.
You should then see an option to open QuPath that should work.

.. figure:: images/installing_macOS_open_right_click.png
  :align: center

  Gatekeeper on macOS after right-clicking and selecting 'Open'.


.. note::
    This alternative method to start QuPath should only be necessary the first time you run it - double-clicking as normal should work afterwards.


Linux
=====

QuPath for Linux was compiled on Ubuntu, with best efforts made to include all dependencies, although in the case of OpenSlide this wasn't entirely successful.
You may need to install OpenSlide separately through your package manager.
