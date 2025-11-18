'''decorators in python'''
# def div(a,b):
#     return a/b
# print(div(10,5))


'''generator :- generator is a special type of function that returns an iterator object.
 it returns the yield keyword'''
# def generate_num(limit):
#     for num in range (1,limit+1):
#         yield num
#         sequence = generate_num(5)
#         for value in sequence:
#             print(value)

# def function (num):
#     for i in range(1,num+1):
#         yield num
#         sequence = function(10)
#         for value in sequence:
#             print(value)

# def display(message):
#     return (message)
# @display
# def printer():
#     print("bharath is very smart guy")
# printer()

# def decorator(func):
#     def wrapper():
#         print("before execution of the function")
#         func()
#         print("after execution of the function")
#     return wrapper

# @decorator
# def function():
#     print('hello')

# function()

# def decorator(input):
#     def wrapper():
#         print("this is before function")
#         input()
#         print("this is after function")
#     return wrapper()
# @decorator
# def function():
#     print("hello!")

# def generator(n):
#     count=1
#     while count<n:
#         yield count
#         count+=1
# result=generator(5)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

# fruits=['apple','banana','cherry']
# a=iter(fruits)
# print(next(a))
# print(next(a))

# def decorator(func):
#     def wrapper():
#         print("this is before execution")
#         func()
#         print("this is after execution")
#     return wrapper()
# @decorator
# def function():
#     print("hello")
# function

# dict1={1:'bharath',2:'ravi',3:'ashok'}
# res1=dict1.get(1)
# print(res1)

# for key,value in dict1.items():
#     print(key,value)

# str="hello how are you"
# count={}
# for word in str.split():
#     count [word]=len(word)
# print(count)

# def decorator(func):
#     def wrapper():
#         print("this is before execution")
#         func()
#         print("this is after execution")
#     return wrapper()
# @decorator
# def function():
#     print("hello!")
# function

 
# fruits=['apple','banana','cherry']
# a=iter(fruits)
# print(next(a))
# print(next(a))

# def generate(n):
#     count=1
#     while count<n:
#         yield count
#         count=count+1
# a=generate(3)
# print(next(a))

# def fiction(func):
#     def display():
#         print("this is before execution")
#         func()
#         print("this is after execution")
#     return display()
# @fiction
# def function():
#     print("hello!")
# function

# def display(n):
#     count=0
#     while count<n:
#         yield count
#         count+=1
# var=display(7)
# print(next(var))
# print(next(var))
# print(next(var))

# fruits=['apple','banana','cherry']
# a=iter(fruits)
# print(next(a))
# print(next(a))

# list1=[1,2,3,4]
# list2=[3,4,5,6]
# a=list1+list2
# print(a)

# list=[1,2,3,4,5]
# index=list.index(2)
# list[index]='bharath'
# print(list)

# var=60
# print(var)

# for i in range(0,10):
#     print(i)

# def decorator(func):
#     def display():
#         print("this is before execution")
#         func()
#         print("this is after execution")
#     return display()
# @decorator
# def function():
#     print("hello!")
# function

# fruits=['apple','banana','cherry']
# result=iter(fruits)
# print(next(result))
# print(next(result))

# def generator(n):
#     count=0
#     while count<n:
#         yield count
#         count+=1
# result=generator(8)
# print(next(result))
# print(next(result))

# class Student:
#     def display(self):
#         print("this is class")
#         a=9
#         b=8
#         print(a+b)
# obj=Student()
# obj.display()

# class Person:
#     def display(self,a,b):
#        return a+b
#     def display(self,a,b,c=9):
#         return a+b+c
# obj=Person()
# print(obj.display(3,6))

# class Person:
#     def func(self):
#         print("this is person class")
# class Student(Person):
#     def func(self):
#         print("this is Student class")
#         super().func()
# obj=Student()
# obj.func()

# class Demo:
#     def __init__(self,a,b):
#         self.__a=a
#         self._b=b
# class Demo1(Demo):
#     def output(self):
#         print(self._b)
# obj=Demo1(3,4)
# obj.output()

# def decorator(func):
#     def wrapper():
#         print("this is before execution")
#         func()
#         print("this is After execution")
#     return wrapper()
# @decorator
# def function():
#     print("Hello!")
# function

# list=[1,2,3,4,'naga',4,5,6]
# index=list.index(5)
# list[index]='bharath'
# print(list)

# def generator(n):
#     count=0
#     while count<n:
#         yield count
#         count+=1
# result=generator(8)
# print(next(result))

# list=[1,2,3,4,5,6,7,8,9]
# for i in list:
#     if i%2==0:
#         print(i)

# num=int(input("enter the number"))
# factorial=1
# if num<0:
#     print("the factorial cannot be negative")
# elif num==0:
#     print("the factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print("the factorial of the number is:",factorial)

# num=int(input("enter the number:"))
# for i in range(2,num):
#     if (num%i)==0:
#         print('this is not a prime num')
#         break
# else:
#     print("this is a prime num")

# a=input("enter the word:")
# if a==a[::-1]:
#     print ("it is a palindrome")
# else:
#     print("it is not a palindrome")

# numbers=int(input("enter the number"))
# if numbers%2==0:
#     print("it is even num")
# else:
#     print("it is odd num")

# for i in range(0,10):
#     if i==5:
#         pass
#     print(i)

# s=[x for x in range(10) if x%2==0 ]
# print(s)

# s={x:x*x for x in range(5)}
# print(s)

# a={x%9 for x in range(8)}
# print(a)

# even=(x for x in range (10) if x%2==0)
# print(even)

# s=lambda x,y:x+y
# print(s(4,7))

# numbers=[1,2,3,4,5,6]
# result=map(lambda x:x**x,numbers)
# print(list(result))

# numbers=[1,2,3,4,5,6,7,8,9]
# result=filter(lambda x:x%2==0,numbers)
# print(list(result))

# def function(a,b):
#     return a+b
# result=function(3,4)
# print(result)

# def decorator(func):
#     def wrapper():
#         print("this is before the function")
#         func()
#         print("this is after the function")
#     return wrapper()
# @decorator
# def function():
#     print("Hello!")
# function

# def generate(n):
#     count=0
#     while count<n:
#         count+=1
#         yield count
    
# res=generate(7)
# print(next(res))
# print(next(res))

# fruits=['apple','cherry','banana']
# res=iter(fruits)
# print(next(res))
# print(next(res)) 

# class Student:
#     def demo(self):
#         print("this is student class")
# class Person(Student):
#     def demo1(self):
#         print("this is person class")
# obj=Person()
# obj.demo1()
# obj.demo()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(f"my name is {self.name} and my age is {self.age}")
# class Student(Person):
#     def __init__(self,name,age,salary,department):
#         super().__init__(name,age)
#         self.salary=salary
#         self.department=department
        
#         print(f"my salary is {self.salary} and my dept is {self.department}")
# obj=Student('bharath',24,25000,'cse')

# num=int(input("enter the number:"))
# for i in range(2,num):
#     if (num%i)==0:
#         print(f"it is not a prime number")
#         break
# else:
#     print(f"it is a prime number")

# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print(f"factorial cannot be negative")
# elif num==0:
#     print(f"factorial of 0 is 1")
# else:
#     for i in range(1,1+num):
#         factorial=factorial*i
#     print(f"the factorial of the number is",factorial)

# num=int(input("enter the number:"))
# a,b=0,1
# for i in range(0,num):
#     if i<=1:
#         print(i)
#     else:
#         res=a+b
#         a=b
#         b=res
#         print(res)

# a='bharath'
# res=a[:3].upper()+a[3:]
# print(res)

# num=int(input("enter the number:"))
# a,b=0,1
# for i in range(0,num):
#     if i<=1:
#         print(i)
#     else:
#         res=a+b
#         a=b
#         b=res
#         print(f"the fibonacci of the number is :",res)

# num=int(input("enter the number:"))
# if num%2==0:
#     print("even num")
# else:
#     print("odd num")

# a="bharath"
# res=a[:3].upper()+a[3:]
# print(res)

# str="bharath"
# a=[]
# for i,c in enumerate(str):
#     if i%2==0:
#         a.append(c.lower())
#     else:
#         a.append(c.upper())
# print("".join(a))

# a=[1,2,3,2,2,3,3,4,4,4,5,5,6,6,6,7,7,8,8,9,9]
# res={}
# for i in a:
#     if i in res:
#         res[i]+=1
#     else:
#         res[i]=1
# print(f"the frequency of",res)

# def decorator(func):
#     def wrapper():
#         print(f"this is before execution")
#         func()
#         print(f"this is after execution")
#     return wrapper()
# @decorator
# def function():
#     print("hello!")
# function

# def generator(n):
#     count=0
#     while count<n:
#         yield count
#         count+=1
# res=generator(5)
# print(next(res))
# print(next(res))

# fruits=["apple","orange","banana"]
# res=sorted(fruits)
# print(res)

# age=12
# if age >18:
#     print("ready to vote")
# elif age==18:
#     print("become major")
# else:
#     print("minor")

# num=int(input("enter the number:"))
# for i in range(2,num):
#     if (num%i)==0:
#         print("it is not a prime num")
#         break
# else:
#     print("it is a prime num")

# def prime(n):
#     if n<2:
#         print(f"{n} it is not a prime num")
#         return
#     for i in range(2,n):
#         if (n%i)==0:
#             print(f"{n} it is not a prime num")
#             return
#     else:
#         print(f"{n} it is a prime num")
# res=prime(4)


# def prime(n):
#     if n < 2:
#         print(f"{n} is not a prime number")
#         return
#     for i in range(2, n):
#         if n % i == 0:  # ✅ Correct logic
#             print(f"{n} is not a prime number")
#             return
#     else:
#         print(f"{n} is a prime number")

# res = prime(4)
# print(res)

# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print(f"factorial cannot be negative")
# elif num==0:
#     print(f"fcatorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
# print(f"fatorial of the number is:",factorial)

# str="bharath"
# print(str[::-1])

# a="bharath"
# rev=" "
# for i in a:
#     rev=i+rev
# print(rev)

# list=[1,2,3,4,5,6,7,8,9]
# list.sort
# print(list[-2])

# a="hello"
# s=""
# for i in a:
#     s=i+s
# print(s)

# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# if a>b:
#     print(f"first num is greater")
# elif b>a:
#     print(f"the second number is greater")
# else:
#     print(f"both are equal")

# n=int(input("enter the number"))
# total=0
# for i in range(1,n+1):
#     total=total+i
# print(f"the sum of {n} natural number is:",total)

# a=int(input("enter the number:"))
# for i in range(0,11):
    # print(f"{a} x {i} = {a*i}")

# str="bharath"
# s="aeiouAEIOU"
# count=0
# consonents=0
# for i in str:
#     if i in s:
#         count+=1
#     else:
#         consonents+=1
# print(f"the vowel count is:",count)
# print(f"the consonents are:",consonents)

# a=int(input("enter the number:"))
# if a>0:
#     print(f"positive num")
# elif a==0:
#     print(f"zero num")
# else:
#     print(f"negative num")

# num1=int(input("enter the number:"))
# num2=int(input("enter the number"))
# if num1>num2:
#     print(f"num1 is largest")
# elif num2>num1:
#     print(f"num2 is largest")
# else:
#     print(f"both are equal")

# start=int(input("enter the starting num:"))
# end=int(input("enter the ending num:"))

# print(f"prime numbers between {start} and {end} are:")
# for num in range(start,end+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)

# a="bharath"
# vowels="aeiouAEIOU"
# count=0
# consonents=0
# for i in a:
#     if i in vowels:
#         count+=1
#     else:
#         consonents+=1
# print(f"the count of vowels are:",count)
# print(f"the count of consonents are:",consonents)

# num=int(input("enter the number:"))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

# n=int(input("enter the number:"))
# total=0
# for i in range(1,n+1):
#     total=total+i
# print(f"the sum of {n} natural numbers are:",total)

# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print(f"factorial cannot be negative")
# elif num==0:
#     print(f"factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
# print(f"the factorial of the number is :",factorial)

# a="bharath"
# rev=""
# for i in a:
   
#     rev=i+rev
# print(rev)

# def reverse(input):
#     return (input[::-1])
# s=reverse("bharath")
# print(s)

# s="bharath"
# a=[]
# for i,c in enumerate (s):
#     if i%2==0:
#         a.append(c.lower())
#     else:
#         a.append(c.upper())
# print("".join(a))

# s=[1,2,3,4,5]
# for i in s:
#     if i%2==0:
#         print(i)

# s="bharath"
# a=[]
# for i,c in enumerate (s):
#     if i%2==0:
#         a.append(c.lower())
#     else:
#         a.append(c.upper())
# print("".join(a))

a,_b="c","d"
print(_b)
print(type(_b))
