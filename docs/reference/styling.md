# Styling QuPath

Starting with v0.4.0, QuPath can be styled using CSS.
This makes it possible to generate custom themes.

Because *most* colors are derived from a few base ones, it's possible to change quite a bit with just a few tiny tweaks.
The result is not guaranteed to look good, but it can be fun to explore.

The process is

* Create a .css file to define your theme
* Drag the .css file onto QuPath to copy it to your QuPath user directory
  * If you don't have a QuPath user directory defined already (i.e. a place to store styles, logs and extensions) then you'll be prompted to create one
* Select the theme under {menuselection}`Edit --> Preferences...`

```{tip}
This builds on JavaFX's CSS support, which uses `modena.css` as the base theme.
Therefore if you really want to get into the details, check out

* [JavaFX CSS reference](https://openjfx.io/javadoc/19/javafx.graphics/javafx/scene/doc-files/cssref.html)
* [modena.css at OpenJDK](https://github.com/openjdk/jfx/blob/jdk-11+14/modules/javafx.controls/src/main/resources/com/sun/javafx/scene/control/skin/modena/modena.css)
```

## Changing the main color

To see this in action, create a file `Unpleasant blue.css` and add the contents below:

:::css
.root {
    -fx-base: rgb(30, 28, 75);
    -fx-light-text-color: rgb(200, 200, 255);
    -fx-background: derive(-fx-base, -10%);
    -fx-control-inner-background: derive(-fx-base, 10%);
}
:::

Then drag the .css file onto QuPath, and selected it in the preferences.
You should see something like the screenshow below.

:::{figure} images/building-blue-theme.jpg
:align: center
:class: shadow-image
:width: 90%

A rather unpleasant blue theme
:::

This essentially defines a base color, and the color for text to show on top.
Then everything else is derived from these.

To switch to red with white text, you can use the following .css:

```css
.root {
    -fx-base: rgb(130, 28, 25);
    -fx-light-text-color: white;
    -fx-background: derive(-fx-base, -10%);
    -fx-control-inner-background: derive(-fx-base, -10%);
}
```

:::{figure} images/building-red-theme.jpg
:align: center
:class: shadow-image
:width: 90%

Also an unpleasant red theme
:::

## A more complex example

Setting the base color is just the start: there are lots more styles that can be specified to customize different aspects of QuPath's appearance.

[Dracula](https://draculatheme.com) is a popular, [open-source](https://github.com/dracula/dracula-theme) theme that is available for lots of software applications.

The .css below depicts a quick attempt to apply the [colors defined in the dracula spec](https://spec.draculatheme.com) to QuPath, and in particular the script editor.

```css
.root {
    -qp-dracula-selection: #44475A;
    -qp-dracula-comment: #6272A4;
    -qp-dracula-red: #FF5555;
    -qp-dracula-orange: #FFB86C;
    -qp-dracula-yellow: #F1FA8C;
    -qp-dracula-green: #50FA7B;
    -qp-dracula-purple: #BD93F9;
    -qp-dracula-cyan: #8BE9FD;
    -qp-dracula-pink: #FF79C6;

    -fx-base: #282A36;
    -fx-light-text-color: #F8F8F2;
    -fx-background: #282A36;

    -fx-control-inner-background: derive(-fx-base, 10%);
    -fx-control-inner-background-alt: derive(-fx-control-inner-background,1%);

    -fx-accent: -qp-dracula-selection;

    -qp-script-comment-color: -qp-dracula-comment;
    -qp-script-error-color: -qp-dracula-red;
    -qp-script-warn-color: -qp-dracula-orange;
    -qp-script-string-color: -qp-dracula-yellow;
    -qp-script-keyword-color: -qp-dracula-pink;
}
```

:::{figure} images/building-dracula-theme.jpg
:align: center
:class: shadow-image
:width: 90%

A dracula-inspired theme for QuPath
:::

## Updating a theme

When you drag a theme onto QuPath, it's copied to the QuPath user directory - so if you want to update it (or uninstall it), that's where you should look.
Updating your original .css file outside the user directory won't have any effect.

You can find the directory location under {menuselection}`Edit --> Preferences...` and *QuPath user directory*.
Once you've found where it's stored, you can edit a .css file that's set as the current theme in QuPath.

If you do this, QuPath should recognize when changes are saved and automatically update.
This might take a few seconds (particularly on macOS), but provides a way to interactively explore theme changes.