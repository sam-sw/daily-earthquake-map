from pathlib import Path
from shutil import copytree
from sys import argv

from minify_html import minify as _minify


def minify(src: Path, dst: Path):
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


def build(src: Path, dst: Path, static: list[Path]):
    try:
        assert isinstance(src, Path)
        assert isinstance(static, list) or isinstance(static, tuple)
        assert all([isinstance(s, Path) for s in static])
        assert isinstance(dst, Path)
    except:
        raise TypeError(
            'Source, list/tuple of static, and destination paths must all be'
            'pathlib.Path objects.'
        )

    if not (src.is_dir() and all([s.is_dir() for s in static]) and dst.is_dir()):
        raise NotADirectoryError(
            'Source, static, and destination paths must point to directories.'
        )

    if any(['..' in str(s) for s in static]) or '..' in str(dst):
        raise ValueError('Static and destination paths must not contain \'..\'.')

    src_paths = [p for p in src.glob('**/*')]
    dst_paths = [dst / p.relative_to(src) for p in src_paths]

    _ = [d.mkdir(parents=True, exist_ok=True) for d in dst_paths if d.is_dir()]
    _ = [minify(s, d) for s, d in zip(src_paths, dst_paths)]

    dst_static_paths = [dst / p.name for p in static]
    _ = [copytree(s, d, dirs_exist_ok=False) for s, d in zip(static, dst_static_paths)]


if __name__ == '__main__':
    if len(argv) < 3:
        raise ValueError(
            'Require at least two arguments: source and destination directories.'
        )

    try:
        src = Path(argv[1])
        dst = Path(argv[2])
        if len(argv) > 3:
            static = [Path(a) for a in argv[3:]]
        else:
            static = []
    except:
        raise TypeError('Could not parse arguments.')

    build(src, dst, static)
