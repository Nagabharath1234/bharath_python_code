'''Write a function to reverse a given string.
Example: "hello" → "olleh"'''

# txt="hello"
# print (txt[::-1])

# def reversed(input):
#     return (input==input[::-1])
# result=reversed("hello")
# print(result)

# a=input("enter the word :")
# reversed_a=""
# if a:
#     for char in a:
#         reversed_a=char+reversed_a
#     print("it is reversed",reversed_a)
# else:
#     print("no input provided",reversed_a)

# def reversed():
#     user_input=input("enter the word:")
#     reversed_input=user_input[::-1]
#     print('reversed word',reversed_input)
# reversed()

# def reversed():
#     a=input("enter the word:")
#     result=a[::-1]
#     print('reversed word',result)
# reversed()
    
'''Check if a Number is Prime
Write a function to check if a number is prime.'''
# num=int(input("enter any number:"))
# for i in range(2,num):
#     if (num%2)==0:
#             print("it is not a prime num")
#             break
# else:
#     print("this is prime num")


# def prime_number():
#     num=int(input("enter any number:"))
#     if (num%2)==0:
#         print('it is not a prime number')
#     else:
#         print("it is prime")
# prime_number()

'''Calculate the Factorial of a Number
Write a function to calculate the factorial of a number.'''
# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print("factorial cannot be negative")
# elif num==0:
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print("factorial of the number is:",factorial)

# def factorial(n): 
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# result=factorial(5)
# print(f"the factorial of a number is:{result}")

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# num=int(input("enter the number:"))
# print(f"the factorial of a number is:{result}")

'''Check if a String is a Palindrome
Write a function to check if a string is a palindrome.'''
# a=input("enter the word:")
# if (a==a[::-1]):
#     print("true it is a palindrome")
# else:
#     print("false it is not a palindrome")

# def is_palindrome(input):
#     return (input==input[::-1])
# result=is_palindrome("bharath")
# print(result)

# def is_palindrome(n):
#     if (n==n[::-1]):
#         print("it is a palindrome")
#     else:
#         print("it is not a palindrome")
# result=input("enter the word:")
# is_palindrome(result)


'''Find the Largest Element in a List
# Write a function to find the largest element in a list.'''
# list = [1,2,3,4,5,6]
# print(max(list))

# def largest(list):
#     return max(list)
# result=largest([1,2,3,4,5,6,7,8,9])
# print(result)

''' find the second largest number'''
# numbers=[1,2,3,4,45,99,101]
# numbers.sort(reverse=True)
# print(numbers[1])  

'''write a function of basic clculator '''     
# def calculator(a,b,operator):
#     if operator=="+":
#         return a+b
#     elif operator=="-":
#         return a-b
#     elif operator=="*":
#         return a*b
#     elif operator=="/":
#         return a/b
#     else:
#         print("invalid")
# result=calculator(3,5,"+")
# print(result)

# class Student:
#     def display(self):
#         print("this is class")
#         a=9
#         b=8
#         print(a+b)
# obj=Student()
# obj.display()

# def calculator(a,b,operator):
#     if operator=="+":
#         return(a+b)
#     elif operator=="-":
#         return (a-b)
#     elif operator=="*":
#         return (a*b)
#     elif operator=="/":
#         return(a/b)
#     else:
#         print("invalid")
# res=calculator(2,3,"*")
# print(res)

# class Student:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def display(self):
#         print(self.a+self.b)
# obj=Student(3,5)
# obj.display()

# class Student:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def display(self):
#         if type(self.a)==int and type(self.b)==int:
#             print(self.a+self.b)
#         else:
#             print("provide valid values")
# obj=Student('9',8)
# obj.display()

# class Student:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def display(self):
#         print("my name is",self.a)
#         print("my age is",self.b)
# obj=Student('bharath',24)
# obj.display()

# def is_function(a,b):
#     return a+b
# result=is_function(3,6)
# print(result)
          
# class Person:
#     def func(self):
#         print("this is class a")
# class Student(Person):
#     def func(self):
#         print("this is class b")
#         super().func()
# obj=Student()
# obj.func()

# class A:
#     def func(self,a,b):
#         return a+b
#     def func(self,a,b,c=8):
#         return a+b+c
# obj=A()
# print(obj.func(3,4))

# class Student:
#     def __init__(self,a,b):
#         self.__a=a
#         self._b=b
#     def display(self):
#         print(self.__a)
#         print(self._b)
# obj=Student(3,5)
# obj.display()

# for i in range(0,10):
#     print(i)

# n=5
# while n<10:
#     print(n)
#     n+=1

# for i in (1,9):
    
#     if i==5:
#         break
        
#         print(i)

# for i in ('python'):
#     if i=='o':
#         break
#     print(i) 

# for i in 'python':
#     if i=='t':
#         continue
#     print(i)
 
# age=12
# if age >18:
#     print("right to vote")
# elif age==18:
#     print("just completed minor age")
# else:
#     print("minor not eligible for vote")

# rows=int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# rows=int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(rows-i):
#         print("*",end=" ")
#     print()

# rows=int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(rows-i):
#         print("*",end=" ")
#     print()

''' print triangle method'''
# rows=int(input("enter the number of rows:"))
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# num=int(input("enter the number:"))
# for i in range(2,num):
#     if (num%i)==0:
#         print("it is not a prime number")
#         break
# else:
#     print("it is a prime number")


# a=input("enter the word:")
# print (a[0:4])

# num=int(input("enter the number:"))
# if (num%2)==0:
#     print("it is  not prime ")
#     print("the value is:",num*2)
# else:
#     print("it is prime")
#     print("the value is:",num*3)
    


'''Write a Python program that prints "Hello, World!" to the console.'''
# txt="Hello World!"
# print(txt)

''' Determine if a given number is even or odd.'''
# numbers=int(input("enter the number:"))
# if numbers%2==0:
#     print("even number")
# else:
#     print("odd number")

'''Write a function that returns the sum of two numbers.'''
# def sum(a,b):
#     return a-b
# result=sum(3,6)
# print(result)

'''Find the largest among three numbers provided by the user.'''
# num1=int(input("enter the number:"))
# num2=int(input("enter the number"))
# num3=int(input("enter the number:"))
# if num1>=num2 and num1>=num3:
#     largest=num1
# elif num2>=num1 and num2>=num3:
#     largest=num2
# else:
#     largest=num3
# print(f"largest number is :{largest}")

'''Compute the factorial of a given number using a loop.'''
# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print("factorial cannot be negative")
# elif num==0:
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print("factorial of the number is:",factorial)

'''Check if a given string is a palindrome.'''
# a=input("enter the word:")
# if a==a[::-1]:
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")

'''Reverse a list without using built-in functions.'''
# list=['b','h','a','r','a','t','h']
# result=list[::-1]
# print(result)

'''Count the number of vowels in a given string.'''
# str='bharath'
# vowels="aeiouAEIOU"
# count=0
# for char in str:
#     if char in vowels:
#         count=count+1
# print(f"number of vowels are:{count}")

'''Implement a basic calculator that can perform addition, subtraction, multiplication, and division.'''
# def calculator(a,b,operator):
#     if operator=="+":
#         return a+b
#     elif operator=="-":
#         return a-b
#     elif operator=="*":
#         return a*b
#     elif operator=="/":
#         return a/b
#     else:
#         return ("invalid")
# result=calculator(3,4,"*")
# print(result)

'''Determine if a number is prime.'''
# num=int(input("enter the number:"))

#     for i in range(2,num):
#         if (i%2)==0:
#             print("it is not a prime number")
#             break
#         else:
#             print("tihis is prime num")


#'''lambda function is a small and ananymous function no def needed in lambda function'''
# add = lambda x,y: x+y
# print(add(2,3))

# add = lambda x, y: x + y
# print(add(2, 3)) 

'''Generate the Fibonacci sequence up to a specified number of terms.'''
# def fibonacci(input):
#    if input<=0:
#       return []
#    if input==1:
#       return[0]
#    if input==2:
#       return[0,1]
#    seq=fibonacci(input-1)
#    seq.append(seq[-1]+seq[-2])
#    return seq
# result=fibonacci(8)
# print(result)
     
# s=lambda x,y : x+y
# print(s(6,8))

# s=[1,2,3,4,5,6,7,8,9]
# res=list(map (lambda x :x*x,s))
# print(res)

s=[1,2,3,4,5,6,7,8,9]
res=list(filter(lambda x:x%2==0,s))
print(res)

# class BankAccount:
#     def __init__(self, account_holder, bank_balance=100.0):
#         self.account_holder = account_holder
#         self.balance = bank_balance  

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f"Withdraw ${amount:.2f}. New balance: ${self.balance:.2f}")

#     def check_balance(self):
#         print(f"Current balance: ${self.balance:.2f}")
#         return self.balance

# # Usage
# obj = BankAccount('Bharath', 1000.0)
# obj.deposit(50.0)
# obj.withdraw(100.0)
# obj.check_balance()

# class Bankbalance:
#     def __init__(self,accountholder,balance):
#         self.accountholder=accountholder
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance+=amount
#         print(f"deposited ${amount:.2f}.new balance:${self.balance:{amount:.2f}}")

#     def withdraw(self,amount):
#         self.balance-=amount
#         print(f"withdraw ${amount:.2f}.new balance:${self.balance:{amount:.2f}}")

#     def checkbalance(self):
#         print(f"current balance ${self.balance:.2f}")
#         return self.balance


# obj= Bankbalance('bharath',100)
# obj.deposit(50)
# obj.withdraw(30)
# obj.checkbalance()

# class BankBalance:
#     def __init__(self, accountholder, balance):
#         self.accountholder = accountholder
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f"Withdraw ${amount:.2f}. New balance: ${self.balance:.2f}")

#     def check_balance(self):
#         print(f"Current balance: ${self.balance:.2f}")
#         return self.balance

# # Example usage
# obj = BankBalance('Bharath', 100)
# obj.deposit(50)
# obj.withdraw(30)
# obj.check_balance()

# '''Determine if a number is prime.'''
# def is_prime(num):
#     if num<=1:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%2==0:
#             return False
#         return True
# result = is_prime(6)
# print(result)
  
# a="hello world"
# print(a.upper())

# a="HELLO WORLD"
# print(a.lower())

# a="bharath learning python"
# print(a.title())

# str="bharath"
# print(str.upper())

# str="BHARATH"
# print(str.lower())

# str="bharath"
# print(str.capitalize())

# str= "bharath learning python"
# print(str.title())

# str="BHarAtH"
# print(str.lower())

# str="bharath"
# print(str[:3].upper() + str[3:])

# str="bharath learning python"
# print(str.split())

# str="bharath"
# print(str.split())

# str="BHARATH"
# print(str.swapcase())

# str="Hello World"
# print(str.removeprefix("Hello"))

# str="naga bharath"
# print(str.removesuffix("bharath"))

# str="hello world"
# print(str.replace("world","bharath"))

# str="  bharath   "
# print(str.strip())

# str="****bharath****"
# print(str.strip("*"))

# str="banana"
# print(str.replace("a","o"))

# str="apple"
# print(str.replace("a","i"))

# str="{} scored {} points"
# print(str.format("bharath",100))

# s="resto"
# s+="bar"
# print(s)

# a="hello"
# b="bharath"
# c=a+" "+b
# print(c)

# list=[0,1,2,3,4,5,6,7,8]
# print(sum(list))
# print(len(list))
# print(max(list))
# print(min(list))

# a="bharath"
# print(a.count("a"))

# python = "python language"
# print(python.endswith("l"))
# print(python.startswith("l"))

# python = "python language"
# print(python.index('bharath'))
# print(python.find('bharath'))

# python = "python language"
# print(python.count('g'))

# s=[x for x in range(10)]
# print(s)

# s=[x for x in range(100) if x%5==0]
# print(s)

# s=[x for x in range(20) if x%3==0]
# print(s)

# import random
# choices=("rock", "paper", "scissor")
# user_choice=input("enter rock, paper, scissor:").lower()
# computer_choice= random.choice(choices)
# print(f"your choice:{user_choice}")
# print(f"computer choice:{computer_choice}")
# if user_choice==computer_choice:
#     print("it is a tie")
# elif (
#     (user_choice=='rock' and computer_choice=='scissor')or
#     (user_choice=='scissor' and computer_choice=='paper')or
#     (user_choice=='paper' and computer_choice=='rock')
# ):
#     print("you will win")
# elif user_choice in choices:
#     print("computer will win")
# else:
#     print("enter valid choices")

