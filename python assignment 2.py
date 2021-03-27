# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:33:46 2021

@author: Sai
"""

n = 5
for i in range(n):
    print('*'*(i+1))
for j in range(n):
    print('*'*(n-1-j))
    
    
n = input("Enter The Name : ")
n = n[ ::-1]
print("Reverse of the given name: ", n)


