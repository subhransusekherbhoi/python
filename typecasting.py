# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:34:16 2021

@author:subhransu

"""
i=int(input('Enter an integer:'))
f=float(input('Enter an float:'))
s=str(input('Enter an string but only in numbers:'))
c=complex(input('Enter an complex number:'))
#other datatype to intger
x= int(f) 
y = int(s)
print('float to int:',x,'\n','string to int:',y)
print('\n')
#other to float
x = float(i)    
y = float(f)   
z = float(s)   
print('int to float:',x,'\n','float to float:',y,'\n','string to float',z)
print('\n')
#other to str
x = str(s) 
y = str(i)    
z = str(f)
print('string to string:',x,'\n','int to str:',y,'\n','float to str',z)
print('\n')
#complex
c=4+3j
print(type(c))
print(id(c))
print(complex(c))
print(c.imag)
print(c.real)   
'''-----------------output--------------
Enter an integer:10

Enter an float:2.

Enter an string but only in numbers:2

Enter an complex number:3+4j
float to int: 2 
 string to int: 2


int to float: 10.0 
 float to float: 2.0 
 string to float 2.0


string to string: 2 
 int to str: 10 
 float to str 2.0


<class 'complex'>
2110783632656
(4+3j)
3.0
4.0
----------------------------------------------
'''
