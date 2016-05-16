#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, subprocess, operator
import argparse
from sys import argv

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import delims

gramN = [2, 3, 4, 5]
neighborFilter = 0

def countNGram(n, word):
    ret = {}
    size = len(word)
    for i in range(0, size - n):
        cur = word[i:i+n]
        if cur in ret:
            ret[cur] += 1
        else:
            ret.update({cur: 1})
    return ret

def nGram(inputFileName, outputFileName):
    bigTable = [{} for n in gramN]

    catResult = subprocess.Popen(["cat", inputFileName], \
            stdout=subprocess.PIPE).communicate()[0]
    wcResult = subprocess.Popen(["wc", "-l"], \
            stdin=subprocess.PIPE,\
            stdout=subprocess.PIPE).communicate(catResult)[0]
    totalLine = int(wcResult.strip())
    curLine = 0
    print "TotalLine: " + str(totalLine)
    sys.stdout.flush()

    inputFile = open(inputFileName, "r")
    lastPercent = 0.0
    sentences = []
    for _inputLine in inputFile:
        curLine += 1
        curPercent = float(curLine) / float(totalLine)
        if curPercent - lastPercent >= 0.0001:
            print " %.2lf%%\r" % (curPercent * 100),
            lastPercent = curPercent
            sys.stdout.flush()
        inputLine = _inputLine.strip().decode('utf-8')
        rawDict = {}
        curWord = ""
        L = len(inputLine)
        for char in inputLine:
            if char in delims.delims:
                if curWord in rawDict:
                    rawDict[curWord] += 1
                else:
                    rawDict.update({curWord: 1})
                curWord = ""
            else:
                curWord += char

        if curWord != '':
            if curWord in rawDict:
                rawDict[curWord] += 1
            else:
                rawDict.update({curWord: 1})

        for n in gramN:
            for word, freq in rawDict.items():
                sentences.append(word)
                for k, v in countNGram(n, word.decode('utf-8')).items():
                    if k in bigTable[n-gramN[0]]:
                        bigTable[n-gramN[0]][k] += freq * v
                    else:
                        bigTable[n-gramN[0]].update({k: v})
    inputFile.close()

    if neighborFilter:
        for sentence in sentences:
            for n in gramN:
                for i in range(0, len(sentence)-n-1):
                    word1 = sentence[i:i+n]
                    word2 = sentence[i+1:i+n+1]
                    if word1 in bigTable[n-gramN[0]] and word2 in bigTable[n-gramN[0]]:
                        freq1 = bigTable[n-gramN[0]][word1]
                        freq2 = bigTable[n-gramN[0]][word2]
                        if freq1 < 1.2 * freq2 and freq2 < 1.2 * freq1:
                            bigTable[n-gramN[0]].update({word1: 0})
                            bigTable[n-gramN[0]].update({word2: 0})
                        elif freq1 < 0.1 * freq2:
                            bigTable[n-gramN[0]].update({word1: 0})
                        elif freq2 < 0.1 * freq1:
                            bigTable[n-gramN[0]].update({word2: 0})

    outputFile = open(outputFileName, "w")
    for n in gramN:
        curList = sorted(bigTable[n-gramN[0]].items(),\
                cmp=lambda x,y: y[1] - x[1])
        for k, v in curList:
            if v > 1:
                outputFile.write(k + "|" + str(v) + "\n")
    outputFile.close()

    return bigTable

def main():
    L = len(argv)
    if L < 4 or L > 5:
        print "nGram.py: count nGram words in Chinese Texts"
        print "Usage:\n\t ./nGram.py inputFileName nMin nMax [outputFileName]"
        print "Explanation:\n\t inputFileName -- Name of the input data text"
        print "\t nMin, nMax -- the range of N for n-gram"
        print "\t outputFileName -- (optional) Name of the output nGram text"
        print "\t                  If it is omitted, than store result to 'results.txt'"
        print "\t                  and do the neighbor-word-filtering."
        print "Example:\n\t ./nGram.py data.txt 2 5"
        return
    if os.path.isfile(argv[1]) == False:
        print "Cannot find input file named '" + argv[1] + "'"
    else:
        filename = argv[1]
    if L == 5:
        outputFileName = argv[4]
    else:
        global neighborFilter
        neighborFilter = 1
        outputFileName = "result.txt"
    try:
        nMin = int(argv[2])
        nMax = int(argv[3])
        if nMin <= 0 or nMax <= 0 or nMin > nMax:
            raise ValueError
    except ValueError:
        print "Value illegal or out of range: nMin=" + argv[2] + " nMax=" + arv[3]
        return
    global gramN
    gramN = range(nMin, nMax+1)
    nGram(filename, outputFileName)

if __name__ == "__main__":
    main()
