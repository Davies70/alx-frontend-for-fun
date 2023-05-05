#!/usr/bin/python3
""" Python to Markdown """

import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    try:
        with open(sys.argv[1], "r") as f:
            contents = f.read()
            if contents == "":
                sys.exit(0)
    except FileNotFoundError:
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)
