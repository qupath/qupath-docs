(tips-and-tricks)=
# Tips & tricks

This page contains a (growing) collection of tips & tricks that can help make life with QuPath more pleasant.

Some of these are always applicable, while others depend upon which specific operating system you are using.



## macOS

### Conflicting shortcuts
Some of QuPath's shortcuts conflict with built-in shortcuts in macOS.

In particular, the handy shortcut to select all detections is {kbd}`Option`+`Cmd`+`D`.
On a Mac, this tends to show or hide the Dock... leaving the detections just as visible as they were before.

In cases where you don't use the macOS shortcut and want to turn it off, you can do so system-wide under {menuselection}`System Settings --> Keyboard --> Keyboard Shortcuts`.
For example, unchecking {guilabel}`Turn Doc hiding on/off` can enable QuPath's shortcut to function as expected.


### Lost windows
QuPath doesn't play entirely nicely with multiple monitors on macOS.
For example, when dragging a (sub)window (e.g. the Brightness/Contrast dialog) to a different monitor, it might become 'detached' from the main QuPath window.

The {menuselection}`Window --> Center all windows` and {menuselection}`Window --> Center off-screen windows` were introduced in QuPath v0.6.0 to help find windows that might have gotten lost.

The problem is [described on GitHub](https://github.com/qupath/qupath/issues/1785) and is not something that can be fixed entirely within QuPath, since it [relates to JavaFX's behavior](https://bugs.openjdk.org/browse/JDK-8252373).

Nevertheless, there is a macOS system setting that can *influence* the behavior, and so may be worth trying if you find it too annoying.
It is found under {menuselection}`System Settings --> Desktop & Dock --> Displays have separate Spaces`.
