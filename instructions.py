__author__ = 'marcus'

from base import Memory, Registers

class Instruction(object):

    mem = Memory()
    regs = Registers()

    def __init__(self, regs, mem):
        self.regs = regs
        self.mem = mem

    def evaluate(self, fun, *args):
        """
        The evaluate method will evaluate the instruction and save it
        to the specified saveReg
        args[0] = Register to be saved
        args[1] = word 1
        args[2] = word 3
        ... etc..
        :return:
        """
        return fun(args)

    def getMemory(self):
        return self.mem

    def applyMaskRegister(self, num):
        mask = num & 0b11111100000000000000011111111111
        d_word = (num >> 11) & 0x3F
        print d_word
        return mask

    def applyMaskImmediate(self, num):
        mask = num & 0b11111100000000000000000000000000
        return mask

    def applyMaskJump(self, num):
        mask = num & 0b1111110000011111000000000000
        return mask

    def add(self, *args):
        self.regs.generalPurposes[args[0]] = args[1] + args[2]
        self.getMemory().getRegisters().advancePC()
        return

    def addi(self, *args):
        self.add(args)
        return

    def addu(self, *args):
        self.add(args)
        return

    def addiu(self, *args):
        self.add(args)
        return


    def sub(self, *args):
        self.regs.generalPurposes[args[0]] = args[1] + args[2]
        self.getMemory().getRegisters().advancePC()
        return


    instructions = {
        0b00000000000000000000000000100000: add,
    }

