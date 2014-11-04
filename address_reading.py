__author__ = 'marcus'

import ctypes

class Fields(object):

    def __init__(self, s, t, d, imm, s_imm, sh, jump):
        self.s = s
        self.t = t
        self.d = d
        self.imm = imm
        self.s_imm = s_imm
        self.sh = sh
        self.jump = jump

class ReadAddress(object):

    def applyMaskRegister(self, num):
        return num & 0b11111100000000000000011111111111

    def applyMaskImmediate(self, num):
        return num & 0b11111100000000000000000000000000

    def applyMaskJump(self, num):
        return num & 0b11111100000000000000000000111111

    def applyMaskMFHI_LO(self, num):
        return num & 0b11111111111111110000011111111111

    def applyOtherMask(self, num):
        return num & 0b11111100000111110000000000000000

    def sign_extend(self, val):
        return int(val | 0xFFFF0000) - 2**32 if (val & 0x8000 != 0) else val

    def int32_to_uint32(self, i):
        return ctypes.c_uint32(i).value

    def get_fields(self, num):
        s = (num >> 21) & 0x1F
        t = (num >> 16) & 0x1F
        d = (num >> 11) & 0x1F
        imm = (num & 0xFFFF)
        s_imm = self.sign_extend(imm)
        sh = (num >> 6) & 0x1F
        jump = num & 0x3FFFFFF
        return Fields(s, t, d, imm, s_imm, sh, jump)