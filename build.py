"""Simple module to minify and copy source and static website files to an output."""

from pathlib import Path
from shutil import copytree
from sys import argv
from typing import Optional

from minify_html import minify as _minify


def minify(src: Path, dst: Path):
    """Minify the contents of a given file and write it to a destination path.

    Parameters
    ----------
    src : pathlib.Path
        Path to the source file.
    dst : pathlib.Path
        Path to the destination.
    """
    with src.open('r') as fsrc:
        with dst.open('w') as fdst:
            fdst.write(
                _minify(
                    fsrc.read(),
                    minify_css=True,
                    minify_js=True,
                    do_not_minify_doctype=True,
                    ensure_spec_compliant_unquoted_attribute_values=True,
                    keep_spaces_between_attributes=True,
                )
            )


def build(src: Path, dst: Path, static: Optional[Path] = None):
    """Build a site by minifying or copying files to a build directory.

    Takes all files within the ``src`` directory, minifies them, and copies the
    results to the same location within the ``dst`` directory. Copies the
    contents of an optionally-supplied ``static`` directory inside the
    top-level of the ``dst`` directory.

    Parameters
    ----------
    src : pathlib.Path
        Path to the source directory.
    dst : pathlib.Path
        Path to the destination (build) directory.
    static : pathlib.Path, optional
        Path to static directory. Defaults to None.

    Raises
    ------
    TypeError
        If the source, destination, or static paths are not pathlib.Path
        objects.
    NotADirectoryError
        If the source, destination, or static paths are not directories.
    ValueError
        If any paths contain '..'.
    """
    try:
        # Check parameters have correct types (pathlib.Path)
        assert isinstance(src, Path)
        assert isinstance(dst, Path)
        assert isinstance(static, Path) or static is None
    except:
        raise TypeError(
            'Source, destination, and static paths must all be pathlib.Path objects.'
        )

    # Check paths are all directories
    if not (src.is_dir() and dst.is_dir()):
        if static:
            if not static.is_dir():
                raise NotADirectoryError(
                    'Source, destination, and static paths must point to directories.'
                )
        else:
                raise NotADirectoryError(
                    'Source, destination, and static paths must point to directories.'
                )

    if '..' in str(static) or '..' in str(dst):
        # Check paths don't contain any dodgy .. patterns
        raise ValueError('Static and destination paths must not contain \'..\'.')

    # Generate a list of source paths, and their applicable destinations
    src_paths = [p for p in src.glob('**/*')]
    dst_paths = [dst / p.relative_to(src) for p in src_paths]

    # Make all output directories, and minify and copy source files
    _ = [d.mkdir(parents=True, exist_ok=True) for d in dst_paths if d.is_dir()]
    _ = [minify(s, d) for s, d in zip(src_paths, dst_paths)]

    # Copy all static directories
    if static:
        copytree(static, dst, dirs_exist_ok=True)


if __name__ == '__main__':
    # Check we have at least source and destination paths
    if len(argv) < 3:
        raise ValueError(
            'Require at least two arguments: source and destination directories.'
        )
    if len(argv) > 4:
        raise ValueError(
            'Require at most three arguments: source, destination, and static directories.'
        )

    # Make sure we have pathlib.Path objects
    try:
        src = Path(argv[1])
        dst = Path(argv[2])
        if len(argv) == 4:
            static = Path(argv[3])
        else:
            static = None
    except:
        raise TypeError('Could not parse arguments.')

    # Build the directory
    build(src, dst, static=static)
