__author__ = 'marcus'

class Registers(object):

    def __init__(self):
        self.generalPurposes = [0] * 31
        self.PC = 0
        self.nPC = 0
        self.LO = 0
        self.HI = 0

    def getValueForRegister(self, num):
        return self.generalPurposes[num]

    def setValueForRegister(self, val, num):
        self.generalPurposes[num] = val

    def setInitialPC(self, val):
        self.PC = val

    def advancePC(self, val = 4):
        self.PC = self.nPC
        self.nPC += val

    def decreasePC(self, val = 4):
        self.PC = self.nPC
        self.nPC -= val

class Memory(object):

    reg = Registers()

    def __init__(self):
        self.mem = [0] * (2**20)

    def getValInAddress(self, address):
        return self.mem[address >> 2]

    def setValToAddress(self, val, address):
        self.mem[address >> 2] = val

    def getRegisters(self):
        return self.reg

    def getRegisterNum(self, reg):
        #print "Register Number! " + reg[1:len(reg)]
        return int(reg[1:len(reg)])

    def printMemory(self):
        for x in self.mem:
            if x is not 0: print x