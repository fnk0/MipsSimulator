__author__ = 'marcus'

from numpy import binary_repr

reg = [0] * 31
#[0x00000004]	0x27a50004  addiu $5, $29, 4
#[0x00000008]	0x24a60004  addiu $6, $5, 4
#[0x00000040]	0x01002021  add $4, $8, $0
# 0010 01ss ssst tttt iiii iiii iiii iiii
# $t = $s + imm; advance_pc (4);

def add(args = []):
    reg[args[0]] = reg[args[1]] + reg[args[2]]
    return reg[args[0]]

def addiu(args = []):
    reg[args[0]] = reg[args[1]] + args[2]
    return reg[args[0]]

def sll():
    return 4 << 2

def get_t_word(num):
    return (num >> 16) & 0x1F

def get_d_word(num):
    return (num >> 11) & 0x1F

def get_s_word(num):
    return (num >> 21) & 0x1F

def get_imm_val(num):
    return (num & 0xFFFF)

def get_immediate_words(num):
    t_word = get_t_word(num)
    s_word = get_s_word(num)
    val = sign_extend(get_imm_val(num))
    return [t_word, s_word, val]

def sign_extend(val):
    return (val | 0xFFFF0000) if (val & 0x8000 != 0) else val

test = {
    0b00000000000000000000000000100000: (add, get_d_word),
    0b00100100000000000000000000000000: (addiu, get_immediate_words),
    0b00000000000000000000000000000000: (sll, get_d_word)
}

def applyMask(num):
    mask = num & 0b11111100000000000000011111111111
    #print "Mask 1: " + str(int(mask))
    return mask

def applyMask2(num):
    mask = num & 0b11111100000000000000000000000000
    #print "Mask 2: " + str(mask)
    return mask

def applyMask3(num):
    mask = num & 0b1111110000011111000000000000
    #print "Mask 3: " + str(mask)
    return mask


location = applyMask(0b00000000000000000000000000100000)

z = 0x27a50004
w = 0x24a60004
y = 0x00000040


def calculate(z):
    try:
        y = applyMask(z)
        print test[y][1](z)
        return (test[y][0](test[y][1](z)))
    except:
        pass
    try:
        y = applyMask2(z)
        print test[y][1](z)
        return (test[y][0](test[y][1](z)))
    except:
        pass
    try:
        y = applyMask3(z)
        return (test[y][0](test[y][1](z)))
    except:
        return "Could not find"


print calculate(z)
print calculate(w)
