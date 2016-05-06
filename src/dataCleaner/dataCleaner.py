#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

yearMonth = [
    (2006, 1),
    (2006, 2),
    (2006, 3),
    (2006, 4)
]

def isChinese(uchar):
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    return False

def walk(rootDir, outputFile):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for f in files:
            print "processing text for", os.path.join(f.split('.')[0]), "... ",
            sys.stdout.flush()
            fi = open(os.path.join(root, f), "r")
            content = fi.read()
            fi.close()
            soup = BeautifulSoup(content, 'lxml' )
            paras = soup.findAll(text=True)
            for para in paras:
                hasChinese = 0
                for ch in para:
                    if isChinese(ch):
                        hasChinese = 1
                        break
                if hasChinese:
                    outputFile.write(re.sub('<[^>]*>', '', str(para)) + "\n")
            print "\r                                                     \r",
            sys.stdout.flush()

def main():
    os.system('mkdir textdata')
    outputFile = open("./textdata/data.txt", "w")
    for (year, month) in yearMonth:
        walk("./data/" + str(year) + str(month).zfill(2), outputFile)
    outputFile.close()

if __name__ == "__main__":
    main()
