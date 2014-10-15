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
op = (instruction >> 26) & 0x7F # Takes the high order 6 bits

#int
sRegister = (instruction >> 21) & 0x1F

```