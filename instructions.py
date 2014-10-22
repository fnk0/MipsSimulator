__author__ = 'marcus'

from base import Memory, Registers
from address_reading import ReadAddress

class Instruction(object):

    rA = ReadAddress()

    def __init__(self, regs, mem, sys):
        self.regs = regs
        self.mem = mem
        self.s_call = sys

    def evaluate(self, num):
        try:
            ins = self.rA.applyMaskRegister(num)
            (self.instructions[ins][0](self, self.instructions[ins][1](num)))
        except:
            pass
        try:
            #return (test[y][0](test[y][1](z)))
            ins = self.rA.applyMaskJump(num)
            (self.instructions[ins][0](self, self.instructions[ins][1](num)))
        except:
            pass
        try:
            ins = self.rA.applyMaskImmediate(num)
            (self.instructions[ins][0](self, self.instructions[ins][1](num)))
        except:
            return

    def getMemory(self):
        return self.mem

    def _add(self, args = []): #$d = $s + $t; advance_pc (4);
        self.regs.set_value_for_register(args[0], args[1] + args[2])
        self.regs.advance_pc()

    def _addi(self, args = []):
        self._add(args)

    def _addu(self, args = []):
        self._add(args)

    def _addiu(self, args = []):
        self._add(args)

    def _and(self, args = []): #$d = $s & $t; advance_pc (4);
        self.regs.generalPurposes[args[0]] = args[1] & args[2]

    def _andi(self, args = []): #$t = $s & imm; advance_pc (4);
        self._and(args)

    def _beq(self, args = []):
        self.regs.advance_pc(args[1] << 2) if args[0] == args[1] else self.regs.advance_pc()

    def _bgez(self, args = []): #if $s == $t advance_pc (offset << 2)); else advance_pc (4);
        self.regs.advance_pc(args[1] << 2) if args[0] >= args[1] else self.regs.advance_pc()

    def _bgezal(self, args = []): #if $s >= 0 $31 = PC + 8 (or nPC + 4); advance_pc (offset << 2)); else advance_pc (4);
        if args[0] >= 0:
            self.regs.set_value_for_register(31, self.regs.PC + 8)
            self.regs.advance_pc(args[1] << 2)
        else:
            self.regs.advance_pc()

    def _bgtz(self, args = []): #if $s > 0 advance_pc (offset << 2)); else advance_pc (4);
        self.regs.advance_pc(args[1] << 2) if args[0] > 0 else self.regs.advance_pc()

    def _blez(self, args = []): #if $s <= 0 advance_pc (offset << 2)); else advance_pc (4)
        self.regs.advance_pc(args[1] << 2) if args[0] <= 0 else self.regs.advance_pc()

    def _bltz(self, args = []): #if $s < 0 advance_pc (offset << 2)); else advance_pc (4);
        self.regs.advance_pc(args[1] << 2) if args[0] < 0 else self.regs.advance_pc()

    def _bltzal(self, args = []): #if $s < 0 $31 = PC + 8 (or nPC + 4); advance_pc (offset << 2)); else advance_pc (4);
        pass

    def _bne(self, args = []): #if $s != $t advance_pc (offset << 2)); else advance_pc (4)
        self.regs.advance_pc(args[2] << 2) if args[0] != args[1] else self.regs.advance_pc()

    def _div(self, args = []): #$LO = $s / $t; $HI = $s % $t; advance_pc (4);
        self.regs.LO = args[0] / args[1]
        self.regs.HI = args[0] / args[1]
        self.regs.advance_pc()

    def _divu(self, args = []):     #$LO = $s / $t; $HI = $s % $t; advance_pc (4);
        self._div(args)

    def _jump(self, arg): #PC = nPC; nPC = (PC & 0xf0000000) | (target << 2);
        self.regs.PC = self.regs.nPC
        self.regs.nPC = self.regs.PC & 0xf0000000 | arg << 2

    def _jal(self, arg): #$31 = PC + 8 (or nPC + 4); PC = nPC; nPC = (PC & 0xf0000000) | (target << 2);
        self.regs.set_value_for_register(31, self.regs.PC + 8)
        self.regs.PC = self.regs.nPC
        self.regs.nPC = (self.regs.PC & 0xf0000000) | (arg << 2)

    def _jr(self, arg): #PC = nPC; nPC = $s;
        self.regs.PC = self.regs.nPC
        self.regs.nPC = arg

    def _lb(self, args = []):     #$t = MEM[$s + offset]; advance_pc (4);
        self.regs.set_value_for_register(args[1], self.mem.get_val_in_address(args[0] + args[2]))
        self.regs.advance_pc()

    def _lui(self, args = []):     #$t = (imm << 16); advance_pc (4);
        self.regs.set_value_for_register(args[0], args[2] << 16)
        self.regs.advance_pc()

    def _lw(self, args = []):     #$t = MEM[$s + offset]; advance_pc (4);
        self.regs.set_value_for_register(args[0], self.mem.get_val_in_address(args[1] + args[2]))
        self.regs.advance_pc()

    def _mfhi(self, arg): #$d = $HI; advance_pc (4);
        self.regs.generalPurposes(arg, self.regs.HI)
        self.regs.advance_pc()

    def _mflo(self, arg): #$d = $LO; advance_pc (4);
        self.regs.generalPurposes(arg, self.regs.LO)
        self.regs.advance_pc()

    def _mult(self, args = []): # $LO = $s * $t; advance_pc (4);
        self.regs.LO = args[0] * args[1]
        self.regs.advance_pc()

    def _multu(self, args=[]):
        self._mult(args)

    def _noop(self, args = []):
        pass

    def _or(self, args = []): #$d = $s | $t; advance_pc (4);
        self.regs.set_value_for_register(args[0], args[1] | args[2])
        self.regs.advance_pc()

    def _ori(self, args = []):
        self._or(args)

    def _sb(self, args = []): #MEM[$s + offset] = (0xff & $t); advance_pc (4);
        self.mem.setValInAddress(args[0] + args[2], 0xff & args[1])
        self.regs.advance_pc()

    def _sll(self, args = []): #$d = $t << h; advance_pc (4);
        self.regs.set_value_for_register(args[0], args[2] << args[1])
        self.regs.advance_pc()

    def _sllv(self, args = []): #$d = $t << $s; advance_pc (4);
        self._sll(args)

    def _slt(self, args = []): #if $s < $t $d = 1; advance_pc (4); else $d = 0; advance_pc (4);
        self.regs.set_value_for_register(args[0], 1) if args[1] < args[2] else self.regs.set_value_for_register(args[0], 0)
        self.regs.advance_pc()

    def _slti(self, args = []): #if $s < imm $t = 1; advance_pc (4); else $t = 0; advance_pc (4);
        self._slt(args) # change the args[0] from d to t

    def _sltiu(self, args = []): #if $s < imm $t = 1; advance_pc (4); else $t = 0; advance_pc (4);
        self._slti(args)

    def _sltu(self, args = []): #if $s < $t $d = 1; advance_pc (4); else $d = 0; advance_pc (4);
        self._slt(args)

    def _sra(self, args = []): #$d = $t >> h; advance_pc (4);
        self.regs.set_value_for_register(args[0], args[1] >> args[2])
        self.regs.advance_pc()

    def _srl(self, args = []): #$d = $t >> h; advance_pc (4);
        self._sra(args)

    def _srlv(self, args = []): #$d = $t >> $s; advance_pc (4);
        self._srl(args)

    def _sub(self, *args): #$d = $s - $t; advance_pc (4);
        self.regs.generalPurposes[args[0]] = args[1] + args[2]
        self.getMemory().get_registers().advance_pc()
        return

    def _subu(self, args = []): #$d = $s - $t; advance_pc (4);
        self._sub(args)

    def _sw(self, args = []): #MEM[$s + offset] = $t; advance_pc (4);
        self.mem.setValInAddress(args[0] + args[2], args[1])
        self.regs.advance_pc()

    def _xor(self, args = []): #$d = $s ^ $t; advance_pc (4);
        self.regs.set_value_for_register(args[0], args[1] ^ args[2])
        self.regs.advance_pc()

    def _xori(self, args = []):
        self._xor(args)

    def _syscall(self, val):
        self.s_call._syscall_funs[val]() # calls the function stored in the value position of the syscall dictionary

    instructions = {
        0b00000000000000000000000000100000: (_add,rA.get_dst_words),
        0b00100000000000000000000000000000: (_addi, rA.get_immediate_words_signed),
        0b00100100000000000000000000000000: (_addiu, rA.get_immediate_words),
        0b00000000000000000000000000100001: (_addu, rA.get_immediate_words),
        0b00000000000000000000000000100100: (_and, rA.get_dst_words),
        0b00110000000000000000000000000000: (_andi, rA.get_immediate_words),
        0b00010000000000000000000000000000: (_beq, rA.get_branch_with_t_offset),
        0b00000100000000010000000000000000: (_bgez, rA.get_branch_with_offset),
        0b00000100000100010000000000000000: (_bgezal, rA.get_branch_with_offset),
        0b00011100000000000000000000000000: (_bgtz, rA.get_branch_with_offset),
        0b00011000000000000000000000000000: (_blez, rA.get_branch_with_offset),
        0b00000100000000000000000000000000: (_bltz, rA.get_branch_with_offset),
        0b00000100000100000000000000000000: (_bltzal, rA.get_branch_with_offset),
        0b00010100000000000000000000000000: (_bne, rA.get_branch_with_t_offset),
        0b00000000000000000000000000011010: (_div, rA.get_st_words),
        0b00000000000000000000000000011011: (_divu, rA.get_st_words),
        0b00001000000000000000000000000000: (_jump, rA.get_jump_word),
        0b00001100000000000000000000000000: (_jal, rA.get_jump_word),
        0b00000000000000000000000000001000: (_jr, rA.get_s_word),
        0b10000000000000000000000000000000: (_lb, rA.get_branch_with_t_offset),
        0b00111100000000000000000000000000: (_lui, rA.get_immediate_words),
        0b10001100000000000000000000000000: (_lw, rA.get_immediate_words),
        0b00000000000000000000000000010000: (_mfhi, rA.get_d_word),
        0b00000000000000000000000000010010: (_mflo, rA.get_d_word),
        0b00000000000000000000000000011000: (_mult, rA.get_st_words),
        0b00000000000000000000000000011001: (_multu, rA.get_st_words),
        0b00000000000000000000000000100101: (_or, rA.get_dst_words),
        0b00110100000000000000000000000000: (_ori, rA.get_immediate_words),
        0b10100000000000000000000000000000: (_sb, rA.get_t_offset_words),
        0b00000000000000000000000000000000: (_sll, rA.get_dht_words),
        0b00000000000000000000000000000100: (_sllv, rA.get_dst_words),
        0b00000000000000000000000000101010: (_slt, rA.get_dst_words),
        0b00101000000000000000000000000000: (_slti, rA.get_immediate_words_signed),
        0b00101100000000000000000000000000: (_sltiu, rA.get_immediate_words),
        0b00000000000000000000000000101011: (_sltu, rA.get_dst_words),
        0b00000000000000000000000000000011: (_sra, rA.get_dht_words),
        0b00000000000000000000000000000010: (_srl, rA.get_dht_words),
        0b00000000000000000000000000000110: (_srlv, rA.get_dst_words),
        0b00000000000000000000000000100010: (_sub, rA.get_dst_words),
        0b00000000000000000000000000100011: (_subu, rA.get_dst_words),
        0b10101100000000000000000000000000: (_sw, rA.get_branch_with_t_offset),
        0b00000000000000000000000000100110: (_xor, rA.get_dst_words),
        0b00111000000000000000000000000000: (_xori, rA.get_immediate_words),
        0b00000000000000000000000000001100: _syscall
    }