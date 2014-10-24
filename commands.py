__author__ = 'marcus'

from base import Registers, Memory

class Command(object):

    def __init__(self, regs, mem):
        self.regs = regs
        self.mem = mem

    def execute_command(self, command, arg):
        self.commands[command](self, arg)

    def print_mem_address(self, address):
        print hex(self.mem.get_val_in_address(int(address)))

    def print_reg(self, reg):
        print hex(self.regs.get_value_for_register(int(reg)))

    commands = {
        "print mem": print_mem_address,
        "print reg": print_reg

    }