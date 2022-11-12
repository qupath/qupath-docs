# Shortcuts

QuPath would like you to be able to work easily with your images, and not get in your way.

Learning the shortcut keys for the tools and commands you use most frequently can help a lot to get things done quickly, and with less frustration.

## Viewer shortcuts

The following shortcuts apply to the viewer.  They are worth remembering, because they can be used *very frequently* when navigating and annotating images.

:::{NOTE}
These shortcuts only work whenever the viewer is 'in focus', i.e. it is the last thing that was clicked.  If a shortcut doesn't seem to work, click on the viewer once to bring it into focus, then try the shortcut again.
:::

### Drawing & navigation

```{eval-rst}
.. csv-table::
  :header: "Tool", "Shortcut"
  :align: center

  "Move", :kbd:`M`
  "Move (temporary)", :kbd:`Spacebar`
  "Rectangle", :kbd:`R`
  "Ellipse", :kbd:`O`
  "Line", :kbd:`L`
  "Polygon", :kbd:`P`
  "Polyline", :kbd:`V`
  "Brush", :kbd:`B`
  "Wand", :kbd:`W`
  "Points", :kbd:`.`


```

:::{sidebar} Note for Linux users
Replace {kbd}`Alt` with {kbd}`Alt + Super` (thanks to [Philipp Tschandl for this](https://groups.google.com/d/msg/qupath-users/QB03tHjRrZs/od-nL_9SBQAJ)).
:::

### The {kbd}`Alt` key

- When the *Move* tool is selected, use the {kbd}`Alt` key to click on multiple objects to select them.
- When the *Brush* or *Wand* tools are selected, use the {kbd}`Alt` key to switch to 'eraser' mode when drawing.

### The {kbd}`Shift` key

- When the *Brush* or *Wand* tools are selected, use the {kbd}`Shift` key to continue adding to an existing selected annotation (rather than creating a new one).

### Display shortcuts

The following shortcuts are used to toggle on/off display elements in the viewer.

```{eval-rst}
.. csv-table::
  :header: "Action", "Shortcut"
  :align: center

  "Show/hide detections", :kbd:`H`
  "Show/hide annotations", :kbd:`A`
  "Show/hide TMA grid", :kbd:`G`
  "Show/hide counting grid", :kbd:`Shift + G`
  "Show/hide pixel classification", :kbd:`C`
  "Fill/unfill detections", :kbd:`F`
  "Fill/unfill annotations", :kbd:`Shift + F`
  "Show/hide color channel", :kbd:`Numeric keys`

```

## Command shortcuts

The following shortcuts trigger commands that can also be accessed within the QuPath menus.

Because the shortcuts are shown in the menus as well, only a small number of the most important are shown here to draw attention to them - subjectively ordered according to usefulness.

### Main QuPath window

```{eval-rst}
.. csv-table::
  :header: "Command", "Shortcut"
  :align: center

  :menuselection:`File --> Save`, :kbd:`Ctrl + S`
  :menuselection:`File --> Reload data`, :kbd:`Ctrl + R`
  :menuselection:`View --> Show command list`, :kbd:`Ctrl + L`
  :menuselection:`View --> Brightness/Contrast`, :kbd:`Shift + C`
  :menuselection:`View --> Show log`, :kbd:`Ctrl + Shift + L`
  :menuselection:`Objects --> Duplicate annotation`, :kbd:`Shift + D`
  :menuselection:`Objects --> Restore last annotation`, :kbd:`Shift + E`
  :menuselection:`Objects --> Create full image annotation`, :kbd:`Ctrl + Shift + A`
  :menuselection:`Objects --> Select --> Reset selection`, :kbd:`Ctrl + Shift + R`
  :menuselection:`Classify --> Create detection classifier`, :kbd:`Ctrl + Shift + D`



```

## Scripting shortcuts

### Script editor menus

The *Script editor* has its own menubar, which supports the followings shortcuts when in focus.

```{eval-rst}
.. csv-table::
  :header: "Command", "Shortcut"
  :align: center

  :menuselection:`Run --> Run`, :kbd:`Ctrl + R`
  :menuselection:`File --> Save`, :kbd:`Ctrl + S`
  :menuselection:`File --> Close script`, :kbd:`Ctrl + W`
  :menuselection:`Edit --> Find`, :kbd:`Ctrl + F`


```

### Autocompletion

There is an additional shortcut that can be very helpful when typing code in the *Script editor* window: for any built-in function, start typing the name and then press {kbd}`Ctrl + Spacebar`.

If the script editor can find the function you are aiming at, it should then auto-complete the name.  If there are multiple options, press {kbd}`Ctrl + Spacebar` repeatedly to cycle through them.

For example, starting to type

```groovy
cells = getC
```

and pressing {kbd}`Ctrl + Spacebar` should automatically produce

```groovy
cells = getCellObjects
```

Pressing {kbd}`Ctrl + Spacebar` again immediately would produce

```groovy
cells = getColorRGB
```

Probably not what you want in this case, admittedly, but useful to know.
Especially if, like me, you often do not *quite* remember the function name or capitalization used.
