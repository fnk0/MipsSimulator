#!/usr/bin/python
__author__ = 'marcus'

import sys, re
import string
from base import Memory
from instructions import Sub
from process import FileProcess


def usage():
    print "Welcome to Mips Simulator by Marcus Gabilheri"
    print "Usage: simulator [mode] [input]"
    print "Modes available: -d (debug), -n (normal)"

if __name__ == "__main__":
    inputFile = []

    mem = Memory()

    fProcess = FileProcess(mem)

    if len(sys.argv) != 3:
        print usage()
    else:
        lines = [line.rstrip() for line in open(sys.argv[2])]
        for l in lines:
            if not l:
                continue
            l = re.sub(' +', ',', l)
            l = re.sub('\t+', ',', l)
            line = l.split(",")

            arr = []
            for i in line:
                if i != '':
                    arr.append(i)
            inputFile.append(arr)

    #for l in inputFile:
    #    print l
    fProcess.process(inputFile)
    mem.printMemory()
    print mem.getValInAddress(0x00007000)

