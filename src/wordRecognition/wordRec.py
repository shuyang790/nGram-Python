#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, subprocess
from sys import argv

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

nGramFileName = "/Users/Ivan/nGram_1-5_ge2times.txt"

class Recognizer():

    def __init__(self):
        self.nGrams = {}
        self.iterNum = 3
        self.freqLowerBound = 10
        self.prLowerBound = 10

    def init(self, filename):
        print ("nGram file '" + filename + "' loading ...")
        sys.stdout.flush()
        lineNum = 0
        for line in open(filename, "r"):
            lineNum += 1
            if lineNum % 50000 == 0:
                print "Current Line: " + str(lineNum) + "\r",
                sys.stdout.flush()
            element = line.split('|')
            word = element[0]
            cnt = int(element[1])
            if cnt > self.freqLowerBound:
                self.nGrams.update({element[0]: int(element[1])})
        print ("nGram file '" + filename + "' loaded! (" + \
                str(len(self.nGrams)) + " words totally)")
        sys.stdout.flush()

    def run(self):

        # frquency bound;
        self.pr = {}
        maxfreq = 0
        for word, freq in self.nGrams.iteritems():
            if freq > maxfreq:
                maxfreq = freq
            self.pr[word] = float(freq)
        for word in self.pr:
            self.pr[word] /= float(maxfreq)

        print "probability initialized"
        sys.stdout.flush()

        for curIter in range(self.iterNum):
            newPr = dict.copy(self.pr)
            for word in self.pr:
                length = len(word)
                for i in range(1, length):
                    if word[i:] in self.pr and self.pr[word] > 0:
                        if self.pr[word[i:]] / self.pr[word] < 1.0:
                            newPr[word[i:]] *= 0.1
                            newPr[word] *= 10
                        elif self.pr[word[i:]] > 10 * self.pr[word]:
                            newPr[word[i:]] *= 10000
                            newPr[word] = 0
                    if word[:i] in self.pr and self.pr[word] > 0:
                        if self.pr[word[:i]] / self.pr[word] < 1.0:
                            newPr[word[:i]] *= 0
                            newPr[word] *= 10
                        elif self.pr[word[:i]] > 10 * self.pr[word]:
                            newPr[word[:i]] *= 1000
                            newPr[word] *= 0
                    # for anotherWord in self.pr:
                    #     if anotherWord.startswith(word[i:]) and \
                    #         self.pr[word] < 1.1 * self.pr[anotherWord] and \
                    #         self.pr[word] * 1.1 > self.pr[anotherWord]:
                    #         newPr[word] = 0
                    #         newPr[anotherWord] = 0
            self.pr = newPr
        print "sub-word filtered"
        sys.stdout.flush()

    def report(self):
        f = open("./result.log", "w")
        items = sorted(self.pr.items(), cmp=lambda x,y:-1 if y[1]<x[1] else 1)
        for word, pr in items:
            if pr > self.prLowerBound and len(word.decode('utf-8')) > 1:
                f.write("%s|%.2lf\n" % (word, pr))

def main():
    r = Recognizer()
    r.init(nGramFileName)
    r.run()
    r.report()

if __name__ == "__main__":
    main()
