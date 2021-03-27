# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:53:07 2021

@author: Sai
"""

#######1.1 Write a Python Program to implement your own myreduce() function which works exactly 
  ########like Python's built-in function reduce()####



def myreduce(num):
    num_list=list(range(1,number+1))
    sum_of_elements=0
    
    for i in num_list:
        sum_of_elements+=i
        
    return num_list,sum_of_elements

#Input 
number=int(input("Please insert the number :"))

output_value=myreduce(number)

#Output
print("Output:")
print("List of First n Natural numbers are:",output_value[0])
print("Sum of List elements are :",output_value[1])


#######1.2 Write a Python program to implement your own myfilter() function which works exactly 
########like Python's built-in function filter()

number=int(input("Please insert the number: "))

num_list=list(range(1,number+1))

num_even_list=list(filter(lambda x: x%2==0,list(filter(lambda x: x%5==0 ,num_list))))
num_odd_list= list(filter(lambda x: x%2!=0,list(filter(lambda x: x%5==0 ,num_list))))

print("List of numbers:",num_list)
print("List of Even number and also which are multiples of 5 are:",num_even_list)
print("List of Odd numbers and also which are multiples of 5 are:",num_odd_list)

#########Implement List comprehensions to produce the following lists.

#####['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']

word1=list('xyz')
word2=[x*n for x in word1 for n in range(1,5) ]
print(word2)

#####['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz'] 

word1=list('xyz')
word3=[x*n for n in range(1,5) for x in word1 ]
print(word3)

######[[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6], 

number=[2,3,4]
resultnumber1=[[x+n] for x in number for n in range(0,3)]
print(resultnumber1)

########[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]

number2=[2,3,4,5]
resultnumber3=[[x+n for n in range(0,4)] for x in number2 ]
print(resultnumber3)

####[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)

number4=[1,2,3]
resultnumber5= [(b,a) for a in number4 for b in number4]
print(resultnumber5)














