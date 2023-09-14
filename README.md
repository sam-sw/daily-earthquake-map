# Daily Earthquake Map

Live, minute-by-minute data from the [U.S. Geological Survey](https://usgs.gov)
plotted on an interactive map, showing earthquakes from the last day across the
globe.


## Building

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

To minify and copy files, first create an empty build directory in this
repository's root:

```bash
mkdir build
```

Then run the script (making sure you have the Python virtual environment
activated, and are again in this repository's root):

```bash
python build.py src build static
```

The `build` directory should now contain all the minified source files, and a
copy of all the static files. Note you can deactivate your Python virtual
environment (and return back to your usual shell) with:

```bash
deactivate
```


## Deploying

As a static site, only a web server capable of serving files is required. (In
fact, you can run without a web server by loading `build/index.html` in your
browser - only fetching the tectonic plate boundaries fails.) For deploying to
Netlify, a file with HTTP headers is provided
([`static/_headers`](static/_headers)) that has some sensible defaults (such as
disabling embeds, not sending a referrer on external links, and disabling
Google Chrome's browsing history ad-tracking). A
[`robots.txt`](static/robots.txt) is also set up to disable OpenAI's GPTBot
from scraping any text content.


## Contributing

TBC


## License

TBC
