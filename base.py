__author__ = 'marcus'

class Registers(object):

    def __init__(self):
        self.generalPurposes = [0] * 32
        self.PC = 0
        self.nPC = self.PC + 4
        self.LO = 0
        self.HI = 0

    def get_value_for_register(self, num):
        return self.generalPurposes[num]

    def set_value_for_register(self, num, val):
        self.generalPurposes[num] = val

    def set_initial_pc(self, val):
        self.PC = val
        self.nPC = val + 4

    def advance_pc(self, val = 4):
        self.PC = self.nPC
        self.nPC += val

    def decrease_pc(self, val = 4):
        self.PC = self.nPC
        self.nPC -= val

class Memory(object):

    reg = Registers()

    def __init__(self):
        self.mem = [0] * (2**20)

    def get_val_in_address(self, address):
        return self.mem[address >> 2]

    def set_val_to_address(self, val, address):
        self.mem[address >> 2] = val

    def get_registers(self):
        return self.reg

    def get_register_num(self, reg):
        #print "Register Number! " + reg[1:len(reg)]
        return int(reg[1:len(reg)])

    def print_memory(self):
        for x in self.mem:
            if x is not 0: print x