''' write a python function that takes a string as input  and returns the string reversed.
additionally make the function count the number of vowels within the input string.'''
# def reversed_string_vowel(input):
#     reversed_string=input[::-1]
#     vowels = "aeiouAEIOU"
#     vowels_count=sum(1 for char in input if char in vowels) 
#     return reversed_string,vowels_count
# result,count = reversed_string_vowel("malyalam ")
# print("reversed:",result)
# print("vowel_count:",count)

'''create a function that takes a list of numbers as input and returns a new list containing only the even numbers 
from the original list.'''
# def list_of_numbers(num):
#     return [num for num in num if num%2==0]
# original_list = [1,2,3,4,5,6,7,8,9]
# new_list =list_of_numbers(original_list)
# print("new_list :",new_list)

'''Create a function that takes a list of names as input and returns a dictionary where the keys are the names 
and the values are the lengths of the names.'''
# def list_of_names(name):
#     return {name:len(name) for name in name}
# name_list=["bharath","ravi","jordan","veera"]
# name_len = list_of_names(name_list)
# print(name_len)

'''Develop a Python program that takes two numbers and an operator (+, -, \*, /) as input and performs the corresponding calculation.
def calculator(a,b,operator):'''
#     if operator == '+':
#         return a+b
#     elif operator == '-':
#         return a-b
#     elif operator == '*':
#         return a*b
#     elif operator == "/":
#         return a/b if b!=0 else "error: division by zero"
#     else:
#         return 'invalid'
# result=calculator(10,5,'+')
# print(f"result",{result})
   
'''Write a Python script that generates a list of 10 random integers between 1 and 100.'''
# import random
# def generate_random_numbers():
#     return[random.randint(1,100) for _ in range(10)]
# random_numbers=generate_random_numbers()
# print(f"random_numbers:{random_numbers}")

'''Define a Python class called "Rectangle" with attributes for width and height, and methods to calculate its area 
and perimeter.'''
# class Rectangle:
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#         def area(self):
#             return self.width * self.height
#         def perimeter(self):
#             return 2*(self.width + self.height)
# rect = Rectangle(5,10)
# print(f"area: {rect.area()}")
# print(f"perimeter: {rect.perimeter()}")

'''Write a Python program that prints a right-angled triangle pattern of stars, where the number of rows is determined 
by user input.'''
# rows = int(input("enter the number of rows:"))
# for i in range(1,rows+1):
#     print("*" * i)

'''Write a Python program that prints an inverted right-angled triangle pattern of stars.'''
# rows =int(input("enter the number of rows:"))
# for i in range(rows,0,-1):
#     print("*"*i)

'''Write a Python program that prints a pattern of numbers, as shown below.'''
# rows = int(input("enter the number of rows:"))
# for i in range(1,rows+1):
#     for j in range (1,i+1):
#         print(j,end=" ")
#     print()

'''Write a Python program that prints the following alphabet pattern.'''
# rows = int(input("enter the numbers of rows: "))
# for i in range(1,rows+1):
#     for j in range(i):
#         print(chr(64+i),end=' ') 
#     print()



'''Create a Python function that calculates the difference between two given dates in days.'''
#from datetime import datetime
# def date_difference(date1,date2):
#     format = "%Y-%m-%d"
#     d1 = datetime.strptime(date1, format)
#     d2 = datetime.strptime(date2, format)
#     return abs ((d2-d1).days)
# days_diff = date_difference("2024-01-01","2024-04-01")
# print(f"days difference: {days_diff}")

'''Write a Python script that reads a text file, counts the number of words in it, and prints the result.'''
# def count_the_number(filename):
#     try:
#         with open(filename,'r') as file:
#             text = file.read()
#             word_count=len(text.split())
#             print(f"number of words : {word_count}")
#     except FileNotFoundError:
#         print("file not Found")
# count_the_number("sample.txt")

''' right angled triangled triangle'''
# rows=int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


'''inverted right angled triangle'''
# rows = int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(rows-i):
#         print("*",end="")
#     print()


''' inverted triangle'''
# rows = int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(rows-i): 
#         print("*",end=" ")
#     print()()

'''  triangle'''
# rows = int(input("enter the number of rows:"))
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(" ",end="")
#     for k in range(i): 
#         print("*",end=" ")
#     print()

