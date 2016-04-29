#!/usr/bin/python

import os
import delims

gramN = [2, 3, 4, 5]

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

    inputFile = open(inputFileName, "r")
    for inputLine in inputFile:
        rawDict = {}
        curWord = ""
        for char in inputLine:
            if char in delims:
                if curWord in rawDict:
                    rawDict[curWord] += 1
                else
                    rawDict.update({curWord: 1})
                curWord = ""
            else:
                curWord += char

        for n in gramN:
            for word, freq in curWord.items():
                for k, v in countNGram(n, word).items():
                    if k in bigTable[n]:
                        bigTable[n][k] += freq * v
                    else:
                        bigTable[n].update({k: v})
    inputFile.close()

    outputFile = open(outputFileName, "w")
    for n in gramN:
        for k, v in bigTable[n].iteritems():
            outputFile.write(k + "|" + v)
    outputFile.close()

def main():
    nGram("data/2006_all", "data/2006_nGram")

if __name__ == "__main__":
    main()
