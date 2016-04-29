#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

year = 2006

def walk(rootDir, outputFile):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for f in files:
            print os.path.join(root, f)
            with open(os.path.join(root, f)) as fi:
                content = fi.read()
            outputFile.write(content)

def main():
    outputFile = open("./data/" + str(year) + "_all", "w")
    walk("./data/" + str(year), outputFile)
    outputFile.close()

if __name__ == "__main__":
    main()
