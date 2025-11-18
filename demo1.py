# list1=[1,2,3,4]
# list2=[2,3,4,5]
# result=(list1+list2)
# print(result)

# list=[1,2,3,4]
# index=list.index(2)
# list[index]='bharath'
# print(list)

# a="python"
# b=a.upper()
# print(b)
 
# try:
#     if 10/7:
#         print(f"yes correct!")
# except ZeroDivisionError:
#     print({"error":"zero division error"})
# finally:
#     print("always runs")

# a="bharath"
# s=[]
# for i,c in enumerate(a):
#     if i%2==0:
#         s.append(c.lower())
#     else:
#         s.append(c.upper())
# print("".join(s))

# a="bharath"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)

# list=[1,2,2,2,3,3,3,4,4,5,6,7,7,8,8,9,9]
# f={}
# for i in list:
#     if i in f:
#         f[i]+=1
#     else:
#         f[i]=1
# print(f"the frequency of the list is",f)
    
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

# def generator(n):
#     count=0
#     while count<n:
#         yield count
#         count+=1
# res=generator(7)
# print(next(res))
# print(next(res))

# fruits=["apple","orange",'cherry']
# res=iter(fruits)
# print(next(res))
# print(next(res))

# num=int(input("enter the number:"))
# for i in range(2,num):
#     if (num%i)==0:
#         print(f"it is not a prime num")
#         break
# else:
#     print(f"it is a prime num")

# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print(f"the factorial cannot be zero")
# elif num==0:
#     print(f"factorial of 0 is 1")
# else:
#     for i in range(1,1+num):
#         factorial=factorial*i
# print(f'the factorial of the number is:',factorial)

# num=int(input("enter the number:"))
# a,b=0,1
# for i in range(0,num):
#     if num<=1:
#         print(i)
#     else:
#         res=a+b
#         a=b
#         b=res
#         print(f"the fibonacci of the number is:",res)

# num=int(input("enter the number:"))
# if num%2==0:
#     print(f"even num")
# else:
#     print(f"odd num")

# list=[1,2,3,4,5,6,7,8,9]
# for i in list:
#     if i%2==0:
#         print(i)

# a="bharath"
# res=a[:3].upper()+a[3:]
# print(res)

# d={1,'bharath',2,'ravi',3,'naveen'}
# numbers=[]
# names=[]
# for i in d:
#     if type(i)==str:
#         names.append(i)
#     if type(i)==int:
#         numbers.append(i)
# print(f"the separation of names are,{names} separation of numbers are:,{numbers}")

# list=[1,2,3,'bharath','raju' ,4,56,6,7,8]
# names=[]
# numbers=[]
# for i in list:
#     if type(i)==str:
#         names.append(i)
#     if type(i)==int:
#         numbers.append()
# print("separation of names are:"names, separation of numbers are:", {numbers})
        

# num=int(input("enter the number:"))
# for i in range(0,11):
#     print(f"{num} x {i} = {num*i}")

# num=int(input("eter the number:"))
# total=0
# for i in range(1,num+1):
#     total=total+i
#     print(f"the sum of {num} natural number is:",total)

# a="bharath"
# res=a[::-1]
# print(res)

# a="bharath"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)

# x=9
# y=8
# print(x is not y)


# s=[1,2,3,4,5,6,7,8,9]
# print(list(filter(lambda x:x%2==0,s)))

# s=[1,2,3,4,5,6,7,8]
# print(list(map(lambda x:x*2,s)))

# list=[1,2,3,4,5,6,7,8,9]
# s=[x for x in list if x%2==0]
# print(s)

# list=[1,2,3,4,5,6,7,8]
# s=[x*2 for x in list]
# print(s)

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
#         print(f"my salary is {self.salary} and iam from {self.dept}")
# obj=Person('bharath',24,25000,'cse')

# class Student:
#     def greet(self,a,b):
#         return a+b
#     def greet(self,a,b,c=4):
#         return a+b+c
# obj=Student()
# print(obj.greet(2,3))

# a="bharath"
# b="ramu"
# print(a+","+b)

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

# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print("the factorial cannot be negative")
# elif num==0:
#     print("factorial of the 0 is 1")
# else:
#     for  i in range(1,num+1):
#         factorial=factorial*i
#     print("the factorial of the number is:",factorial)

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
#         print(f"my salary is {self.salary} and my department is {self.dept}")
# obj=Person('bharath',24,25000,'cse')

# class Student:
#     def greet(self,a,b):
#         return a+b
#     def greet(self,a,b,c=9):
#         return a+b+c
# obj=Student()
# print(obj.greet(3,4))

# class Person:
#     def __init__(self,a,b):
#         self.__a=a
#         self._b=b
       
# class Student(Person):
#     def output(self):
#         print(self._b)
# obj=Student(3,4)
# obj.output()

# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print(f"factorial cannot be negative")
# elif num==0:
#     print(f"factorial of 0 is 1")
# else: 
#     for i in range(1,num+1):
#         factorial=factorial*i
# print(f"factorial of the number is :",factorial)

# num=int(input("enter the number:"))
# for i in range(2,num):
#     if num%i==0:
#         print(f"it is not a prime nuum")
#         break
# else:
#     print(f"it is a prime num")

# num=int(input("enter the number:"))
# if num%2==0:
#     print("it is even num")
# else:
#     print("it is odd num")

# a="bharath"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)

# a="bharath"
# s=[]
# for i,c in enumerate(a):
#     if i%2==0:
#         s.append(c.lower())
#     else:
#         s.append(c.upper())
# print("".join(s))

# list=[1,2,3,'bharath','balu','mohith']
# names=[]
# numbers=[]
# for i in list:
#     if type(i)==str:
#         names.append(i)
#     if type(i)==int:
#         numbers.append(i)
# print(f"separetion of names are{names} and separation of numbers{numbers}")

# num=int(input("enter the number:"))
# for i in range(0,11):
#     print(f"{num} x {i} = {num*i}")

# list=[1,1,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6,7,7,8,8,9,0,9]
# frequency={}
# for i in list:
#     if i in frequency:
#         frequency[i]+=1
#     else:
#         frequency[i]=1
# print(f"the frequency of the list is:",frequency) 

# def calculater(a,b,operator):
#     if operator=="+":
#         return(a+b)
#     elif operator=="-":
#         return(a-b)
#     elif operator=="*":
#         return(a*b)
#     elif operator=="/":
#         return(a/b)
#     else:
#         return "invalid input"
# res=calculater(2,5,"*")
# print(res)

# a=input("enter the word:")
# if (a==a[::-1]):
#     print(f"it is a palindrome")
# else:
#     print(f"it is not a palindrome")

# a="bharath"
# print(a[::-1])

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

def generator(num):
    count=0
    while count<num:
        count+=1
        yield count
res=generator(5)
print(next(res))
print(next(res))