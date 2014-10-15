__author__ = 'marcus'

from base import Memory

class FileProcess(object):

    IS_PC = 0
    IS_MEM = 1
    IS_REG = 2

    mem = Memory()

    def __init__(self, mem):
        self.mem = mem
        """ :type : Memory """

    def processLine(self, line):
        if line[0] is ('#'): # if starts with a pound symbol is a comment line and we ignore
            return "#"
        else:
            return line[0].translate(None, "[]") # get the memory address on the first value of the input file

    def getRealAddress(self, location):
        # print location
        try:
            return (int(location, 16), self.IS_MEM) # see if it's a hex address
        except:
            if location == "PC":
                return (0, self.IS_PC)
            else:
                return (self.mem.getRegisterNum(location), self.IS_REG)

    def process(self, file):
        # print len(mem.mem) # debug Only check the size of the array

        for line in file:
            location = self.processLine(line)
            if location is "#":
                continue
            addr = self.getRealAddress(location)
            iterLines = iter(line) # make a iterator over the array
            next(iterLines) # skip the first element
            for s in iterLines: # iterate over each string of the line
                try:
                    val = int(s, 16) # check if the value is a hex string
                    # print val
                    if addr[1] == self.IS_MEM:
                        self.mem.setValToAddress(val, addr[0])
                    elif addr[1] == self.IS_PC:
                        self.mem.getRegisters().setInitialPC(val)
                    elif addr[1] == self.IS_REG:
                        self.mem.getRegisters().setValueForRegister(val, addr[0])
                    else:
                        continue

                except ValueError:
                    break # break the loop if the value is no longer a hex string
