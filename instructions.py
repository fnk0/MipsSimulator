__author__ = 'marcus'

from base import Memory, Registers
from address_reading import ReadAddress, Fields

class Instruction(object):

    rA = ReadAddress()

    def __init__(self, regs, mem, sys):
        self.regs = regs
        self.mem = mem
        self.s_call = sys

    def evaluate(self, num):
        if num == 0:
            self._nop()
            return
        f = self.rA.get_fields(num)
        self.get_instruction(num)(self, f)

    def get_instruction(self, num):
        ins = 0
        if self.instructions.has_key(self.rA.applyMaskRegister(num)):
            ins = self.rA.applyMaskRegister(num)
        elif self.instructions.has_key(self.rA.applyMaskJump(num)):
            ins = self.rA.applyMaskJump(num)
        elif self.instructions.has_key(self.rA.applyOtherMask(num)):
            ins = self.rA.applyOtherMask(num)
        elif self.instructions.has_key(self.rA.applyMaskMFHI_LO(num)):
            ins = self.rA.applyMaskMFHI_LO(num)
        elif self.instructions.has_key(self.rA.applyMaskImmediate(num)):
            ins = self.rA.applyMaskImmediate(num)

        return self.instructions[ins]


    def get_memory(self):
        return self.mem

    def _add(self, f): #$d = $s + $t; advance_pc (4);
        self.regs.set_value_for_register(f.d, self.regs.generalPurposes[f.s] + self.regs.generalPurposes[f.t])
        self.regs.advance_pc()

    def _addi(self, f): # $t = $s + imm; advance_pc (4);
        self.regs.set_value_for_register(f.t, self.regs.generalPurposes[f.s] + f.s_imm)
        self.regs.advance_pc()

    def _addu(self, f): #$d = $s + $t; advance_pc (4)
        self._add(f)

    def _addiu(self, f): #$t = $s + imm; advance_pc (4);
        self.regs.set_value_for_register(f.t, int(self.regs.generalPurposes[f.s] + f.s_imm))
        self.regs.advance_pc()

    def _and(self, f): #$d = $s & $t; advance_pc (4);
        self.regs.set_value_for_register(f.d, self.regs.generalPurposes[f.s] & self.regs.generalPurposes[f.t])
        self.regs.advance_pc()

    def _andi(self, f): #$t = $s & imm; advance_pc (4);
        self.regs.set_value_for_register(f.t, self.regs.generalPurposes[f.s] & f.imm)
        self.regs.advance_pc()

    def _beq(self, f): # if $s == $t advance_pc (offset << 2)); else advance_pc (4);
        self.regs.advance_pc(f.s_imm << 2) if self.regs.generalPurposes[f.s] == self.regs.generalPurposes[f.t] else self.regs.advance_pc()

    def _bgez(self, f): # if $s >= 0 advance_pc (offset << 2)); else advance_pc (4);
        self.regs.advance_pc(f.s_imm << 2) if self.regs.generalPurposes[f.s] >= 0 else self.regs.advance_pc()

    def _bgezal(self, f): #if $s >= 0 $31 = PC + 8 (or nPC + 4); advance_pc (offset << 2)); else advance_pc (4);
        if self.regs.generalPurposes[f.s] >= 0:
            self.regs.set_value_for_register(31, self.regs.PC + 8)
            self.regs.advance_pc(f.s_imm << 2)
        else:
            self.regs.advance_pc()

    def _bgtz(self, f): #if $s > 0 advance_pc (offset << 2)); else advance_pc (4);
        self.regs.advance_pc(f.s_imm << 2) if self.regs.generalPurposes[f.s] > 0 else self.regs.advance_pc()

    def _blez(self, f): #if $s <= 0 advance_pc (offset << 2)); else advance_pc (4)
        self.regs.advance_pc(f.s_imm << 2) if self.regs.generalPurposes[f.s] <= 0 else self.regs.advance_pc()

    def _bltz(self, f): #if $s < 0 advance_pc (offset << 2)); else advance_pc (4);
        self.regs.advance_pc(f.s_imm << 2) if self.regs.generalPurposes[f.s] < 0 else self.regs.advance_pc()

    def _bltzal(self, f): #if $s < 0 $31 = PC + 8 (or nPC + 4); advance_pc (offset << 2)); else advance_pc (4);
        if self.regs.generalPurposes[f.s] < 0:
            self.regs.set_value_for_register(31, self.regs.PC + 8)
            self.regs.advance_pc(f.s_imm << 2)
        else:
            self.regs.advance_pc()

    def _bne(self, f): #if $s != $t advance_pc (offset << 2)); else advance_pc (4)
        self.regs.advance_pc(f.s_imm << 2) if self.regs.generalPurposes[f.s] != self.regs.generalPurposes[f.t] else self.regs.advance_pc()

    def _div(self, f): #$LO = $s / $t; $HI = $s % $t; advance_pc (4);
        self.regs.LO = self.regs.generalPurposes[f.s] / self.regs.generalPurposes[f.t]
        self.regs.HI = self.regs.generalPurposes[f.s] % self.regs.generalPurposes[f.t]
        self.regs.advance_pc()

    def _divu(self, f):     #$LO = $s / $t; $HI = $s % $t; advance_pc (4);
        self._div(f)

    def _jump(self, f): #PC = nPC; nPC = (PC & 0xf0000000) | (target << 2);
        self.regs.PC = self.regs.nPC
        self.regs.nPC = (self.regs.PC & 0xf0000000) | (f.jump << 2)

    def _jal(self, f): #$31 = PC + 8 (or nPC + 4); PC = nPC; nPC = (PC & 0xf0000000) | (target << 2);
        self.regs.set_value_for_register(31, self.regs.PC + 8)
        self.regs.PC = self.regs.nPC
        self.regs.nPC = (self.regs.PC & 0xf0000000) | (f.jump << 2)

    def _jr(self, f): #PC = nPC; nPC = $s;
        self.regs.PC = self.regs.nPC
        self.regs.nPC = self.regs.generalPurposes[f.s]

    def _lb(self, f):     #$t = MEM[$s + offset]; advance_pc (4);
        self.regs.set_value_for_register(f.t, self.mem.get_val_in_address(self.regs.generalPurposes[f.s] + f.s_imm))
        self.regs.advance_pc()

    def _lui(self, f):     #$t = (imm << 16); advance_pc (4);
        self.regs.set_value_for_register(f.t, f.imm << 16)
        self.regs.advance_pc()

    def _lw(self, f):     #$t = MEM[$s + offset]; advance_pc (4);
        self.regs.set_value_for_register(f.t, self.mem.get_val_in_address(self.regs.generalPurposes[f.s] + f.s_imm))
        self.regs.advance_pc()

    def _mfhi(self, f): #$d = $HI; advance_pc (4);
        self.regs.set_value_for_register(f.d, self.regs.HI)
        self.regs.advance_pc()

    def _mflo(self, f): #$d = $LO; advance_pc (4);
        self.regs.set_value_for_register(f.d, self.regs.LO)
        self.regs.advance_pc()

    def _mult(self, f): # $LO = $s * $t; advance_pc (4);
        self.regs.LO = self.regs.generalPurposes[f.s] * self.regs.generalPurposes[f.t]
        self.regs.advance_pc()

    def _multu(self, f):
        self._mult(f)

    def _nop(self):
        self.regs.advance_pc()

    def _or(self, f): #$d = $s | $t; advance_pc (4);
        self.regs.set_value_for_register(f.d, self.regs.generalPurposes[f.s] | self.regs.generalPurposes[f.t])
        self.regs.advance_pc()

    def _ori(self, f): #$t = $s | imm; advance_pc (4);
        self.regs.set_value_for_register(f.t, self.regs.generalPurposes[f.s] | f.imm)
        self.regs.advance_pc()

    def _sb(self, f): #MEM[$s + offset] = (0xff & $t); advance_pc (4);
        self.mem.set_val_to_address(self.regs.generalPurposes[f.s] + f.s_imm, 0xff & self.regs.generalPurposes[f.t])
        self.regs.advance_pc()

    def _sll(self, f): #$d = $t << h; advance_pc (4);
        self.regs.set_value_for_register(f.d, self.regs.generalPurposes[f.t] << f.sh)
        self.regs.advance_pc()

    def _sllv(self, f): #$d = $t << $s; advance_pc (4);
         self.regs.set_value_for_register(f.d, self.regs.generalPurposes[f.t] << self.regs.generalPurposes[f.s])
         self.regs.advance_pc()

    def _slt(self, f): #if $s < $t $d = 1; advance_pc (4); else $d = 0; advance_pc (4);
        self.regs.set_value_for_register(f.d, 1) if self.regs.generalPurposes[f.s] < self.regs.generalPurposes[f.t] else self.regs.set_value_for_register(f.d, 0)
        self.regs.advance_pc()

    def _slti(self, f): #if $s < imm $t = 1; advance_pc (4); else $t = 0; advance_pc (4);
         self.regs.set_value_for_register(f.t, 1) if self.regs.generalPurposes[f.s] < f.s_imm else self.regs.set_value_for_register(f.t, 0)
         self.regs.advance_pc()

    def _sltiu(self, f): #if $s < imm $t = 1; advance_pc (4); else $t = 0; advance_pc (4);
        self.regs.set_value_for_register(f.t, 1) if self.regs.generalPurposes[f.s]< f.imm else self.regs.set_value_for_register(f.t, 0)
        self.regs.advance_pc()

    def _sltu(self, f): #if $s < $t $d = 1; advance_pc (4); else $d = 0; advance_pc (4);
        self._slt(f)

    def _sra(self, f): #$d = $t >> h; advance_pc (4);
        self.regs.set_value_for_register(f.d, self.regs.generalPurposes[f.t] >> f.sh)
        self.regs.advance_pc()

    def _srl(self, f): #$d = $t >> h; advance_pc (4);
        self._sra(f)

    def _srlv(self, f): #$d = $t >> $s; advance_pc (4);
        self.regs.set_value_for_register(f.d, self.regs.generalPurposes[f.t] >> self.regs.generalPurposes[f.s])
        self.regs.advance_pc()

    def _sub(self, f): #$d = $s - $t; advance_pc (4);
        self.regs.set_value_for_register(f.d, self.regs.generalPurposes[f.s] - self.regs.generalPurposes[f.t])
        self.regs.advance_pc()

    def _subu(self, f): #$d = $s - $t; advance_pc (4);
        self._sub(f)

    def _sw(self, f): #MEM[$s + offset] = $t; advance_pc (4);
        temp = (self.regs.generalPurposes[f.s] + f.s_imm)
        temp2 = self.regs.generalPurposes[f.t]
        self.mem.set_val_to_address(temp2, temp)
        self.regs.advance_pc()

    def _xor(self, f): #$d = $s ^ $t; advance_pc (4);
        self.regs.set_value_for_register(f.d, self.regs.generalPurposes[f.s] ^ self.regs.generalPurposes[f.t])
        self.regs.advance_pc()

    def _xori(self, f): #$t = $s ^ imm; advance_pc (4);
        self.regs.set_value_for_register(f.t, self.regs.generalPurposes[f.s] ^ f.imm)
        self.regs.advance_pc()

    def _syscall(self, f):
        self.s_call._syscall_funs[self.regs.generalPurposes[2]](self.s_call) # calls the function stored in the value position of the syscall dictionary
        self.regs.advance_pc()

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
        0b00000000000000000000000000001100: _syscall,
    }