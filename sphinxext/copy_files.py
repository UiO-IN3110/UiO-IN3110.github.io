"""
Copy files from source directory to destination

Based on https://github.com/sphinx-contrib/rawfiles,
but accepts glob patterns

Relative path within source directory is preserved,
unlike sphinx builtin html_extra_path.
"""

import shutil
from pathlib import Path

from sphinx.util import logging

logger = logging.getLogger(__name__)


def copy_source_files(app):
    src_dir = Path(app.srcdir)
    out_dir = Path(app.builder.outdir)

    for pattern in app.builder.config.copy_files:
        # cleanup
        for dst in out_dir.rglob(pattern):
            if dst.exists():
                if dst.is_dir():
                    shutil.rmtree(dst)
                else:
                    dst.unlink()

        src_list = list(src_dir.rglob(pattern))
        if not src_list:
            logger.warning(f"No files found for copy_files pattern {pattern:r}")

        for src in src_list:
            relpath = src.relative_to(src_dir)
            dst = out_dir / relpath
            logger.info(f"Copy {src} -> {dst}")

            # copy file
            if src.is_dir():
                shutil.copytree(src, dst)
            else:
                shutil.copy(src, dst)

    # must return empty iterable
    return ()


def setup(app):
    app.add_config_value("copy_files", [], "html")
    app.connect("html-collect-pages", copy_source_files)
