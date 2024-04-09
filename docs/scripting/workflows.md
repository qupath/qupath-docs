# Workflows

QuPath uses **Workflows** to represent sequences of steps that have been applied to an image.

This includes not only the commands that are run (e.g. `Cell detection`), but also the parameters that are used.

Workflows therefore provide a way to record and standardize how an image is (or should be) analyzed - both so that it is possible to see how the results were generated, and so the same steps can be applied to other images.

## Workflows & the *Command history*

If you have run any kind of analysis within QuPath, you will already have created a workflow - even if you didn't intend to.
This is because QuPath automatically logs many of the commands that are run in a **Command history**, to keep a record of what has been done within an image.

The `Command history` can be found by opening the {guilabel}`Workflow` tab of the `Analysis panel` on the left.

:::{figure} images/command_history.jpg
:class: shadow-image full-image

The `Command history` within QuPath
:::

The **Command history** is an example of a workflow that reflects all (or most...) of what has been done to the currently open image.

Whenever a particular command is selected within this list, a table below updates to show any relevant parameters that are associated with the command, along with the values that were used.

:::{TIP}
The `Command history` is more than just a record: for many commands, double-clicking on the entry within the list results in its dialog box being opened with the same parameters - so that the command can be run again interactively if required.

This is very useful when trying out a command with various settings, by making it possible to go back and revisit previous settings if needed.
:::

## Creating new workflows

Below the {guilabel}`Command history` is a button {guilabel}`Create workflow`.

This makes it possible to create a new workflow based on the `Command history`, but differing from it in one important way: the new workflow can be edited.

:::{NOTE}
In QuPath, as in life, it is neither easy nor wise to rewrite history... because the `Command history` is supposed to be an accurate log of what was actually applied to an image.
:::

:::{figure} images/workflow_orig.png
:class: shadow-image small-image

A workflow created from the `Command history`.
:::

The new workflow is shown in its own panel.
Right-clicking on any entry within a `Workflow` allows some minor editing, e.g. to remove an entry or shift it up or down.

:::{figure} images/workflow_editing.png
:class: shadow-image small-image

Editing a workflow
:::

:::{TIP}
There currently isn't much benefit in editing workflows manually.
It's usually much easier to create a script and edit that... which is the theme of the next section.
:::

## Working with workflows

At this point, workflows may seem a bit underwhelming.
The `Command history` is useful for reproducibility, but beyond that it is not actually possible to do very much with workflows directly, or even to save edited workflows for posterity.

However, even now workflows are already extremely important within QuPath because of one important feature: workflows can be turned into {doc}`scripts <workflows_to_scripts>`.

:::{NOTE}
Since **scripts** are written in the form of code that is much more computer-friendly than it is human-friendly, they aren't particularly appealing - especially to non-programmers.

Future versions of QuPath might try to hide scripts from view more, so that **Workflows** can be run directly... but currently, I'm afraid it's necessary to go through the process of creating a script to achieve automation.
:::
