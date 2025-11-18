# import functions

# functions.add(3,3)
# functions.sub(4,2)

# functions.mul(3,8)

# a=  
# print(a)

# x=67
# print(x)
# print(type(x))
# print(float(x))

# age=12
# if age>18:
#     print("adult")
# elif age==18:
#     print("become adult")
# else:
#     print("minor")

# for i in range(0,9):
#     print(i)

# n=20
# while n<=29:
#     print(n)
#     n+=1

# for i in range (10):
#     if i ==6:
#         break
    
#     print(i)

# for i in range (1,12):
#     if i ==6:
#         continue
    
#     print(i)

# def input(a,b):
#     return (a+b)
# print (input(1,2))

# def is_function(*a):
#     print("this is function",a)
# is_function(1,2,3,4,5)
  
# def function(**a):
#     print("this is function",a)
# function(a=2,b=6,c=9)

# s= lambda a,b:a+b
# print(s(19,8))

# num=[1,2,3,4,5,6]
# s=list(map(lambda x:x**2,num))
# print(s)

# num=[1,2,3,4,5,6]
# s=list(filter(lambda x:x%2==0,num))
# print(s)

# try:
#     num=10/0
#     print("it is divisible by 2")
# except:
#     print("Error:it is can't divisible by zero")
# finally:
#     print("always")

# for i in range(0,10):
#     print(i,end="")

# str='1234567'
# print(str)

# num = [78]
# for i in num:
#     if i%2==0:
#         print(i)

# num=[1,2,3,45,67,89,90]
# for i in num:
#     if i%2==0:
#         print(i)

# def function (a,b):
#     return a+b
# result= function(3,4)
# print(result)

# num=int(input("enter the number:"))
# if num%2==0:
#     print("even numbers")
# else:
#     print("odd numbers")

# num=int(input("enter any number"))
# if num>1:
#     for i in range(2,num):
#         if (num%2)==0:
#             print("it is not a prime number")
#             break
#         else:
#             print("it is a prime num")
#     else:
#         print("it is not prime num")


# def is_function(*a):
#     return("this is function",a)
# result=is_function(1,2,3,4,5)
# print(result)

# def is_function(**a):
#     print("this is function",a)
# result = is_function(a=9,b=80,c=60)

# class Person:
#     def display(self):
#         print("this is class")
#         a=6
#         b=7
#         print(a+b)
# obj=Person()
# obj.display()

# class Student:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def display(self):
#         print(self.a*self.b)
# obj=Student(5,5)
# obj.display()
    
# class Student:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def display(self):
#         if type(self.a)==int and type(self.b)==int:
#             print(self.a+self.b)
#         else:
#             print("invalid")
# obj=Student(6,5)
# obj.display()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("name:",self.name)
#         print("age:",self.age)
# obj=Person('bharath',24)
# obj.display()

# class Student:
#     def __init__(self,a,b):
#         self.__a=a
#         self._b=b
#     def display(self):
#         print(self._b)
# obj=Student(3,4)
# obj.display()

# class Student:
#     def display(self,a,b):
#         return a+b
#     def display(self,a,b,c=9):
#         return a+b+c
# obj=Student()
# print(obj.display(2,3))       

# class A:
#     def display(self):
#         print("this is class A")
# class B(A):
#     def display(self):
#         print("this is class B")
#         super().display()
# obj=B()
# obj.display()   

# class Parent:
#     def func1(self):
#         print("this is parent class")
# class Child(Parent):
#     def func2(self):
#         print("this is Child class")
# obj=Child()
# obj.func2()
# obj.func1()

# class Parent:
#     def func(self):
#         print("this is parent class")
# class Child1(Parent):
#     def func2(self):
#         print("this is child1 class")
# class Child2(Parent):
#     def func3(self):
#         print("this is child2 class")
# obj=Child2()
# obj.func3()
# obj.func()
# obj=Child1()
# obj.func2()
# obj.func()

# class Father:
#     def func1(self):
#         print("this is father class")
# class Mother:
#     def func2(self):
#         print("this is Mother class")
# class Child(Father,Mother):
#     def func3(self):
#         print("this is child class")
# obj=Child()
# obj.func3()
# obj.func2()
# obj.func1()

# class Grandfather:
#      def func1(self):
#           print("this is grandfather class")
# class Father(Grandfather):
#      def func2(self):
#           print("this is Father class")
# class Child(Father):
#      def func3(self):
#           print("this is child class")
# obj=Child()
# obj.func3()
# obj.func2()
# obj.func1()

# num=int(input("enter the number"))
# if num>1:
#     for i in range(2,num):
#         if (num%i)==0:
#             print("it is not prime num")
#             break
#     else:
#         print("it is prime num")
# else:
#     print("it is not prime num")

# list=[12,334,33,44,55,23,44,90]
# for i in list:
#     if i%2==0:
#         print(i)

# rows=int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# rows=int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(rows-i):
#         print("*",end="")
#     print()

# rows=int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(rows-i):
#         print("*",end=" ")
#     print()

# rows=int(input("enter the number of rows:"))
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end=" ")
#     print()

# x=input("enter value of x:")
# y=input("enter the value of y:")
# temp=x
# x=y
# y=temp
# print("after swapping x:{}".format(x))
# print("after swapping y:{}".format(y))

# list=['bharath','ravi','raju','ramu']
# name='bharath'
# if name in list:
#     print("it is in list")
# else:
#     print("it is not in list")

# names=[]
# numbers=[]
# list=['bharath',23,'ravi',45,'raju',78]
# for i in list:
#     if type(i)==str:
#         names.append(i)
#     if type(i)==int:
#         numbers.append(i) 
# print("separation of names are:",names)
# print("separation of numbers are:",numbers)

# list=[1,2,3,4,5,6,7]
# list.sort(reverse=True)
# print(list[1])

# list=[1,2,3,4]
# a=tuple(list)
# print(a)

# my_tuple=(1,2,3,4,'bharath')
# my_list=list(my_tuple)
# print(my_list)

# # Original tuple
# my_tuple = (1, 2, 3, 4, 5)

# # Convert tuple to list
# my_list = list(my_tuple)

# print(my_list)


# list1=[1,2,3,4,5]
# list2=[5,6,7,8]
# a=list(set(list1)&(set(list2)))
# print(a)

# dict1={'name':'bharath','age':24,'name':'ravi','age':20}
# dict2={'name':'manoj','age':27}
# # dict1.update(dict2)
# # print(dict1)

# merged_dict=(dict1,dict2)
# print(merged_dict)

# set={1,2,3,4,5}
# a=list(set)
# print(a)

# import functions
# functions.add(3,6)
# functions.sub(10,7)
# functions.func(1,3)
# functions.greet(3,6,9) 

# def func(*a):
#     return a
# res=func(1,2,3,4,5,6,7,8,9)
# print(res)

# class Student:
#     def greet(self):
#         print("this is student class")
# class Person(Student):
#     def greet1(self):
#         print("this is person class")
# obj=Person()
# obj.greet1()
# obj.greet()

# rows=int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# rows=int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(rows-i):
#         print("*",end="")
#     print()

# rows=int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(rows-i):
#         print("*",end=" ")
#     print()

# rows=int(input("enter the number of rows:"))
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end=" ")
#     print()

# rows=int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# rows=int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(rows-i):
#         print("*",end="")
#     print()

# rows=int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(rows-i):
#         print("*",end=" ")
#     print()

# rows=int(input("enter the number of rows:"))
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(" ",end="")
#     for k in range(2*(i)-1):
#         print("*",end="")
#     print()

# a="bharath"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)

# a="bharath"
# print(a[::-1])

# num=int(input("enter the number:"))
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")
    
# def calculator(a,b,operator):
#     if operator   =="+":
#         return(a+b)
#     elif operator =="-":
#         return (a-b)
#     elif operator =="*":
#         return (a*b)
#     elif operator =="/":
#         return (a/b)
#     else:
#         return("invalid input")
# res=calculator(20,3,"+")
# print(res)

