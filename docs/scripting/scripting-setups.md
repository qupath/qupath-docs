# Scripting setups

When writing scripts for QuPath, the script editor built-in to QuPath is
a good option for prototyping scripts. Alternatively, extensions can provide
alternative script editor implementations. However, these are generally somewhat
limited when compared to fully-fledge text editors and IDEs. In this document,
we outline some options for setting up external editing tools with QuPath.

## IntelliJ setup

IntelliJ is an IDE developed by JetBrains for Java, Groovy and Kotlin.
It is very popular and comes in free "Community" and paid "Ultimate" editions,
both of which are broadly similar in functionality when it comes to features
relevant to writing code for QuPath. Importantly, it enables autocomplete,
symbol lookup, and dependency management for complex projects.

To set up IntelliJ for writing QuPath scripts, first download the 
[QuPath gradle scripting project](https://github.com/qupath/qupath-gradle-scripting-project),
using IntelliJ to download the repository or using git directly.

Following this, you should have a project with a simple example script,
but more importantly autocomplete support for most relevant QuPath
classes, and even QuPath's dependencies. However, there is no easy way to
run this code in QuPath yet. To solve this, you can open the same file in both
IntelliJ and QuPath's script editor at the same time.
IntelliJ auto-saves files by default when they are edited. QuPath should
automatically reload the file when these changes are saved to disk.
This enables you to write code with all of the modern conveniences
of a Groovy IDE, and still easily run them as usual in QuPath.

## VSCode setup

VSCode is a text editor that can be used to write code and documents in many
languages. As such, it's a favourite among some QuPath developers.

To use VSCode to write QuPath code, you could just install an extension
that adds groovy syntax highlighting, and call it a day. However, this
will leave you without autocomplete suggestions and other nice features
of modern text editors.

To enable autocomplete, there are a few slightly complex steps.

1. Download a build of `groovy language server` built with a suitable Java
    and groovy version
    [from github](https://github.com/alanocallaghan/groovy-language-server/releases/).
2. Install this extension `.vsix` file manually as described
    [in the Microsoft docs](https://learn.microsoft.com/en-us/visualstudio/ide/finding-and-using-visual-studio-extensions?view=vs-2022).
3. Open VSCode's user settings.
4. Add an entry under `Groovy -> Classpath` in the settings menu, or under
    `groovy.classpath` in the `settings.json`, pointing to the path that contains
    all of the QuPath Jar files, as well as (optionally) the extensions directory.
    For example:
```json
"groovy.classpath": [
"/path/to/QuPath/lib/app/",
"/path/to/QuPath/extensions/"
]
```

As described in the IntelliJ section,
you can now open this file in both VSCode and QuPath's script editor at the
same time. When you manually save the script in VSCode, QuPath should
automatically reload the file. You can run the script as normal from QuPath's
script editor.
