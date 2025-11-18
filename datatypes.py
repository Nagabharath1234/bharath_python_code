''' data types are defined as type of a value like int,str,bool,float

int()
float()
bool()
str()
'''

# data types.
# a=1
# b=2.5
# c="vikas"
# d=True
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# a=2+5j
# print(type(a))

# def function (a,b):
#     return(a+b)
# print (function(3,4))

# def display(*a):
#     return (a)
# print(display(1,2,3,4,5,6,7,8))

# def greet(**a):
#     return(a)
# result=greet(name='bharath')
# print(result)

# list=[1,2,3,4,-2,-6,-7,-8]
# for i in list:
#     if i<0:
#         print(i)

# lists=[1,2,3,4,5,8,12,23,45,67,46,47,67,69,68]
# a=sorted(lists)
# print(a)

# lists=[1,2,3,4,5,8,12,23,45,67,46,47,67,69,68]
# lists.sort(reverse=True)
# print(lists[1])

# class Student:
#     def display(self):
#         return("this is class")
#     a=9
#     b=8
#     print(a+b)
# obj=Student()
# obj.display()

# str='12345'
# print (int(str))

# a=2
# print(float(a))

# class Student:
#     def display(self,a,b):
#         return(a+b)
#     def display(self,a,b,c=8):
#         return(a+b+c)
# obj=Student()
# print(obj.display(1,2))

# class Student:
#     def display(self):
#         print ("this is a class")
# class Person(Student):
#     def display(self):
#         print("this is b class")
#         super().display()
# obj=Person()
# obj.display()

# class Person:
#     def __init__(self,a,b):
#         self.__a=a
#         self._b=b
# class Person2(Person):
#     def display(self):
#         print(self._b)
# obj=Person2(3,4)
# obj.display()
        

# class Demo():
#     def __init__(self,a,b):
#         self.__a=a
#         self._b=b
# class Demo2(Demo):
#     def output(self):
#         print(self._b)
# d=Demo(3,4)
# d.output()

# list=[1,2,34,56,67,57,89,90,77,55,33,22]
# result=[x for x in list if x%2==0]
# print(result)

# result={x%3 for x in list}
# print(result) 

# def even(n):
#     return n%2==0
# print(even(2))
# print(even(3))

# nums=[1,2,3,4,5,6,7,8]
# result=list(map(lambda x:x*x,nums))
# print(result)

# nums=[12,34,23,22,55,66,77,88,90]
# result=list(filter(lambda x:x%2==0,nums))
# print(result)

# list=[1,2,3,4,5,6]
# result=[x for x in list if x%2==0]
# print(result)

# nums=[1,2,3,4,5,6,7]
# squares=list(map(lambda x:x*x,nums))
# print(squares) 

# def display(a,b):
#     return a+b
# print(display (3,6))

# def even_odd(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
# result=int(input("enter the number"))
# print (even_odd(result))

# class Student:
#     def display(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a+self.b)
# obj=Student()
# obj.display(7,9)

# class Person:
#     def display(self):
#         print("this is person class")
# class Student(Person):
#     def display1(self):
#         print("this is student class")
# obj=Student()
# obj.display1()
# obj.display()

# class Parent:
#     def display(self):
#         print("this is parent class")
# class Child(Parent):
#     def display2(self):
#         print("this is child class")
# obj=Child()
# obj.display2()
# obj.display()

# class Father:
#     def func1(self):
#         print("this is father class")
# class Mother():
#     def func2(self):
#         print("this is mother class")
# class Child(Father,Mother):
#     def func3(self):
#         print("this is child class")
# obj=Child()
# obj.func3()
# obj.func2()
# obj.func1()

# class Person:
#     def display(self,a,b):
#         return a+b
#     def display(self,a,b,c=9):
#         return a+b+c
# obj=Person()
# print(obj.display(3,5))

# class Student:
#     def display(self):
#         print("this is student class")
# class Person(Student):
#     def display(self):
#         print("this is person class")
#         super().display()
# obj=Person()
# obj.display()      

# age=12
# if age>18:
#     print('eligible for vote')
# elif age==18:
#     print("becomming major")
# else:
#     print("minor")

# def function(a,b):
#     return a+b
# result=function(2,3)
# print(result)

# list=[1,2,3,4,5,6,7,8,9]
# for i in list:
#     if i%2==0:
#         print(i)

# def decorator(func):
#     def wrapper():
#         print("this is before execution")
#         func()
#         print("this is after execution")
#     return wrapper()
# @decorator
# def function():
#     print("Hello")
# function

# def generator(n):
#     count=0
#     while n<5:
#         yield count
#         count+=1
# res=generator(1)
# print(next(res))
# print(next(res))

fruits=["apple","banana","orange"]
res=iter(fruits)
print(next(res))
print(next(res))