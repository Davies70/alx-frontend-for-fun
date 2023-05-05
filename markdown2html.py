#!/usr/bin/python3
""" Python to Markdown converter """

import sys

if __name__ == "__main__":
    n = 0
    line = ""
    start = 0
    count = 0
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    try:
        with open(sys.argv[1], "r") as f:
            contents = f.read()
        with open(sys.argv[2], "w") as f:
            for i in range(len(contents)):
                if contents[i] == "#":
                    n += 1
                if contents[i] == "\n" and contents[i + 1] != "":
                    start = n + count
                    f.write(f"<h{n}>{contents[start + 1 : i]}</h{n}>\n")
                    count = i
                    n = 0
        sys.exit(0)
    except FileNotFoundError:
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)
