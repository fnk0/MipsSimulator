#!/usr/bin/python
__author__ = 'marcus'

import sys
import string
from base import Memory

def usage():
    print "Welcome to Mips Simulator by Marcus Gabilheri"
    print "Usage: simulator [mode] [input]"
    print "Modes available: -d (debug), -n (normal)"


def process(file):
    mem = Memory()
    # print len(mem.mem) # debug Only check the size of the array

    for line in file:
        addr = line[0].translate(None, "[]") # get the memory address on the first value of the input file
        iterLines = iter(line) # make a iterator over the array
        next(iterLines) # skip the first element
        val = "" # set the initial value to nothing
        for s in iterLines: # iterate over each string of the line
            try:
                x = int(s, 16) # check if the value is a hex string
                val = x
            except ValueError:
                break # break the loop if the value is no longer a hex string

        print int(addr, 16) / 4 # debugging. Prints the address
        mem.setValToAddress(val, int(addr, 16)) # sets the value to the specific address

if __name__ == "__main__":
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

    for l in inputFile:
        print l
    #process(inputFile)