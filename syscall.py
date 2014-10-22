__author__ = 'marcus'

import sys

class Syscall:

    a0 = 4
    v0 = 2

    def __init__(self, regs, mem):
        self.regs = regs
        self.mem = mem

    def get_ch4(self, num):
        return chr((num >> 24) & 0xFF)

    def get_ch3(self, num):
        return chr((num >> 16) & 0xFF)

    def get_ch2(self, num):
        return chr((num >> 8) & 0xFF)

    def get_ch1(self, num):
        return chr(num & 0xFF)

    def print_integer(self):
        print str(self.regs.get_value_for_register(self.a0))

    def read_integer(self):
        x = raw_input("Syscall Read Integer: ")
        self.regs.set_value_for_register(self.v0, x)

    def print_string(self):
        addr = self.regs.get_value_for_register(self.a0)

        val = self.mem.get_val_in_address(addr)
        counter = 0
        out = ""

        while(val != 0):
            out += self.get_ch1(val)
            out += self.get_ch2(val)
            out += self.get_ch3(val)
            out += self.get_ch4(val)
            counter += 4
            val = self.mem.get_val_in_address(addr + counter)

        print out

    def sys_exit(self):
        sys.exit(0)