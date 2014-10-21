MipsSimulator
=============

Mips simulator for computer systems class


* Read File
* Save in Memory
* Goes to Infinite loop (Fetch Execute)
* Reads the instruction and finds out what to do

###### Grab a instruction word
```python
# int
instruction = memArray[pc >> 2] # shifts by 2 or divide by 4 

#int 
op = (instruction >> 26) & 0x3F # Takes the high order 6 bits

#int
sRegister = (instruction >> 21) & 0x1F

if instruction & SLL_MASK == SLL_OP # Another way of checking which instruction should be executed.

switch(op):
    ins = Instruction()
    op == ADD:
        ins = Add()
    ...
    
ins.execute()

get char from string = num % 16^2

imm = inst & 0xFFFF
se_imm = (imm & 0x8000 != 0) ? imm : ( imm | 0xFFFF0000)
   
```

###### Mask Instruction
Everywhere that there is a 0 or 1 we set the value to 1.
If there is a variable we set the value to a 0

Ex: 

Add Mask: 0000 00ss ssst tttt dddd d000 0010 0000
          1111 1100 0000 0000 0000 0111 1111 1111
            
Write a routine that gets a String and converts it to hex


#### Flow:

* Read input
* Store in Memory and Registers
* Start infinite loop
  * Read PC location in memory
  * Call Evaluate with the value stored in memory
    * Mask 1 -> Mask 2 -> Mask 3 -> Function Call
    * Function:
      * Calls get s, t, d, or h word
      * Evaluate the function with those arguments.


### Mips Instructions:

| Instruction Type | Encoding Example                        | Mask                               |
| ---              | ---                                     | ---                                |
| Register         | 0000 00ss ssst tttt dddd d000 0010 0000 | 0b11111100000000000000011111111111 |
| Immediate        | 0010 00ss ssst tttt iiii iiii iiii iiii | 0b11111100000000000000000000000000 |
| Jump / Branch    | 0000 01ss sss0 0000 iiii iiii iiii iiii | 0b11111100000111110000000000000000 |


| Instructions | Encoding                           | Operation                                                                             |
| ---          | ---                                | ---                                                                                   |
| add          | 0b00000000000000000000000000100000 | $d = $s + $t; advance_pc (4);                                                         |
| addi         | 0b00100000000000000000000000000000 | $t = $s + imm; advance_pc (4);                                                        |
| addiu        | 0b00100100000000000000000000000000 | $t = $s + imm; advance_pc (4);                                                        |
| addu         | 0b00000000000000000000000000100001 | $d = $s + $t; advance_pc (4);                                                         |
| and          | 0b00000000000000000000000000100100 | $d = $s & $t; advance_pc (4);                                                         |
| andi         | 0b00110000000000000000000000000000 | $t = $s & imm; advance_pc (4);                                                        |
| beq          | 0b00010000000000000000000000000000 | if $s == $t advance_pc (offset << 2)); else advance_pc (4);                           |
| bgez         | 0b00000100000000010000000000000000 | if $s >= 0 advance_pc (offset << 2)); else advance_pc (4);                            |
| bgezal       | 0b00000100000100010000000000000000 | if $s >= 0 $31 = PC + 8 (or nPC + 4); advance_pc (offset << 2)); else advance_pc (4); |
| bgtz         | 0b00011100000000000000000000000000 | if $s > 0 advance_pc (offset << 2)); else advance_pc (4);                             |
| blez         | 0b00011000000000000000000000000000 | if $s <= 0 advance_pc (offset << 2)); else advance_pc (4);                            |
| bltz         | 0b00000100000000000000000000000000 | if $s < 0 advance_pc (offset << 2)); else advance_pc (4);                             |
| bltzal       | 0b00000100000100000000000000000000 | if $s < 0 $31 = PC + 8 (or nPC + 4); advance_pc (offset << 2)); else advance_pc (4);  |
| bne          | 0b00010100000000000000000000000000 | if $s != $t advance_pc (offset << 2)); else advance_pc (4);                           |
| div          | 0b00000000000000000000000000011010 | $LO = $s / $t; $HI = $s % $t; advance_pc (4);                                         |
| divu         | 0b00000000000000000000000000011011 | $LO = $s / $t; $HI = $s % $t; advance_pc (4);                                         |
| j - jump     | 0b00001000000000000000000000000000 | PC = nPC; nPC = (PC & 0xf0000000) &#124; (target << 2);                               |
| 

| sll          | 0b00000000000000000000000000000000 |                                                                                       |


