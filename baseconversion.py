# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:47:10 2021

@author: subhransu sekher bhoi
"""
#base conversion
#int to other
a=int(input('Enter an integer:'))
print('integer to binary',bin(a))
print('integer to hexadecimal',hex(a))
print('integer to octal',oct(a))
#binary to other
b=int(input('Enter a binary number'),2)
print('binary  to binary',b)
print('binary  to hexadecimal',hex(b))
print('binary to octal',oct(b))
#octal to other
c=int(input('Enter a octal number'),8)
print('octalto integer',c)
print('octal to binary',bin(c))
print('octal to hexadecimal',hex(c))
#hexadecimal to other
d=int(input('Enter a hexadecimal number'),16)
print('hexadecimal to integer',d)
print('hexadecimal to binary',bin(d))
print('hexadecimal to octal',oct(d))

''' ---------------output------------------
Enter an integer:10
integer to binary 0b1010
integer to hexadecimal 0xa
integer to octal 0o12

Enter a binary number1101
binary  to binary 13
binary  to hexadecimal 0xd
binary to octal 0o15

Enter a octal number7
octalto integer 7
octal to binary 0b111
octal to #exadecimal 0x7

Enter a hexadecimal numberf
hexadecimal to integer 15
hexadecimal to binary 0b1111
hexadecimal to octal 0o17
----------------------------------------------
'''