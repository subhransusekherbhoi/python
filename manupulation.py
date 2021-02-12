# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:05:53 2021

@author: Subhransu
"""
#list
list1=[10,20,30,40,'sam',50,'vikash',60]
print(list1.append(20))#insert from the end
print(list1)
print(list1.pop(6))#remove element from a index
print(list1.count(20))#count number of dublicates
print(list1.remove(50))#remove elements from end
print(list1)
print(type(list1))
list2=[10,20,[55,22,44,'sam'],5,88,77]
print('To display a character of a word inside a list which is inside of list2 i.e;',list2[2][3][0])
list2.append(50)
print(list2)
print('\n')
#tuple
#tuple is immutable so we can't perform any manupulating function
tup1=(10,20,220,50,'soap',55,20)
print(tup1)
print(tup1.count(20))#count number of dublicates
print(tup1.index(10))#returns index numbers
print('\n')
#dict
#dict is mutable
dict1={1:'sony',2:'cannon',3:'leica',4:'nikon'}
print(dict1.keys())
print(dict1.values())
print(type(dict1))
print('\n')
#set
#set is mutable
set1={1,2,3,'acting','dancing',5,8,9}
print(type(set1))
set1.add(55)#add the number in any index
print(set1)#doesn't display in sequence and also doesn't support indexing

'''
-----------------output--------------
None
[10, 20, 30, 40, 'sam', 50, 'vikash', 60, 20]
vikash
2
None
[10, 20, 30, 40, 'sam', 60, 20]
<class 'list'>
To display a character of a word inside a list which is inside of list2 i.e; s
[10, 20, [55, 22, 44, 'sam'], 5, 88, 77, 50]


(10, 20, 220, 50, 'soap', 55, 20)
2
0


dict_keys([1, 2, 3, 4])
dict_values(['sony', 'cannon', 'leica', 'nikon'])
<class 'dict'>


<class 'set'>
{'dancing', 1, 2, 3, 5, 8, 9, 55, 'acting'}
------------------------------------------
'''

