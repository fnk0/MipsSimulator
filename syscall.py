__author__ = 'marcus'

import sys

class Syscall:

    a0 = 4
    v0 = 2
    gp = 28

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
        sys.stdout.write(str(int(self.regs.get_value_for_register(self.a0))))

    def read_integer(self):
        x = raw_input("")
        self.regs.set_value_for_register(self.v0, int(x))

    def print_string(self):
        addr = self.regs.get_value_for_register(self.a0)
        val = self.mem.get_val_in_address(addr)

        counter = 0
        out = ""

        mod = addr % 4
        nullchar = chr(0)
        while True:
            if mod <= 0:
                c = self.get_ch1(val)
                if c == nullchar: break
                sys.stdout.write(str(c))

            if mod <= 1:
                c = self.get_ch2(val)
                if c == nullchar: break
                sys.stdout.write(str(c))

            if mod <= 2:
                c = self.get_ch3(val)
                if c == nullchar: break
                sys.stdout.write(str(c))

            c = self.get_ch4(val)
            if c == nullchar: break
            sys.stdout.write(str(c))

            mod = 0
            counter += 4
            val = self.mem.get_val_in_address(addr + counter)

    def read_string(self):
        sl = []
        s = ""
        r_str = raw_input("")
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

    # Allocates bytes based on $a0=$4, returns address in $v0=$2
    # Makes a stack based allocator but do not deallocate
    # data_segment = GP
    # sets the value of the $v0 to be the GP
    # sets GP = GP + a0
    # returns v0
    def allocate_memory(self):
        self.regs.set_value_for_register(self.v0, self.regs.get_value_for_register(self.gp))
        self.regs.set_value_for_register(self.gp, self.regs.get_value_for_register(self.gp) + self.regs.get_value_for_register(self.a0))
        return self.regs.get_value_for_register(self.v0)

    def sys_exit(self):
        sys.exit(0)

    _syscall_funs = {
        1: print_integer,
        4: print_string,
        5: read_integer,
        8: read_string,
        9: allocate_memory,
        10: sys_exit,
    }