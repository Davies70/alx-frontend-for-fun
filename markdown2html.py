#!/usr/bin/python3
""" Python to Markdown converter """

import sys

if __name__ == "__main__":
    unordered_list = []
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    try:
        with open(sys.argv[1], "r") as f:
            contents = f.read()
            lines = contents.splitlines()
        with open(sys.argv[2], "r+") as f:
            for line in lines:
                if line.startswith("# "):
                    f.write("<h1>" + line[2:] + "</h1>\n")
                elif line.startswith("## "):
                    f.write("<h2>" + line[3:] + "</h2>\n")
                elif line.startswith("### "):
                    f.write("<h3>" + line[4:] + "</h3>\n")
                elif line.startswith("#### "):
                    f.write("<h4>" + line[5:] + "</h4>\n")
                elif line.startswith("##### "):
                    f.write("<h5>" + line[6:] + "</h5>\n")
                elif line.startswith("###### "):
                    f.write("<h6>" + line[7:] + "</h6>\n")
                elif line.startswith("- "):
                    unordered_list.append(line[2:])
            for i in range(len(unordered_list)):
                if i == 0:
                    f.write("<ul>\n")
                f.write('<li>' + unordered_list[i] + '</li>\n')
                if i is len(unordered_list) - 1:
                    f.write("</ul>\n")
            unordered_list = []
        sys.exit(0)
    except FileNotFoundError:
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)
