********************
Building from source
********************

Building software can be tricky, but hopefully this won't be - thanks to Gradle_.

.. _Gradle: http://gradle.org

The following instructions assume:

* You're starting from scratch
* You're not an expert in building software

If you *are* an expert, you'll know which steps you can skip or amend.

.. admonition:: Do you need this?!

  Most people using QuPath won't need to build QuPath from source!
  Just download an existing installer from `qupath.github.io <https://qupath.github.io>`__ and use that instead.

.. important::
  
  **These instructions are for QuPath v0.2 only!** |br|
  For later releases, switch to the latest version of the QuPath docs on ReadTheDocs.

================================
Step 1: Installing prerequisites
================================

Install a Java Development Kit (JDK)
====================================

QuPath v0.2 requires **OpenJDK 14** (the `exact version is important! <https://github.com/qupath/qupath/issues/615>`_).

There are a few places where you can find pre-built OpenJDK binaries -- a popular source is AdoptOpenJDK_.


.. _AdoptOpenJDK: https://adoptopenjdk.net/

.. tip::

  During installation you may be asked if you want to add the JDK to your PATH.
  It usually makes things easier if you do.

  If you can't (e.g. because of some other Java software needing the PATH set to something else) I'm afraid I'll leave resolving that up to you.
  
.. warning::
  
  Problems have been reported on Linux using some JDK distributions.
  Switching to HotSpot (rather than OpenJ9) may help -- see `here <https://github.com/qupath/qupath/issues/484>`_ for more details.


==================================
Step 2: Get the QuPath source code
==================================

You can get the source code for QuPath v0.2.3 from https://github.com/qupath/qupath/releases/tag/v0.2.3

Use the *Source code (zip)* or *Source code (tar.gz)* links.


================================
Step 3: Build QuPath with Gradle
================================

Open the QuPath source directory in a command prompt
====================================================

You now need to unzip the source code subdirectory, then open a command prompt and navigate to the directory.

On Windows, the steps in more detail are

* Right-click on the source zip file, then choose the option to extract the contents
* Open a command prompt
* Type ``cd`` followed by a space in the prompt window, then drag the unzipped directory onto the window to have it automatically fill in the right path.
* Press :kbd:`Enter`

On a Mac, the process is similar except the command prompt is called *Terminal*.


Run gradlew
===========

At the command prompt, type the following on Windows:

.. code-block:: bash

  gradlew clean build createPackage

Or on macOS/Linux type

.. code-block:: bash

  ./gradlew clean build createPackage

This will download Gradle and all its dependencies, so may take a bit of time (and an internet connection) the first time you run it.

If all goes well, you should see a triumphant message that the build was successful.

.. figure:: images/building-success.png
  :class: shadow-image
  :align: center
  :width: 50%

Afterwards, you should find QuPath inside the ``./build/dist`` subdirectory.  You may then drag it to a more convenient location.

**Congratulations!** You've now built QuPath, and can run it as normal from now on... at least until there is another update, when you can repeat the (hopefully painless) process.

----

======
Extras
======

Variations & troubleshooting
============================

The code above should create everything you need to run QuPath.

If you want an installer instead, you can use

.. code-block:: bash

  gradlew createPackage -Ptype=installer

Note that for this to work on Windows you'll need to install `WIX Toolset`_.

.. _WIX Toolset: https://wixtoolset.org/

Inevitably, things will go wrong at some point.
When this happens, it's worth running

.. code-block:: bash

  gradlew clean

once or twice extra to clean up old files that could be causing trouble.



Building javadocs
=================

To generate javadocs for the source code, use

.. code-block:: bash

  gradlew mergedJavadocs

This will generate html javadocs in a ``./build/merged-docs`` subdirectory.

If you'd like to include external links to other relevant javadocs (e.g. for the JDK, ImageJ, JTS) use

.. code-block:: bash

  gradlew mergedJavadocs -PlinkJavadoc=true
