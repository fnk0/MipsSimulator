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
    if op == ADD:
        ins = Add()
    ...
    
    ins.execute()
   
```

###### Mask Instruction
Everywhere that there is a 0 or 1 we set the value to 1.
If there is a variable we set the value to a 0

Ex: 

Add Mask: 0000 00ss ssst tttt dddd d000 0010 0000
          1111 1100 0000 0000 0000 0111 1111 1111
            
Write a routine that gets a String and converts it to hex
