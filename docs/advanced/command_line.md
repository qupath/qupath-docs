# Command line

QuPath is *mostly* designed to be an interactive application, and this remains the main priority.

However, a new command line was introduced in v0.2.0 and further improved in v0.3.0, which makes it possible to:

- Launch QuPath with specific options (e.g. a logging level)
- Run scripts headlessly
- Convert images to OME-TIFF
- Specify script parameters with the `--args` option ([#676](https://github.com/qupath/qupath/pull/676))
- Make contents of any extensions directory available to the classloader
- Return a non-zero exit code if an exception is thrown ([#654](https://github.com/qupath/qupath/issues/654))

:::{tip}
The order in which command line arguments are passed can be important.
See [this forum post](https://forum.image.sc/t/unexpected-command-line-usage-in-0-2-0-m10-and-greater/38548/2).
:::

## Viewing command line options

The general way to view the command line options is with:

```bash
QuPath-0.4.3 --help
```

And as of QuPath {{ env.config.release }}, the following information is returned:
```text
Usage: QuPath [-hqrtV] [-i=<image>] [-l=<logLevel>] [-p=<project>] [COMMAND]
  -h, --help                Show this help message and exit.
  -i, --image=<image>       Launch QuPath and open the specified image.
                            This should be the image name if a project is also
                              specified, otherwise it should be the full image
                              path.
  -l, --log=<logLevel>      Log level (default = INFO).
                            Options: TRACE, DEBUG, INFO, WARN, ERROR, ALL, OFF
  -p, --project=<project>   Launch QuPath and open specified project.
  -q, --quiet               Launch QuPath quietly, without setup dialogs,
                              update checks or messages.
  -r, --reset               Reset all QuPath preferences.
  -t, --tma                 Launch standalone viewer for TMA summary results.
  -V, --version             Print version information and exit.
Commands:
  help         Display help information about the specified command.
  script       Runs script for a given image or project.
  convert-ome  Converts an input image to OME-TIFF.

Copyright(c) The Queen's University Belfast (2014-2016)
Copyright(c) QuPath developers (2017-2022)
Copyright(c) The University of Edinburgh (2018-2022)
```


However, there are some platform-specific details on Windows and Mac.

### Windows

On Windows, there are two executable files for QuPath.
It is necessary to use *"QuPath (console).exe"* here to be able to view the output, e.g.

```bash
"QuPath-0.4.3 (console).exe" --help
```

:::{figure} images/command_line_win.png
:align: center
:class: shadow-image
:width: 80%
:::
&NewLine;

Also, when using the *PowerShell* command line interface instead of *Command Prompt*, the QuPath executable name must be preceded with an ampersand otherwise parser errors such as `ParentContainsErrorRecordException` may occur.
See [this forum post](https://forum.image.sc/t/running-qupath-using-command-line-interface/72518/6).

```powershell
& 'QuPath-0.3.0-SNAPSHOT (console).exe' --help
```

### Mac

On macOS, the executable is buried inside the `.app` file and therefore you need something like:

```bash
./QuPath-0.4.3.app/Contents/MacOS/QuPath-0.4.3 --help
```

:::{figure} images/command_line_mac.png
:align: center
:width: 95%
:::

## Subcommands

Some of the command line functionality is available via *subcommands*, such as `script`.
Help is available for these separately.

```bash
QuPath-0.4.3 script --help
```

```text
Usage: QuPath script [-hs] [-c=command] [-i=image] [-p=project]
                     [-a=arguments]... [-e=server-arguments]... [script]
Runs script for a given image or project.
By default, this will not save changes to any data files.
      [script]            Path to the script file (.groovy).
  -a, --args=arguments    Arguments to pass to the script, stored in an 'args'
                            array variable. Multiple args can be passed by
                            using --args multiple times, or by using a "[quoted,
                            comma,separated,list]".
  -c, --cmd=command       Groovy script passed as a string
  -e, --server=server-arguments
                          Arguments to pass when building an ImageSever (only
                            relevant when using --image). For example, --server
                            "[--classname,BioFormatsServerBuilder,--series,2]"
                            may be used to read the image with Bio-Formats and
                            extract the third series within the file.
  -h, --help              Show this help message and exit.
  -i, --image=image       Apply the script to the specified image.
                          This should be the image name if a project is also
                            specified, otherwise it should be the full image
                            path.
  -p, --project=project   Path to a project file (.qpproj).
  -s, --save              Request that data files are updated for each image in
                            the project.
```

:::{tip}
The `--save` option is necessary in order to save any changes made to the project image(s). See [this forum post](https://forum.image.sc/t/creating-project-from-command-line/45608/45) for example.
:::

## Passing arguments to scripts
QuPath v0.3.0 introduced support for passing arguments to scripts using the `--args` keyword. Multiple args can be passed by using the keyword multiple times, or by using a "[comma,separated,list]".

Examples of use are:

```bash
QuPath-0.4.3 script -c "print 'hello ' + args" --args something --args here 
```

```bash
QuPath-0.4.3 script -c "print 'hello ' + args" --args "[something,else,here]" 
```

`--server` can also be used to pass arguments when constructing the ImageServer with the `--image` option.
For example, `--server "[--classname,qupath.lib.images.servers.bioformats.BioFormatsServerBuilder,--series,2]"` has the effect of using Bio-Formats to read the 3rd series of an image.

:::{tip}
In a script, the size of the `args` variable can be queried and returns 0 if no arguments were passed via the command line. For example, the output shown by the following command:

```bash
QuPath-0.4.3 script -c "if (args.size()==0) print 'No arguments' else print 'hello ' + args"
```

:::

