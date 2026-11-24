"""Write this entry's text to the make.fun output directory.

The sealed scorer reads /output/entry.txt, so all this program has to do
is copy the entry file next to it into $MAKEFUN_OUTPUT_DIR, byte for byte.
"""

import os
import shutil

ENTRY_NAME = "entry.txt"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, ENTRY_NAME)
    dst = os.path.join(out_dir, ENTRY_NAME)
    shutil.copyfile(src, dst)
    # The scorer compares characters exactly; prove the copy is faithful.
    with open(src, "rb") as f:
        original = f.read()
    with open(dst, "rb") as f:
        copied = f.read()
    assert copied == original, "copy diverged from entry.txt"


if __name__ == "__main__":
    main()
