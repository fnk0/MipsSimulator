__author__ = 'marcus'

class ReadAddress:

    def __init__(self):
        pass

    def applyMaskRegister(self, num):
        mask = num & 0b11111100000000000000011111111111
        d_word = (num >> 11) & 0x3F
        #print d_word
        return mask

    def applyMaskImmediate(self, num):
        mask = num & 0b11111100000000000000000000000000
        return mask

    def applyMaskJump(self, num):
        mask = num & 0b11111100000000000000000000111111
        return mask

    def get_t_word(self, num):
        return (num >> 16) & 0x1F

    def get_d_word(self, num):
        return (num >> 11) & 0x1F

    def get_s_word(self, num):
        return (num >> 21) & 0x1F

    def get_imm_val(self, num):
        return (num & 0xFFFF)

    def get_h_word(self, num):
        return (num >> 6) & 0x1F

    def get_offset_word(self, num):
        return (num & 0xFFFF)

    def get_jump_word(self, num):
        return self.sign_extend(num & 0x3FFFFFF)

    def get_dst_words(self, num): #returns $d, $s, $t
        return [self.get_d_word(num), self.get_s_word(num), self.get_t_word(num)]

    def get_st_words(self, num): #returns  $s, $t
        return [self.get_s_word(num), self.get_t_word(num)]

    def get_immediate_words(self, num): #returns $t, $s0, imm
        return [self.get_t_word(num), self.get_s_word(num), self.get_imm_val(num)]

    def get_immediate_words_signed(self, num):
        return [self.get_t_word(num), self.get_s_word(num), self.sign_extend(self.get_imm_val(num))]

    def get_branch_with_t_offset(self, num):
        return [self.get_s_word(num), self.get_t_word(num), self.get_offset_word(num)]

    def get_branch_with_offset(self, num):
        return [self.get_s_word(num), self.get_offset_word(num)]

    def sign_extend(self, val):
        return (val | 0xFFFF0000) if (val & 0x8000 != 0) else val


