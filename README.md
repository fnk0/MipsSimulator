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
| jal          | 0b00001100000000000000000000000000 | $31 = PC + 8 (or nPC + 4); PC = nPC; nPC = (PC & 0xf0000000) &#124; (target << 2);    |
| jr           | 0b00000000000000000000000000001000 | PC = nPC; nPC = $s;                                                                   |
| lb           | 0b10000000000000000000000000000000 | $t = MEM[$s + offset]; advance_pc (4);                                                |
| lui          | 0b00111100000000000000000000000000 | $t = (imm << 16); advance_pc (4);                                                     |
| lw           | 0b10001100000000000000000000000000 | $t = MEM[$s + offset]; advance_pc (4);                                                |
| mfhi         | 0b00000000000000000000000000010000 | $d = $HI; advance_pc (4);                                                             |
| mflo         | 0b00000000000000000000000000010010 | $d = $LO; advance_pc (4);                                                             |
| mult         | 0b00000000000000000000000000011000 | $LO = $s * $t; advance_pc (4);                                                        |
| multu        | 0b00000000000000000000000000011001 | $LO = $s * $t; advance_pc (4);                                                        |
| noop         | 0b00000000000000000000000000000000 | advance_pc (4);                                                                       |
| or           | 0b00000000000000000000000000100101 | $d = $s &#124; $t; advance_pc (4);                                                    |
| ori          | 0b00110100000000000000000000000000 | $t = $s &#124; imm; advance_pc (4);                                                   |
| sb           | 0b10100000000000000000000000000000 | MEM[$s + offset] = (0xff & $t); advance_pc (4);                                       |
| sll          | 0b00000000000000000000000000000000 | $d = $t << h; advance_pc (4);                                                         |
| sllv         | 0b00000000000000000000000000000100 | $d = $t << $s; advance_pc (4)                                                         |
| slt          | 0b00000000000000000000000000101010 | if $s < $t $d = 1; advance_pc (4); else $d = 0; advance_pc (4);                       |
| slti         | 0b00101000000000000000000000000000 | if $s < imm $t = 1; advance_pc (4); else $t = 0; advance_pc (4);                      |
| sltiu        | 0b00101100000000000000000000000000 | if $s < imm $t = 1; advance_pc (4); else $t = 0; advance_pc (4);                      |
| sltu         | 0b00000000000000000000000000101011 | if $s < $t $d = 1; advance_pc (4); else $d = 0; advance_pc (4);                       |
| sra          | 0b00000000000000000000000000000011 | $d = $t >> h; advance_pc (4);                                                         |
| srl          | 0b00000000000000000000000000000010 | $d = $t >> h; advance_pc (4);                                                         |
| srlv         | 0b00000000000000000000000000000110 | $d = $t >> $s; advance_pc (4);                                                        |
| sub          | 0b00000000000000000000000000100010 | $d = $s - $t; advance_pc (4);                                                         |
| subu         | 0b00000000000000000000000000100011 | $d = $s - $t; advance_pc (4);                                                         |
| sw           | 0b10101100000000000000000000000000 | MEM[$s + offset] = $t; advance_pc (4);                                                |
| syscall      | 0b00000000000000000000000000001100 | advance_pc (4)                                                                        |
| xor          | 0b00000000000000000000000000100110 | $d = $s ^ $t; advance_pc (4);                                                         |
| xori         | 0b00111000000000000000000000000000 | $t = $s ^ imm; advance_pc (4);                                                        |



