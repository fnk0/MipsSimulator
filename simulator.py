#!/usr/bin/python
__author__ = 'marcus'

import sys, re
import string
from base import Memory
from process import FileProcess
from instructions import Instruction
from syscall import Syscall
from commands import Command

def usage():
    print "Usage: simulator [mode] [input file]"
    print "Modes available: -d (debug), -n (normal)"
    sys.exit(0)

def debug():
    print "Debug mode is ON!"
    print ""

if __name__ == "__main__":
    print "Welcome to Mips Simulator by Marcus Gabilheri"
    inputFile = []
    mem = Memory()
    fProcess = FileProcess(mem)

    if len(sys.argv) != 3: usage()
    if sys.argv[1] == "-d":
        debug = True
    elif sys.argv[1] == "-n":
        debug = False
    else:
        usage()

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
    com = Command(mem.get_registers(), mem, ins)
    #debug = False
    while True:
        if debug:
            command = raw_input("")
            print "PC: " + hex(mem.get_registers().PC)
            print "Instruction Word: " + hex(mem.get_val_in_address(mem.get_registers().PC))
            line = command.split(" ")
            if len(line) > 2:
                if line[1] == "mem":
                    com.execute_command(line[0] + " " + line[1], line[2])
                elif line[1] == 'reg':
                    com.execute_command(line[0] + " " + line[1], line[2])
                elif line[1] == 'inst':
                    com.execute_command(line[0] + " " + line[1], mem.get_val_in_address(mem.get_registers().PC))

                continue
            else:
                pass

        ins.evaluate(mem.get_val_in_address(mem.get_registers().PC))