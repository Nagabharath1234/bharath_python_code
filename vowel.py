
# python program to count the vowel in a given string.
# s=str(input("enter  a string:"))
# vowels ="aeiouAEIOU"
# count=0
# for char in s:
#     if char in vowels:
#         count+=1
# print("total vowels are",count)

# def decorator(func):
#     def wrapper():
#         print("this is before execution")
#         func()
#         print("this is after execution")
#     return wrapper()
# @decorator
# def function():
#     print("Hello!")
# function

# numbers=[]
# names=[]
# list=['bharath',102,'ravi',103,'raju',104]
# for i in list:
#     if type(i)==int:
#         numbers.append(i)
#     elif type(i)==str:
#         names.append(i)
# print(f"separation of numbers",numbers)
# print(f"separation of names",names)


# list=['bharath','sai','ashok','anand']
# name='bharath'
# if name in list:
#     print(f"yes present in the list")
# else:
#     print(f"no name in the list")

# def generate(n):
#     count=1
#     while count<n:
#         yield count
#         count+=1        
# a=generate(4)
# print(next(a))
# print(next(a))

# fruits=['apple','banana','cherry']
# a=iter(fruits)
# print(next(a))
# print(next(a))

# def decorator(func):
#     def wrapper():
#         print("it is before execution")
#         func()
#         print("it is after execcution")
#     return wrapper()
# @decorator
# def function():
#     print("hello!")
# function

# class Student:
#     def __init__(self,name,age,pages):
#         self.name=name
#         self.age=age
#         self.pages=pages
#         print("this is student details")
#     def __str__(self):
#         return(f"my name is {self.name} and my age is {self.age}")
#     def __len__(self):
#         return(self.pages)
# obj=Student('bharath',24,300)
# print(obj)
# print(len(obj))

# def greet(*a):
#     return a
# res=greet(1,2,3,4)
# print(res)

# def greet(**a):
#     return a
# res=greet(name='bharath',age=24)
# print(res)

# try:
#     10/2
#     print("yes it is correct")
# except ZeroDivisionError:
#     print({"error":"zero division error"})
# finally:
#     print("always runs")

# def greet(a,b):
#     return a+b
# res=greet(4,9)
# print(res)

# str="bharath"
# print(str[:3].upper()+str[3:])

# str="anand"
# print(str.capitalize())

# str="bharath learning python"
# print(str.title())

# str="nagbharth"
# print(str[1:9:2])

# str="bharath"
# print(str.swapcase())

# str="sunder"
# print(str.split())

# str="bharath"
# res=''.join(c.upper() if i%2==0 else c.lower() for i,c in enumerate(str))
# print(res)
             
# list=[1,2,2,3,3,4,4,4,5,5,5,6,6]
# freq={}
# for i in list:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(f"the frequency of the list is",freq)

# str="bharath"
# print(str.strip())

# str="naga bharath"
# print (str.replace('naga','balaji'))

# str="bharath"
# print(list(str))

# list=[1,2,3,4,5,6]
# print(str(list))

# str="bharath"
# print(str.upper())

# str="bharath"
# res=str[::-1]
# print(res)

# a=input("enter the words:")
# if (a==a[::-1]):
#     print("it is palindrome")
# else:
#     print("it is not a palindrome")

# num=int(input("enter the number:"))
# if num%2==0:
#     print("even num")
# else:
#     print("odd num")

# str="bharath"
# print(len(str)//2)


# class Student:
#     def __init__(self,a,b):
#         self.__a=a
#         self._b=b
#         print("this is student class")
# class Person(Student):
#     def display(self):
#         print(self._b)
       
# obj=Person(3,5)
# obj.display()

# a="bharath"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)

# a="bharath"
# s=[]
# for i,c in enumerate(a):
#     if i%2==0:
#         s.append (c.lower())
#     else:
#         s.append (c.upper())
# print("".join(s))

# list=[1,2,3,4,5,'bharath','hari',45]
# names=[]
# numbers=[]
# for i in list:
#     if type(i)==str:
#         names.append(i)
#     if type(i)==int:
#         numbers.append(i)
# print(f"separation of names{names} and separation of numbers{numbers}")

# list=[1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,66,6,7,7,7,8,8,8]
# freq={}
# for i in list:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(f"frequency of the list is",freq)

# num=int(input("enter the number:"))
# for i in range(1,11):
#     print(f"{num}x{i}={num*i}")

# def decorator(func):
#     def wrapper():
#         print("it is before execution")
#         func()
#         print("it is after execution")
#     return wrapper()
# @decorator
# def function():
#     print("Hello!")
# function

# class Student:
#     def greet(self):
#         print("it is student class")
# class Person(Student):
#     def greet1(self):
#         print("it is person class")
# obj=Person()
# obj.greet1()
# obj.greet()

# s=["apple","orange","banana","cherry"]
# res=sorted(list(s))
# print(res)

# def generator(n):
#     count=0
#     while count<n:
#         yield count
#         count+=1
# res=generator(6)
# print(next(res))
# print(next(res))

# s=["apple","banana","cherry","mango"]
# res=iter(s)
# print(next(res))
# print(next(res))

# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print(f"factorial cannot be negative")
# elif num==0:
#     print(f"factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print(f"factorial of the number is",factorial)

# num=int(input("enter the number:"))
# for i in range(2,num):
#     if num%i==0:
#         print("it is not a prime num")
#         break
# else:
#     print(f"it is prime num")

# a="bharath"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)

# a="bharath"
# print(a[::-1])

# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print(f"factorial cannot be negative")
# elif num==0:
#     print(f"factorial of 0 is 1")
# else:
#     for i in range (1,num+1):
#         factorial=factorial*i
# print(f"factorial of the number is",factorial)

# num=int(input("enter the number:"))
# for i in range(2,num):
#     if num%i==0:
#         print(f"it is not a prime num")
#         break
# else:
#     print(f"it is a prime num")

# num=int(input("enter the number:"))
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")

# def decorator (func):
#     def wrapper():
#         print("it is before execution")
#         func()
#         print("it is after execution")
#     return wrapper()
# @decorator
# def function():
#     print("Hello!")
# function

# def generator(n):
#     count=0
#     while count<n:
#         yield count
#         count=+1
# res=generator(6)
# print(next(res))
# print(next(res))

# fruits=["apple","cherry","banana","orange"]
# res=iter(fruits)
# print(next(res))
# print(next(res))

# num=int(input("enter the number:"))
# if num%2==0:
#     print(f"even num")
# else:
#     print(f"odd num")

# list=[1,2,3,4,5,6,7,8]
# for i in list:
#     if i%2==0:
#         print(i)      

# s=[1,2,3,4,5,6,7,8]
# print(list(map(lambda x:x*2,s)))

# s=[1,2,3,4,5,6,7,8,9,0]
# print(list(filter(lambda x:x%2==0,s)))

# s=[1,2,3,4,5,6,7,8]
# res=[x for x in s if x%2==0 ]
# print(res)

# t=(2,3,4,5,6,89,78,56,45)
# res=(tuple(x*2 for x in t))
# print(res)

# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print(f"the factorial cannot be negative")
# elif num==0:
#     print(f"the factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
# print(f"the factorial of the number is",factorial)

# num=int(input("enter the number:"))
# for i in range(2,num):
#     if num%i==0:
#         print(f"it is not a prime num")
#         break
# else:
#     print(f"it is a prime num")

# num=int(input("enter the number:"))
# for i in range(1,11):
#     print(f"{num} X {i} ={num*i}")

# a="bharath"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)

# a="bharath"
# print(a[::-1])

# list=[1,2,3,4,5,6,7,8,9,10]
# for i in list:
#     if i%2==0:
#         print(i)