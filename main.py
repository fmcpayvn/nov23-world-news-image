#!/usr/bin/env python3
"""Copy the pre-built front page to the grader's output directory.

Standard library only: the grader runs this with no network on a
read-only copy of the repository, so nothing is installed and nothing
is written back into the repo. The image is already rendered
(entry.png, 1024x1024); this just places it at $MAKEFUN_OUTPUT_DIR/entry.png.
Deterministic: both graded runs write the same bytes.
"""
import os
import shutil

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out, exist_ok=True)
    shutil.copyfile(
        os.path.join(here, "entry.png"),
        os.path.join(out, "entry.png"),
    )
