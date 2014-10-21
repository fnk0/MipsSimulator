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

    def _add(self, args = []):
        self.regs.generalPurposes[args[0]] = args[1] + args[2]
        self.getMemory().getRegisters().advancePC()
        return

    def _addi(self, args = []):
        self._add(args)
        return

    def _addu(self, args = []):
        self._add(args)
        return

    def _addiu(self, args = []):
        self._add(args)
        return

    def _and(self, args = []):
        pass

    def _andi(self, args = []):
        self._andi(args)

    def _beq(self, args = []):
        pass

    def _bgez(self, args = []):
        pass

    def _bgezal(self, args = []):
        pass

    def _bgtz(self, args = []):
        pass

    def _blez(self, args = []):
        pass

    def _bltz(self, args = []):
        pass

    def _bltzal(self, args = []):
        pass

    def _bne(self, args = []):
        pass

    def _div(self, args = []):
        pass

    def _divu(self, args = []):
        pass

    def _jump(self, args = []):
        pass

    def _jal(self, args = []):
        pass

    def _jr(self, args = []):
        pass

    def _lb(self, args = []):
        pass

    def _lui(self, args = []):
        pass

    def _lw(self, args = []):
        pass

    def _mfhi(self, args = []):
        pass

    def _mflo(self, args = []):
        pass

    def _mult(self, args = []):
        pass

    def _multu(self, args = []):
        pass

    def _noop(self, args = []):
        pass

    def _or(self, args = []):
        pass

    def _ori(self, args = []):
        pass

    def _sb(self, args = []):
        pass

    def _sll(self, args = []):
        pass

    def _sllv(self, args = []):
        pass

    def _slt(self, args = []):
        pass

    def _slti(self, args = []):
        pass

    def _sltiu(self, args = []):
        pass

    def _sltu(self, args = []):
        pass

    def _sra(self, args = []):
        pass

    def _srl(self, args = []):
        pass

    def _srlv(self, args = []):
        pass

    def _sub(self, *args):
        self.regs.generalPurposes[args[0]] = args[1] + args[2]
        self.getMemory().getRegisters().advancePC()
        return

    def _subu(self, args = []):
        self._sub(args)

    def _sw(self, args = []):
        pass

    def _xor(self, args = []):
        pass

    def _xori(self, args = []):
        self._xor(args)

    def _syscall(self, args = []):
        pass

    instructions = {
        0b00000000000000000000000000100000: _add,
        0b00100000000000000000000000000000: _addi,
        0b00100100000000000000000000000000: _addiu,
        0b00000000000000000000000000100001: _addu,
        0b00000000000000000000000000100100: _and,
        0b00110000000000000000000000000000: _andi,
        0b00010000000000000000000000000000: _beq,
        0b00000100000000010000000000000000: _bgez,
        0b00000100000100010000000000000000: _bgezal,
        0b00011100000000000000000000000000: _bgtz,
        0b00011000000000000000000000000000: _blez,
        0b00000100000000000000000000000000: _bltz,
        0b00000100000100000000000000000000: _bltzal,
        0b00010100000000000000000000000000: _bne,
        0b00000000000000000000000000011010: _div,
        0b00000000000000000000000000011011: _divu,
        0b00001000000000000000000000000000: _jump,
        0b00001100000000000000000000000000: _jal,
        0b00000000000000000000000000001000: _jr,
        0b10000000000000000000000000000000: _lb,
        0b00111100000000000000000000000000: _lui,
        0b10001100000000000000000000000000: _lw,
        0b00000000000000000000000000010000: _mfhi,
        0b00000000000000000000000000010010: _mflo,
        0b00000000000000000000000000011000: _mult,
        0b00000000000000000000000000011001: _multu,
        0b00000000000000000000000000100101: _or,
        0b00110100000000000000000000000000: _ori,
        0b10100000000000000000000000000000: _sb,
        0b00000000000000000000000000000000: _sll,
        0b00000000000000000000000000000100: _sllv,
        0b00000000000000000000000000101010: _slt,
        0b00101000000000000000000000000000: _slti,
        0b00101100000000000000000000000000: _sltiu,
        0b00000000000000000000000000101011: _sltu,
        0b00000000000000000000000000000011: _sra,
        0b00000000000000000000000000000010: _srl,
        0b00000000000000000000000000000110: _srlv,
        0b00000000000000000000000000100010: _sub,
        0b00000000000000000000000000100011: _subu,
        0b10101100000000000000000000000000: _sw,
        0b00000000000000000000000000100110: _xor,
        0b00111000000000000000000000000000: _xori,
        0b00000000000000000000000000001100: _syscall
    }

