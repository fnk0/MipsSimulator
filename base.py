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

    def advancePC(self):
        self.PC += 4
        print str(self.PC)

    def decreasePC(self):
        self.PC -= 4

class Memory(object):

    reg = Registers()

    def __init__(self):
        self.mem = [0] * (2**20)

    def getValInAddress(self, address):
        return self.mem[address / 4]

    def setValToAddress(self, val, address):
        self.mem[address / 4] = val

    def getRegisters(self):
        return self.reg


class Instruction(object):

    mem = Memory()

    def __init__(self, saveReg, val1, val2, mem):
        self.saveReg = saveReg
        self.val1 = val1
        self.val2 = val2
        self.mem = mem

    def evaluate(self):
        """
        The evaluate method will evaluate the instruction and save it
        to the specified saveReg
        :return:
        """
        pass

    def getMemory(self):
        return self.mem
