# Daily Earthquake Map

Live, minute-by-minute data from the [U.S. Geological Survey](https://usgs.gov)
plotted on an interactive map, showing earthquakes from the last day across the
globe. Visit the map at [earthquakes.samwood.me](https://earthquakes.samwood.me)
or by clicking on the screenshot below.

[![A screenshot of the Daily Earthquake Map website. The world map is centred about 0° latitude, 0° longitude, with North pointing upwards. Open Street Map's default tiles are used for the basemap; the sea is a pale blue and the land is beige. Locations of recent seismic activity are marked with red circles. The bigger the circles, the stronger the seismic activity. The more opaque the circles, the more recent the seismic activity. Thick grey lines span the whole map, indicating the boundaries of tectonic plates; this demonstrates how seismic activity is more concentrated around these plate boundaries. Text in the upper-right-hand corner includes timestamps for the current data, the number of earthquakes from this update, and an accuracy disclaimer. Copyright and licensing information are shown at the bottom of the screen.](screenshot.png)](https://earthquakes.samwood.me)


## Building

Daily Earthquake Map is a static website, so only needs a web server to serve
its files. This repository has separated 'minifiable' files (HTML, CSS, JS,
JSON, etc.) from 'static' files (images, JavaScript libraries, etc.). To create
a single directory that can be served with a web server, either:

1. Copy the contents of [`src/`](src/) and [`static/`](static/) to a chosen
    output directory.
2. Use the provided Python [`build.py`](build.py) script. This has the added
    benefit of minifying source files.


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
browser &mdash; only fetching the tectonic plate boundaries fails.) For
deploying to Netlify, a file with HTTP headers is provided
([`static/_headers`](static/_headers)) that has some sensible defaults (such as
disabling embeds, not sending a referrer on external links, and disabling
Google Chrome's browsing history ad-tracking). A
[`robots.txt`](static/robots.txt) is also set up to disable a variety of bots
from scraping any text content.


## Acknowledgements

This software makes use of (and bundles) the following:

* [Feather](https://github.com/feathericons/feather) icons, licensed under the
    [MIT License](static/feather/LICENSE.txt);
* [Inter](https://rsms.me/inter/) font, licensed under the
    [SIL Open Font License, Version 1.1](static/inter/LICENSE.txt);
* [Leaflet](https://leafletjs.com/) mapping library, licensed under the
    [BSD 2-Clause License](static/leaflet/LICENSE.txt);
* [World tectonic plates and boundaries](https://github.com/fraxen/tectonicplates),
    licensed under the [ODC Attribution License](static/plates/LICENSE.txt).

The software also loads and displays (but does not bundle) an
[OpenStreetMap](https://www.openstreetmap.org/) basemap, Copyright ©
[OpenStreetMap](https://www.openstreetmap.org/copyright) and contributors.
The loaded
[earthquake data](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)
is courtesy of the [U.S. Geological Survey](https://usgs.gov).


## License

This software is available under the MIT license, copies of which are provided
in [`LICENSE.md`](LICENSE.md) and as follows:

Copyright © 2023 Samuel Wood

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the “Software”), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
