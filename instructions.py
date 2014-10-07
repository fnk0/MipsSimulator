__author__ = 'marcus'

from base import Instruction, Memory

class Add(Instruction):

    def evaluate(self):
        self.saveReg = self.val1 + self.val2
        self.getMemory().getRegisters().advancePC()
        return self.saveReg

class Addi(Add):
    pass

class Addiu(Addi):
    pass

class Addu(Add):
    pass

class Sub(Instruction):

    def evaluate(self):
        self.saveReg = self.val1 - self.val2
        self.getMemory().getRegisters().advancePC()
        return self.saveReg