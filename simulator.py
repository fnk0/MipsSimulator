#!/usr/bin/python
__author__ = 'marcus'

import sys, re
import string
from base import Memory
from process import FileProcess
from instructions import Instruction
from syscall import Syscall


def usage():
    print "Welcome to Mips Simulator by Marcus Gabilheri"
    print "Usage: simulator [mode] [input]"
    print "Modes available: -d (debug), -n (normal)"

if __name__ == "__main__":
    print "Mips Simulator writen by Marcus Gabilheri"
    inputFile = []
    mem = Memory()
    debug = True if sys.argv[1] == "-d" else False
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

    fProcess.process(inputFile)
    s_call = Syscall(mem.get_registers(), mem)
    ins = Instruction(mem.get_registers(), mem, s_call)
    debug = False
    while True:
        if debug:
            command = raw_input("")

            if command == "":
                continue

        ins.evaluate(mem.get_val_in_address(mem.get_registers().PC))