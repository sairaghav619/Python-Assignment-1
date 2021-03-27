# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
for i in range(2000,3201):
    if i%7 == 0 and i%5!=0:
        print(i,end=',')
print("\b")



fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print (lname + " " + fname)


pi = 3.1415926535897931
diameter=12
r= diameter/2.0
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is:',V)


