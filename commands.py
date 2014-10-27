__author__ = 'marcus'

from base import Registers, Memory

class Command(object):

    def __init__(self, regs, mem, ins):
        self.regs = regs
        self.mem = mem
        self.ins = ins

    def execute_command(self, command, arg):
        self.commands[command](self, arg)

    def print_mem_address(self, address):
        print hex(self.mem.get_val_in_address(int(address, 16)))

    def print_reg(self, reg):
        print hex(self.regs.get_value_for_register(int(reg)))

    def print_instruction(self, address):
        print "Instruction %s" % str(self.ins.get_instruction(address))

    commands = {
        "print mem": print_mem_address,
        "print reg": print_reg,
        "print inst": print_instruction,
    }