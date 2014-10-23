__author__ = 'marcus'

from numpy import binary_repr
from numpy import unpackbits
import binascii

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

def get_ch4(num):
    return chr((num >> 24) & 0xFF)

def get_ch3(num):
    return chr((num >> 16) & 0xFF)

def get_ch2(num):
    return chr((num >> 8) & 0xFF)

def get_ch1(num):
    return chr(num & 0xFF)

z = 0x27a50004
w = 0x24a60004
y = 0x00000040

# 0110 1100 0110 1100 0110 0101 0100 1000
# 1819043144

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


# print calculate(z)
# print calculate(w)

t = 1819043144
t1 = 0x6f57206f
t2 = 0x00646c72
t3 = 0x00000000

"""
print get_ch1(t)
print get_ch2(t)
print get_ch3(t)
print get_ch4(t)

print get_ch1(t1)
print get_ch2(t1)
print get_ch3(t1)
print get_ch4(t1)

print get_ch1(t2)
print get_ch2(t2)
print get_ch3(t2)
print get_ch4(t2)
"""

def numfy(s):
    number = 0
    for e in [ord(c) for c in s]:
        number = (number * 0x110000) + e
    return number

def denumfy(number):
    l = []
    while(number != 0):
        l.append(chr(number % 0x110000))
        number = number // 0x110000
    return ''.join(reversed(l))

t_str = "Hello World"

x = ''.join(format(ord(i),'b').zfill(8) for i in t_str)
print x
arr = []
counter = 0
while True:
    num = 0
    try:
        num1 = int(x[24 + counter:32 + counter], 2)
        num2 = int(x[16 + counter:24 + counter], 2)
        num3 = int(x[8 + counter:16 + counter], 2)
        num4 = int(x[0 + counter:8 + counter], 2)

        print str(num1) + str(num2) + str(num3) + str(num4)

        arr.append(num)
        counter += 32
    except:
        arr.append(num)
        break

print arr

print get_ch4(arr[2])

print numfy(t_str)

a = [ord(c) for c in t_str]

print a
sl = []
s = ""
"""
count = 1
for b in a:
    s = hex(b)[2:] + s
    if count % 4 == 0:
        sl.append("0x" + s)
        s = ""
    count +=1
sl.append(s)
sl.append("00000000")
"""

for i  in range(0, len(a), 1):
    s = hex(a[i])[2:] + s
    if (i + 1) % 4 == 0 or i == len(a) -1:
        sl.append("0x" + s)
        s = ""
sl.append("0x00000000")

xi = [int(zx, 16) for zx in sl]
print sl
print xi


mfhi = 0x00005810

def applyMaskJump(num):
    return num & 0b11111100000000000000000000111111

print applyMaskJump(mfhi)

sxz = 0x27a50004

print sxz & 0b11111100000000000000000000000000
print 0b11111100000000000000000000000000 & 0b00100100000000000000000000000000



