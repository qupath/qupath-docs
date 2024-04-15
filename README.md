# QuPath Docs

This contains the source for QuPath's documentation, hosted at https://qupath.readthedocs.io

## Building locally

To build this locally, create a virtual environment, eg:

```bash
python -m venv ./venv
. ./venv/bin/activate
```

or using conda/mamba:

```bash
conda env create -n qupath-docs
conda activate qupath-docs
```

Then install the requirements for this repo:

```bash
pip install -r requirements.txt
```

You'll also need the command line tool `Make` (e.g., [GNU Make](https://www.gnu.org/software/make/)).

Then, you can run `make` to see available build options.
`make html` will make the HTML version of the website, which is probably the
most useful option.

## License

All original content here is shared under a Creative Commons license ([CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)).

Here's the formal bit:

---

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />Except where otherwise noted, this website is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

---

In some places, the docs include public images from other sources, e.g. within screenshots.
For download links and information about their licenses, see [the Acknowledgements page](https://qupath.readthedocs.io/en/stable/docs/intro/acknowledgements.html).

> All this refers only to the documentation on this repo. 
> For license info about the QuPath *software*, see https://github.com/qupath/qupath
