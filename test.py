__author__ = 'marcus'

from numpy import binary_repr

def add():
    return 2 + 5

def addi():
    return 3 + 2

test = {
    32 : add,
    9: addi
}

def applyMask(num):
    mask = num & 0b11111100000000000000011111111111
    print mask
    return mask

def applyMask2(num):
    mask = num & 0b11111100000000000000000000000000
    print mask
    return mask

location = applyMask(0b00000000000000000000000000100000)

z = 0x27a50004
t = binary_repr(z, 32)
y = applyMask2(z)
print y
print t
print test[location]()
#print z
#print test[int(t, 2)]()

try:
    print test[4]
except:
    try:
        pass
    except:
        try:
            pass
        except:
            pass
    print "Could not find"