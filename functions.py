'''
functions : function is a block of code reusability it performs a specific tasks.
block of code
'''
# def func(a,b):   # function defination
#     print(a+b)   # function body
# print (func(2,5))# function call

# def func(a,b,c):
#     print("this is function",a,b,c)
# func(1,2,3)

# def is_func(a,b):
#     print ("this is function of:" ,a,b)
# is_func(2,4)


'''arbitary arguments:it means we use (*) because we give only one parameters with multiple arguments 
 then it will be error so we using (*) it is known as arbitary arguments, it is acta as an tuple'''
# def func(*a):
#     print("this is function",a)
# func(1,2,3)

'''keyword arguments is also same as arbitary arguments but we use (**) in a keyword arguments, 
# it is acts as a dict'''
# def func(**a):
#     print("this is function",a)
# func(a=1,b=2)

'''nested function'''

# def outer():
#     print("outer function")
#     def inner():
#         print("inner function")
#     inner()
# outer()

# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)

# result = add(3,3)
# result= sub(5,3)

# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)

'''lambda function is a small and ananymous function no def needed in lambda function'''
# add = lambda x,y: x+y
# print(add(2,3))

# add = lambda x, y: x + y
# print(add(2, 3))  


'''Write a Python program that prints "Hello, World!" to the console.'''
# txt="Hello, World!"
# print(txt)

'''Even or Odd
Determine if a given number is even or odd.'''
# num=int(input("enter the number:"))

# if num%2==0:
#     print(f"even number")
# else:
#     print(f"odd number")

# def add(a,b):
#     print (a+b)
# def sub(a,b):
#     print(a-b)

# def func(a,b):
#     print("this is function",a,b)
# def greet(a,b,c):
#     print(a,b,c)

# s=lambda x,y:x+y
# print(s(8,9))

# s=[1,2,3]
# print (list(map(lambda x:x*x,s)))

# s=[1,2,3,4,5,6,7,8,9]
# print(list(filter(lambda x:x%2==0,s)))

# l="bharath"
# rev=""
# for c in l:
#     rev=c+rev
# print(rev)

# num=int(input("enter the number:"))
# if num%2==0:
#     print("even num")
# else:
#     print("odd num")

# list=[1,2,3,4,5,6,7,8,9]
# for i in list:
#     if i%2==0:
#         print(i)

# num=int(input("enter the number :"))
# for i in range(2,num):
#     if (num%i)==0:
#         print("it is not a prime num")
#         break
# else:
#     print("it is a prime num")

# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print("factorial cannot be negative")
# elif num==0:
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
# print("factorial of the number is:",factorial)

# a=input("enter the word:")
# if a==a[::-1]:
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")

# age=18
# if age>18:
#     print("eligible for vote")
# elif age<18:
#     print("not eligible for vote")
# else:
#     print("become adult")

# a="bharath"
# print(a[::-1])

# a="nagabharath"
# rev=""
# for char in a:
#     rev=char+rev
# print(rev)

# list=[1,2,2,2,2,3,4,5,6,6,6,5,5,4,4]
# freq={}
# for i in list:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)

# a="helloworld!"
# print(a.title())
# print (a[:5].upper()+a[5:])

# a="bharath"
# r=""
# for i,c in enumerate(a):
#     if i%2==0:
#         r+=c
# print(r)

# a="bharath"
# res=[]
# for i,c in enumerate(a):
#     if i%2==0:
#         res.append(c.lower())
#     else:
#         res.append(c.upper())
# print("".join(res))

'''positional arguments:'''
# def greet(name,dept,):
#     print(f"hii {name}")
#     print(f"are you {dept} department?")
# res=greet('bharath',"cs")

'''keyword arguments:'''
# def greet(name,dept):
#     print(f"hii {name}")
#     print(f"are you {dept} department")
# res=greet(name='bharath',dept="cs")

'''default arguments'''
# def greet(name,sub,dept="cs"):
#     print(f"hii {name}")
#     print(f"can you teach me {sub}")
#     print(f"are you {dept} department")
# res=greet('bharath','python')

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
# res=generator(6)
# print(next(res))
# print(next(res))

# fruits=["apple","cherry","banana"]
# res=iter(fruits)
# print(next(res))
# print(next(res))

# class Student: 
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(f"my name is {self.name} and my age is {self.age}")
# class Person(Student):
#     def __init__(self,name,age,salary,dept):
#         super().__init__(name,age)
#         self.salary=salary
#         self.dept=dept
#         print(f"my salary is {self.salary} my dept is {self.dept}")        
# obj=Person('bharath',25,25000,'cs')

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(f"my name is {self.name} and my age is {self.age}")
# class Person(Student):
#     def __init__(self,name,age,salary,employee):
#         super().__init__(name,age)
#         self.salary=salary
#         self.employee=employee
#         print(f"my salary  is {self.salary} and iam {self.employee}")
        
# obj=Person('bharath',24,25000,'engineer')

class Student:
    def __init__(self,a,b):
        
        return(a+b)
class Person(Student):
    def greet(self,a,b,c=9):
        return (a+b+c)
obj=Person()
print(obj(sum(3,6)))


        

