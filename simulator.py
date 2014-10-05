#!/usr/bin/python
__author__ = 'marcus'

import sys
import string
from base import Memory

def usage():
    print "Welcome to Mips Simulator by Marcus Gabilheri"
    print "Usage: simulator [mode] [input]"
    print "Modes available: -d (debug), -n (normal)"

def main():
    inputFile = []

    if len(sys.argv) != 3:
        print usage()
    else:
        lines = [line.rstrip() for line in open(sys.argv[2])]
        for l in lines:
            line = l.split(" ")
            arr = []
            for i in line:
                if i != '':
                    arr.append(i)
            inputFile.append(arr)

    #for l in inputFile:
    #    print l
    process(inputFile)

def process(file):

    mem = Memory()
    print len(mem.mem)
    for line in file:
        addr = line[0].translate(None, "[]")
        iterLines = iter(line)
        next(iterLines)
        for s in iterLines:
            val = ""
            try:
                x = int(s, 16)
                val += s
            except ValueError:
                break

        print int(addr, 16) / 4
        mem.setValToAddress(val, int(addr, 16))

main()