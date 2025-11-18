#File handling: reading, writing,deleting, creating, and manipulating of a file is called file handling.

'''modes:
read
write
append
r+ read write
w+ write read
'''


'''
open

read/write

close()
'''

# s= open('demo.txt',mode='r')
# print(s.read())
# s.close()

'''Check if a number is prime ─ develop a function to determine primality''' 
# def is_prime(num):
#     if num>1:
#         for i in range(2,num):
#             if (num%i)==0:
#                 return (num,"it is not a prime number")
#             else:
#                 return (num,"it is a prime number")
# a=int(input("enter the number:"))
# result=is_prime(a)
# print(result)
            
'''Reverse a string — input a string and output it reversed '''
# def reversed_string(input):
#     return (input[::-1])
# a= reversed_string('bharath')
# print("reversed string is :",a)


'''Find the largest element in a list — write your own logic without using max() .'''
# list=[1,2,3,4,5,6,7,8,9]
# a=max(list)
# print(a)

# list=[1,2,3,4,5,6,7,8,9]
# if not list:
#     print("list is empty")
# else:
#     largest=list[0]
#     for num in list[1:]:
#         if num>largest:
#             largest=num

#     print("largest is :",largest)


'''Even or odd — check parity of a number.'''
# number=int(input("enter the number:"))
# if number%2==0:
#     print("it is even number")
# else:
#     print("it is odd number")

# num1=int(input("enter the number:"))
# num2=int(input("enter the number:"))
# total=num1+num2
# print("the sum is:",total)

'''Maximum of three numbers — find largest among three inputs.'''
# num1=int(input("enter the number:"))
# num2=int(input("enter the number:"))
# num3=int(input("enter the number"))
# maximum=max(num1,num2,num3)
# print("the maximum number is:",maximum)

'''Calculate factorial — iterative or recursive approach '''
# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print("factorial cannot be zero")
# elif num==0:
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print("factorial of the number is",factorial)



'''Count vowels in a string — tally vowels in user input.''' 
# a=str(input("enter the string:"))
# vowels="aeiouAEIOU"
# count=0
# for char in a:
#     if char in vowels:
#         count+=1
# print("the total vowel is:",count)

'''Check palindrome number/string — e.g., “121” or “radar”.'''
# a=input("enter the string:")
# if a==a[::-1]:
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")

'''Generate Fibonacci sequence up to n terms — iterative/generator methods.'''
# def fib(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return (fib(n-1)+fib(n-2))
# print(fib(8))

'''arbitary arguments'''
# def sum_all(*args):
#     print(args)
#     return sum(args)
# sum_all(1,2,3,4)

'''arbitary keyword arguments '''
# def print_info(**kwargs):
#     print(kwargs)
# print_info(name='bharath',age=34)

'''positional arguments'''
# def greet(name,age):
#     print(f"hello {name},you are {age} years old")
# greet("bhatath",30)

'''keyword arguments'''
# def greet(age , name):
#     return("this  is the details")
# greet(age=30,name='bharath') 

# def demo(**args):
#     print(args)
# demo (name='bharath')

# def demo2(**args):
#     print(args)
# demo2(name='bharath',age=34) 

# def function(a,b):
#     return a+b
# print(function(2,9))

# def func(args):
#     return args
# print(func(args=['bharath',2,3,4,5]))

# def mask_input():
#     user_input = input("Enter your number: ")
#     masked = '*' * (len(user_input) - 4) + user_input[-4:]
#     print("Masked output:", masked)

# mask_input()

# a=[1,2,3,4,5,6,7,8,9]
# for i in a:
#     if i<=6:
#         print("*",end="")
#     else:
#         print(i,end="")

# number=int(input("enter the number:"))
# for i in str(number):
#     if int(i)<=6:
#         print("*",end="")
#     else:
#         print(i,end="")

# x=[1,2,3,4,5,6,7,8,9]
# a=[i for i in range (10) if i%2==0]
# print(a)

# a=[i for i in range (10) if i%2==0]
# print(a)

'''List reversal — reverse a list without slicing.'''
# list=['bharath',2,3,4,5,6]
# a=(list[::-1])
# print(a)

# Find second largest number — handle duplicates.
# list =[12,23,45,34,56,34,56,78,90]
# result=(list.sort(reverse=True))
# print(list[1])

# list=[12,23,24,45,56,46,43,42]
# result=(list.sort)
# print(list[::-1])

# list=[1,2,3,4,5,6,7,8,9]
# print(list[5:])

# lists=[12,1,3,4,45,67,78,68,65,64,53]
# lists.sort()
# print(lists)

# Remove duplicates from a list.
# lists=[1,2,2,3,3,4,4,5,5,6,7,8,9]
# a=(list(set(lists)))
# print(a)

# Count frequency of elements in a list.
# list=[1,2,2,3,3,4,4,4,5,5,5,6,6,7,7,8,8,9,9,9,9,8]
# frequency={}
# for items in list:
#     if items in frequency:
#         frequency[items]+=1
#     else:
#         frequency[items]=1
# print(frequency)

# Merge two lists and remove duplicates.
# list1=[1,2,3,4,5,6,7,8]
# list2=[6,7,8,9,10]
# merged_list=(list1+list2)
# print(set(merged_list))

# Check if two strings are anagrams.
# Compute LCM of two numbers — can use math.gcd 

'''Remove vowels from a string — custom function '''
# list='ravi'
# vowels='aeiouAEIOU'
# result="" 
# for char in list:
#     if char not in vowels:
#         result+=char
# print(f"the number of lists are:",list)
# print(f"the removed vowels from string are:",result)


'''Reverse a list with slicing and manual.'''
# list='bharath'
# a=list[::-1]
# print(a)

'''Sort a list of tuples by second element — via sorted() + lambda'''
# list=((1,2),(2,3),(3,4))
# result=(sorted(list,key=lambda x:x[1]))
# print("the second list of tuples are:",list)
# print(f"sorted lists",result)

# list=[(1,4),(3,1),(5,2),(2,6),(5,7),(9,8)]
# sorted_list=sorted(list,key=lambda x:x[1])
# print(f"original list is:",list)
# print(f"sorted list of tuples:",sorted_list)

# list=[1,2,3,4,4,4,5,5,6,7,8,9,5,8,9,12,11,34,35,67,78,87,65]
# # list.sort()
# # print(list)
# list.sort()
# print(set(list))

# s=lambda x:x*2
# print(s(4))

# dict1={'name':'bharath'}
# dict2={'age':24}
# dict1.update(dict2)
# print(dict1)

# list=[1,2,3,4,5,6,78]
# print(list[4])

# a=['bharath','ravi','raju']
# print(a[2])

# a=[1,2,3,4,5,6,7,8,9]
# result=a[6]
# print(result)


