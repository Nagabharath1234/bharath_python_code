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

# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print("factorial cannot be negative")
# elif num==0:
#     print("the factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print("the factorial number is",factorial)

# a="bharath"
# s=""
# for i in a:
#     s=i+s
# print(s)

# a="bharath"
# s=len(a)
# print(s)

# x="apple"
# y="banana"
# print(x is not y)

# def calculater(a,b,operator):
#     if operator=="+":
#         return a+b
#     elif operator=="-":
#         return a-b
#     elif operator=="*":
#         return a*b
#     elif operator=="/":
#         return a/b
#     else:
#         return ("invalid input")
# res=calculater(2,4,"+")
# print(res)

# num=int(input("enter the number:"))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

# s="bharath"
# print (s[::-1])

# s="bharath"
# print (s[:3])

# def function(a,b):
#     return a+b
# res=function(3,6)
# print(res)

# list=[1,2,3,4,5,6]
# list.append(7)
# print(list)

# list=[4,5,6,7,8]
# list.extend([9,10,11,12])
# print(list)

# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)

# try:
#    a= 5/0
#    print("this shows error")
# except:
#    print("zero value error")
# finally:
#    print("always runs")

# s=5
# res=lambda x,y:x+y
# print(res(3,4))

# s= lambda x:x*2
# print(s(4))

# num=[1,2,3,4,5]
# s=list(map(lambda x:x*2,num))
# print(s)

# num=[1,2,3,4,5]
# s=list(filter(lambda x:x%2==0,num))
# print(s)

# s=[x**2 for x in range (1,6)]
# print(s)

# a=[ s for s in range(1,11) if s%2==0]
# print(a)

# def greet(a,b):
#     return(a+b)
# res=greet(2,3)
# print(res)

# a="bharath"
# s=" "
# for i in a:
#     s=i+s
# print(s)

# s="bharath"
# print (s[::-1])

# a="bharath"
# s=[]
# for i,c in enumerate(a):
#     if i%2==0:
#         s.append (c.upper())
#     else:
#         s.append (c.lower())
# print("".join(s))

# list=[1,2,3,4,5,'bharath','sai','naveen',22,333,444,'ravi']
# names=[]
# numbers=[]
# for i in list:
#     if type(i)==str:
#         names.append(i)
#     else:
#         if type(i)==int:
#             numbers.append(i)
# print(f'separated names are {names} and separated numbbers are {numbers}')

# num=int(input("enter the number:"))
# for i in range(1,11):
#     print(f'{num} x {i} = {num*i}')

# class Student:
#     def greet(self):
#         print(f'this is student class')
# class Person(Student):
#     def greet1(self):
#         print(f'this is person class')
# obj=Person()
# obj.greet1()
# obj.greet()

# def decorator(func):
#     def wrapper():
#         print(f"this is before execution")
#         func()
#         print(f"this is after execution")
#     return wrapper()
# @decorator
# def function():
#     print("Hello!")
# function

# fruits=["apple","cherry","orange","banana"]
# res=iter(fruits)
# print(next(res))
# print(next(res))

# def generator(n):
#     count=1
#     while count<n:
#         yield count
#         count=count+1
# res=generator(6)
# print(next(res))
# print(next(res))

# list=[1,1,1,1,1,1,1,22,2,2,2,3,3,3,4,4,4,5,5,56,6,6,7,7,8,8,99,9,8]
# freq={}
# for i in list:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(f'frequency of the list is',freq) 

# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print(f'factorial cannot be negative')
# elif num==0:
#     print(f'factorial of 0 is 1')
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
# print(f'factorial of the number is ',factorial)

# num=int(input("enter the number:"))
# for i in range(2,num):
#     if num%i==0:
#         print(f'it is not a prime num')
#         break
# else:
#     print(f"it is a prime num")

# num=int(input("enter the number:"))
# a,b=0,1
# for i in range(0,num):
#     if i<0:
#         print(i)
#     else:
#         res=a+b
#         a=b
#         b=res
#         print(i)

