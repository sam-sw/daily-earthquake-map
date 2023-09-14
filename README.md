# Daily Earthquake Map

Using data sourced from the USGS, a live-updating map of all earthquakes
detected in the last day is produced.


## Installation

Daily Earthquake Map is a static website, so only needs a web server to serve
its files. This repository has separated 'minifiable' files (HTML, CSS, JS,
JSON, etc.) from 'static' files (images, Javascript libraries, etc.). To create
a single directory that can be served with a web server, either:

    1. Copy the contents of `src/` and `static/` to a chosen output directory.
    2. Use the provided Python `build.py` script. This has the added benefit of
        minifying source files.

### The Python `build.py` Script

The build script has been tested with Python 3.10. It has only one dependency:
[minify-html](https://github.com/wilsonzlin/minify-html). To install this,
first create a virtual environment:

```bash
python -m venv venv
```

Then activate it, and install minify-html:

<details>
    <summary>Linux and macOS</summary>

    ```bash
    source venv/bin/activate
    python -m pip install --upgrade pip minify-html
    ```
</details>

<details>
    <summary>Windows</summary>

    ```batchfile
    venv\Scripts\activate
    python -m pip install --upgrade pip minify-html
    ```
</details>

Note: these steps need only be run once. To minify and copy files, first create
an empty build directory in the root of this repository:

```bash
mkdir build
```

Then run the script (making sure you have the Python virtual environment
activated, and are in the root of this repository):

```bash
python build.py src build static
```

The `build` directory should now contain all the minified source files, and a
copy of all the static files. Note you can deactivate your Python virtual
environment (and return back to your usual shell) with:

```bash
deactivate
```


## Contributing

TBC


## License

TBC
