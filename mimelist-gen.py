#!/usr/bin/env python

import argparse

from pathlib import Path

from xdg.DesktopEntry import DesktopEntry


def main():
    argp = argparse.ArgumentParser()
    argp.add_argument("desktop_file",
                      nargs="+",
                      type=Path,
                      help="Desktop files definining MIME associations")
    args = argp.parse_args()

    mime_types = {}

    for path in args.desktop_file:
        entry = DesktopEntry(path)
        for mime_type in entry.getMimeTypes():
            mime_types.setdefault(mime_type, []).append(path.name)

    print("[Default Applications]")
    for mime_type, applications in sorted(mime_types.items()):
        print(f"{mime_type}={';'.join(applications)};")


if __name__ == "__main__":
    main()
