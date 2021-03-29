# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 11:21:32 2021

@author: Raghav
"""
####Write a Python Program(with class concepts) to find the area of the triangle using the below 
#formula.
##area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
###Function to take the length of the sides of triangle from user should be defined in the parent 
##class and function to calculate the area should be defined in subclass.


class sides:
    def __init__(self,a,b,c):
            self.a = float(a)
            self.b = float(b)
            self.c = float(c)
a= int(input("a="))
b= int(input("b="))
c= int(input("c="))
        
class triangle(sides):
    def area(self):
        s=(self.a+self.b+self.c)*0.5
        return float((s * (s - self.a) * (s - self.b) * (s - self.c))) ** 0.5

t=triangle(a,b,c)
print('area of triangle is ', t.area())



##### Write a function filter_long_words() that takes a list of words and an integer n and returns 
###the list of words that are longer than n.

def filter_long_words(t,a):
    words=[]
    for i in t:
        if(len(i)>a):
            words.append(i)
    return words

n=input("Enter words:")
nt=n.split(",")
low=input("Enter Min Length:")
long=filter_long_words(nt,int(low))

print("Words with at least min length:",long)


##### Write a Python program using function concept that maps list of words into a list of integers 
######representing the lengths of the corresponding words

def map_Words_to_Length(List):
    return list(map(len, List))

words=input("Please enter Words : ")
word_list=words.split(",")
#finalwordlist=[x.strip() for x in word_list]
#Words_lengths=map_Words_to_Length(finalwordlist)
Words_lengths=map_Words_to_Length(word_list)
print("Length of Words are :",Words_lengths )

###### Write a Python function which takes a character (i.e. a string of length 1) and returns True if 
#######it is a vowel, False otherwise.
   

def is_vowel(char):
    lvowel = ['a', 'e', 'i', 'o', 'u']
    uvowel=['A','E','I','O','U']
    if (char  in lvowel) or (char in uvowel):
        return True
    return False
char=input("Please enter any character : ")
print("The entered character is", is_vowel(char) )












