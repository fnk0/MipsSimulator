MipsSimulator
=============

Mips simulator for computer systems class


* Read File
* Save in Memory
* Goes to Infinite loop (Fetch Execute)
* Reads the instruction and finds out what to do

###### Grab a instruction word
```python
instruction = memArray[pc >> 2] # shifts by 2 or divide by 4 
```