__author__ = 'marcus'

from base import Instruction

class Add(Instruction):

    def evaluate(self):
        self.saveReg = self.val1 + self.val2
