#!/usr/bin/python3
""" Python to Markdown converter """

import sys
import hashlib

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    try:
        with open(sys.argv[1], "r") as f:
            content = f.read()
            lines = content.splitlines()
            for j in range(len(lines)):
                asterisk_count = lines[j].count("**")
                dash_count = lines[j].count("__")
                if asterisk_count >= 2:
                    asterisk_counter = 1
                    while asterisk_counter <= asterisk_count:
                        if asterisk_counter % 2 == 1:
                            lines[j] = lines[j].replace("**", "<b>", 1)
                        else:
                            lines[j] = lines[j].replace("**", "</b>", 1)
                        asterisk_counter += 1
                if dash_count >= 2:
                    dash_counter = 1
                    while dash_counter <= dash_count:
                        if dash_counter % 2 == 1:
                            lines[j] = lines[j].replace("__", "<em>", 1)
                        else:
                            lines[j] = lines[j].replace("__", "</em>", 1)
                        dash_counter += 1
                if "(" in lines[j]:
                    start = lines[j].find('((')
                    end = lines[j].find('))')
                    substring = lines[j][start + 2 : end]
                    lines[j] = lines[j].replace("((", "")
                    lines[j] = lines[j].replace("))", "")
                    new_substring = substring.replace("c", "")
                    new_substring = new_substring.replace("C", "")
                    lines[j] = lines[j].replace(substring, new_substring)
                if "[" in lines[j]:
                    start = lines[j].find("[[")
                    end = lines[j].find("]]")
                    substring = lines[j][start + 2 : end ]
                    lines[j] = lines[j].replace("[[", "")
                    lines[j] = lines[j].replace("]]", "")
                    hash = hashlib.md5(substring.encode()).hexdigest()
                    lines[j] = lines[j].replace(substring, hash)

        with open(sys.argv[2], "w+") as f:
            for i in range(len(lines)):
                if lines[i].startswith("# "):
                    f.write("<h1>" + lines[i][2:] + "</h1>\n")
                elif lines[i].startswith("## "):
                    f.write("<h2>" + lines[i][3:] + "</h2>\n")
                elif lines[i].startswith("### "):
                    f.write("<h3>" + lines[i][4:] + "</h3>\n")
                elif lines[i].startswith("#### "):
                    f.write("<h4>" + lines[i][5:] + "</h4>\n")
                elif lines[i].startswith("##### "):
                    f.write("<h5>" + lines[i][6:] + "</h5>\n")
                elif lines[i].startswith("###### "):
                    f.write("<h6>" + lines[i][7:] + "</h6>\n")
                elif lines[i].startswith("- "):
                    if i == 0:
                        f.write("<ul>\n")
                    elif not lines[i - 1].startswith("- "):
                        f.write("<ul>\n")
                    if i == len(lines) - 1:
                        f.write("<li>" + lines[i][2:] + "</li>\n")
                        f.write("</ul>\n")
                    elif not lines[i + 1].startswith("- "):
                        f.write("<li>" + lines[i][2:] + "</li>\n")
                        f.write("</ul>\n")
                    else:
                        f.write("<li>" + lines[i][2:] + "</li>\n")
                elif lines[i].startswith("* "):
                    if i == 0:
                        f.write("<ol>\n")
                    elif not lines[i - 1].startswith("* "):
                        f.write("<ol>\n")
                    if i == len(lines) - 1:
                        f.write("<li>" + lines[i][2:] + "</li>\n")
                        f.write("</ol>\n")
                    elif not lines[i + 1].startswith("* "):
                        f.write("<li>" + lines[i][2:] + "</li>\n")
                        f.write("</ol>\n")
                    else:
                        f.write("<li>" + lines[i][2:] + "</li>\n")
                elif not lines[i] == "":
                    if i == 0:
                        if len(lines) == 1:
                            f.write("<p>\n" + lines[i] + "\n" + "</p>\n")
                        elif lines[i + 1] == "":
                            f.write("<p>\n" + lines[i] + "\n" + "</p>\n")
                        else:
                            f.write("<p>\n" + lines[i] + "\n" + "<br />\n")
                    elif i == len(lines) - 1:
                        if lines[i - 1] == "":
                            f.write("<p>\n" + lines[i] + "\n" + "</p>\n")
                        else:
                            f.write(lines[i] + "\n" + "</p>\n")
                    elif lines[i - 1] == "":
                        f.write("<p>\n" + lines[i] + "\n")
                        if lines[i + 1] == "":
                            f.write("</p>\n")
                        else:
                            f.write("<br />\n")
                    elif not lines[i - 1] == "":
                        if lines[i + 1] == "":
                            f.write(lines[i] + "\n" + "</p>\n")
                        else:
                            f.write(lines[i] + "\n" + "<br />\n")

        sys.exit(0)
    except FileNotFoundError:
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)
