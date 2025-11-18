# #access both key and value using items() from dict.
# d={"name":"bharath","age":25,"rollno":103}
# for i,j in d.items():  # using items() because it gives tuple format for all in dictionary
#     print(i,j)

# #python program to calculate the length of string.
# t= "subscribe to bharath channel"
# print(len(t))

# def string_lenth(str1):
#     count=0
#     for char in str1:
#         count+=1  #count=1+count
#     return count
# print(string_lenth(t))

# d= "bharath"
# def string_length(str):
#     count=0
#     for char in str:
#         count+=1
#     return count
# print(string_length(d))

# # python functions that accepts a string and calculate the number of upper case letters and lower case letters.
# def string(input):
#     d={'Upper_case':0,'Lower_case':0}
#     for i in input:
#         if i.isupper():
#             d['Upper_case']+=1
#         elif i.islower():
#             d['Lower_case']+=1
#         else:
#             pass
#     print("Upper case letters:",d["Upper_case"])
#     print("Lower case letters:",d["Lower_case"])
# string("Bharath")


# example:
# def string(str):
#     d={'upper_case':0,'lower_case':0}
#     for i in str:
#         if i.isupper():
#             d['upper_case']+=1
#         elif i.islower():
#             d['lower_case']+=1
#         else:
#             pass
#     print("upper case letters:",d['upper_case'])
#     print("lower case letters:",d['lower_case'])
# string("Bharath Is An Engineer")
    
# # check if the first and last number of a list is the same or not.
# numbers_x=[10,20,10,30,40,12]
# def first_last(numbers_x):
#     first=numbers_x[0]
#     last=numbers_x[2]
#     if first==last:
#         return True
#     else:
#         return False
# print(first_last(numbers_x))

# #python program to check if a key is already present in a dictionary
# # example : using in keyword
# dict = { "name":"bharath","age":23}
# if "rollno" in dict:
#     print ('pesent')
# else:
#     print('absent')

# # count the occurances of each word in a given sentence
# def word_count(str):
#     counts=dict()
#     words=str.split()
#     for word in str:
#         if word in counts:
#             counts[word]+=1
#         else:
#             counts[word]=1
#     return counts
# print(word_count('the quick brown fox jumps over the lazy dog'))    

# python : create a list of empty dictionaries
#[{},{},{},{}]

# print ([{} for _ in range(10)])

# #another method:
# s=10
# d=([] for _ in range(s))
# print(d)

# print ([[] for _ in range(10)])

# # python :extend  a list without append
# a= [1,2,3,4,5]
# b= [3,4,7,9]
# a[:0]=b
# print(a)

# # another method:
# a= [1,2,3]
# b=[6,7,8]
# a.append(b)
# print(a)



# find the largest number among the three input numbers
# a=[1,2,3,4,5,6]
# print(max(a))

# num1=float(input("enter the number :"))
# num2=float(input("enter the number :"))
# num3=float(input("enter the number :"))
# if (num1>=num2) and (num1>=num3):
#     largest=num1
# elif (num2>=num1) and (num2>=num3):
#     largest=num2
# else:
#     largest=num3
# print("largest number is:",largest)

# # python program to check if a number is positive, negative or 0.
# n=int(input("enter the niumber:"))
# if n>0:
#     print("positive number")
# elif n==0:
#     print("the number is zero")
# else:
#     print("the number is negative")

'''check if the number is an armstrong number or not 
without using power function'''
# n = int(input("enter the number:"))
# s=n
# b=len(str(n))
# print(b)

# n = int(input("enter the number:"))
# s=n
# b=len(str(n))
# sum1=0
# while n!=0: # 153
#     r=n%10  #153%10=3
#     sum1=sum1+(r**b)  # 3*3=27 5**3=125 1**3=1
#     n=n//10 #15
# if s==sum1:
#     print("armstrong number")
# else:
#     print("not a armstrong number")
 
# def even(num):
#     if num%2==0:
#         return True
#     else:
#         return False
    
# def odd(num):
#     if num%2!=0:
#         return True
#     else:
#         return False
# a= int(input("enter the digit:"))

# if even(a):
#     print(f"{a} is even")
# elif odd(a):
#     print(f"{a} is odd")

# # check if the input number is odd or even.
# # A number is even if division by 2 gives a remainder of 0.
# # if the remainder is 1, it is an odd number. 
# num = int(input("enter the digit:"))
# if num%2==0:
#     print("the number is even")
# else:
#     print("the number is odd")

# # python program to get a substring of a string
# # using string slicing.
# list = "bharath is learning python"
# print (list[0:11])

# # python program to get the last element of the list
# # using negative indexing
# list="bharath"
# print(list[-1])

# # python: add two given lists using map and lambda 
# list1 = [1,2,3]
# list2=[4,5,6]
# print("original list")
# print(list1)
# print(list2)
# result=map(lambda x,y:x+y,list1,list2)
# print("result")
# print (list(result))

# # python program to add two matrices using nested loop
# x=[[2,3,4],
#    [4,6,8],
#    [3,4,7]]

# y=[[4,6,9],
#    [2,6,0],
#    [4,5,8]]

# result=[[0,0,0],
#         [0,0,0],
#         [0,0,0]]

# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[i][j]=x[i][j]+y[i][j]
# for r in result:
#     print(r)

# write a python program to detect the number of local variables declared in a function.
# local variable: where we use inside the function.
# global variable: where we use outside the function.

#local variable example
# def bharath():
#     x=2
#     y=5
#     s="bharath"
#     d=2.8
# print(bharath.__code__.co_nlocals)

# # global variable example.
# c=2 # global
# def bharath():
#     x=2
#     y=5 # local
#     s="bharath"
#     d=2.8
# print(bharath.__code__.co_nlocals)

# python program to compute all the permutations of the string.
# run unr rnu nru

# # def get_permutation(string):
# rows = int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(rows-i):
#         print("*",end="")
#     print()

# rows = int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(rows-i): 
#         print("*",end="")
#     print()

# write a numpy program to generate random integers between 1 and 300.

# import random
# x=random.randint(1,100)
# print(x)

# import random
# for i in range(10):
#     print(random.randint(1,100))

# import random
# def random_number():
#     return[(random.randint(1,100)) for _ in range(10)]
# result =random_number()
# print(result)

# import numpy as np
# x=np.random.randint(low=1,high=100)
# print(x)

# # program to print half pyramid using *
# rows=4
# for i in range(rows):
#     for j in range(rows-i):
#         print("*",end="")
#     print()

# rows=4
# for i in range(rows):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# rows=4
# for i in range(rows):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(rows-i):
#         print("*",end=" ")
#     print()

# # python program to remove punctuation from a string.
# import string
# punctuations = "''!#@$%^&*()_+"
# mystr=input("enter the string:")
# new_str=""
# for c in mystr:
#     if c not in punctuations:
#         new_str+=c
# print(new_str)

# # python program to reverse a number
# txt = "123456"
# result =txt[::-1]
# print(result)

# def function(a,b):
#     return(a+b)
# print (function(4,6))

# class Student:
#     def bharath(self):
#         print("this is class")
#         a=8
#         b=9
#         print(a+b)
# obj=Student()
# obj.bharath()

# num = [1,2,3,4,5,6,7,8,9]
# for i in num:
#     if i%2==0:
#         print(i)

# num =int(input("enter the number"))
# factorial=1
# if num<0:
#     print("factorial does not exist")
# elif num==0:
#     print("the factorial is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print("the factorial of num is",factorial)

# # python program to count the vowel in a given string.
# s=str(input("enter  a string:"))
# vowels ="aeiouAEIOU"
# count=0
# for char in s:
#     if char in vowels:
#         count+=1
# print("total vowels are",count)

# num=20
# while num<29:
#     print(num)
#     num+=1

# for i in range(10,20):
#     print(i)

# for i in range(0,10):
#     if i==6:
#         break
#     print(i)

# for i in range(11,20):
#     if i==13:
#         continue
#     print(i)

# age = 12
# if age>18:
#     print("adult")
# elif age==18:
#     print("become adult")
# else:
#     print("minor")

# a=[1,2,3,4,5]
# a.append((2))
# print(a)

# class Person:
#     def display(self):
#         print("this is class")
#         a=8
#         b=9
#         print(a+b)
# obj=Person()
# obj.display()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def greet(self):
#         print("my name is",self.name)
#         print('my age is',self.age)
# obj=Person('bharath',24)
# obj.greet()






