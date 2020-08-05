***************
QuPath versions
***************

This page contains some background on how QuPath's version numbers work.
This can help if you want to reproduce analysis done by someone else, or decide whether you should update the software when in the middle of a project.

.. tip::
  
  When you publish work using QuPath, :doc:`cite the paper <citing>` and mention the version you used!



A version in three parts
************************

The current QuPath version is |release|.

This is made up of three parts: MAJOR.MINOR.PATCH, based on `semantic versioning`_

For practical purposes, the general rules are:

* An updated PATCH means bugs have been fixed... *you probably want these fixes now!*
* An updated MAJOR or MINOR version means the software has changed more substantially.

For reproducibility, you *shouldn't* mix the analysis of images using different MAJOR or MINOR versions within the same project or analysis study.
The results of commands (e.g. cell detection or classification) or scripts might be different.

For that reason, if you're in the middle of a project and a new MAJOR or MINOR version is released you might not want to update immediately... unless you're prepared to redo your analysis in the latest version.

But you probably *do* want to update a PATCH, since that indicates something was broken and should now be fixed.
You can find out what exactly was fixed by checking the changelog_.

.. admonition:: What about annotations?

  If you have laboriously drawn a lot of annotations, you probably don't want to draw them again.
  In this case, the key thing is usually that the correct regions are marked -- not the process (or software) by which they have been marked.
  
  In general, it should be possible to transfer annotations made by older versions of QuPath into the latest release.
      


A commitment of sorts
*********************

.. sidebar:: The path to v1.0.0
  
  The MAJOR version of QuPath is 0... indicating it is still at an early stage of development.
  
  Since QuPath is free, open source, and developed in academia, its long-term development depends on whether funding can be found.

  To help, please be sure to :doc:`cite the paper <citing>` when you use it!


As developers, we try to keep these rules in mind when changing the software.

We are continually working on new MAJOR/MINOR releases, updated to add features -- which are often inspired by our own needs and research projects we are working on.
We're still learning what a plausible schedule is, but we expect two or three such releases per year.

Between MAJOR/MINOR releases we will try to fix critical bugs, and include these in regular PATCH releases -- approximately one per month, depending upon how much is fixed and how important it is.
We will resist the temptation to add new features in a PATCH, particularly if there is a risk these changes might modify the behavior of the software unexpectedly.

This means you can update PATCH versions and not expect huge differences.
We will try to fix bugs promptly, but we can only fix the problems we know about.

In return, **you can help** in a few ways:

* Always check the changelog_ to see what is different in a version. That way you can reduce surprises when updating, and see if an earlier bug affected a feature you used.
* Please report bugs and weirdness that you find on the forum_ -- *after* checking `GitHub Issues`_ to see if it has already been reported or fixed. If you find the issue already exists, but hasn't been resolved, feel free to join in the discussion.
* Do keep in mind that QuPath is developed by researchers, and our time is very limited. If you want a grand new feature, we probably can't spend weeks developing it for you for free... even if we want to. But we're open to discussing ways to collaborate. Talk to us -- the earlier the better.


.. _semantic versioning: https://semver.org
.. _forum: http://forum.image.sc/tag/qupath
.. _changelog: https://github.com/qupath/qupath/blob/master/CHANGELOG.md
.. _Github Issues: http://forum.image.sc/tag/qupath
