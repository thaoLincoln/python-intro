# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:54:09 2019

@author: thaol
"""

import sys
 
user_input = list(input('Please input the value in binary '))
bad_chars = [i for i in user_input if i !='0' and i !='1']
if len(bad_chars) != 0:
    print('Input value is not valid')
    sys.exit()

#arr1 = list(input('Please input the value in binary '))
arr2 = list(map(int,user_input)) 
origin_input = ''.join(user_input)

ex = 1
b = 0
for i in range (0, len(arr2),1):
    b += arr2[len(arr2)-1-i]*ex
    ex *= 2
    
print(b)    

check_value = int(origin_input,2)
if b == check_value:
    print('True')
