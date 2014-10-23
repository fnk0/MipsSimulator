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
        self.regs.set_value_for_register(self.v0, int(x))

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


    def read_sring(self):
        sl = []
        s = ""
        r_str = raw_input("Sycall read String: ")
        arr = [ord(c) for c in r_str]
        for i  in range(0, len(arr), 1):
            s = hex(arr[i])[2:] + s
            if (i + 1) % 4 == 0 or i == len(arr) -1:
                sl.append("0x" + s)
                s = ""
        sl.append("0x00000000")
        arr_i = [int(x, 16) for x in sl]
        counter = 0
        for b in arr_i:
            self.mem.set_val_to_address(self.regs.get_value_for_register(self.a0) + counter, b)
            counter += 4

    def sys_exit(self):
        sys.exit(0)

    _syscall_funs = {
        1: print_integer,
        4: print_string,
        5: read_integer,
        8: read_sring,
        10: sys_exit
    }