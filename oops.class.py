'''
class : blue print of a object
object: is a physical entity,we can create any no. of objects
'''

# class Python():
#     a=3
#     print(a)

# class Python():
#     a=2
#     def output(self):
#         print(self.a)
# b=Python()
# a=Python()
# b.output()
# a.output()

# class Student():
#     def bharath(self):
#         print("this is class")
#         age=30
#         name='bharath'
#         print(age,name)
# a=Student()
# a.bharath()


# class Student:
#     def bharath(self):
#         print("this is class")
#         a=6
#         b=5
#         print(a+b)
# obj=Student()
# obj.bharath()

# class Parent:
#     def func(self):
#         print("this is parent class")
# class Child(Parent):
#     def func1(self):
#         print("this is child class")
# obj=Child()
# obj.func1()
# obj.func()

# class Grandfather:
#     def func1(self):
#         print("this is grandfather class")
# class Father(Grandfather):
#     def func2(self):
#         print("this is Father class")
# class Child(Father):
#     def func3(self):
#         print("this is child class")
# obj=Child()
# obj.func3()
# obj.func2()
# obj.func1()

# class Father:
#     def func1(self):
#         print("this is father class")
# class Mother:
#     def func2(self):
#         print("this is mother class")
# class Child(Father,Mother):
#     def func3(self):
#         print("this is child class")

# obj = Child()
# obj.func3()
# obj.func2()
# obj.func1()

# class Parent:
#     def func(self):
#         print("this is parent class")
# class Child1(Parent):
#     def func2(self):
#         print("this is child 1 class")
# class Child2(Parent):
#     def func3(self):
#         print("this is child2 class")

# obj = Child2()
# obj.func3()
# obj.func()
# obj=Child1()
# obj.func2()
# obj.func()

# class A:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(f"my name is {self.name} and my age is {self.age}")
# class B(A):
#     def __init__(self,name,age,salary,employee):
#         super().__init__(name,age)
#         self.salary=salary
#         self.employee=employee
#         print(f"my salary is {self.salary} and iam {self.employee}")
        

# obj = B('bharath',24,25000,'engineer')


# class Student:
#     def display(self):
#         print("this is class")
#         a=6
#         b=9
#         print(a+b)
# obj=Student()
# obj.display()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def greet(self):
#         print("my name is:",self.name)
#         print("my age is :",self.age)
# obj = Person('bharath',24)
# obj.greet()

# class Python:
#     def display(self):
#         print("this is class")
#         a=9
#         b=8
#         print(a+b)
# obj =Python()
# obj.display()

# class Python:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def greet(self):
#         print("my name is",self.a)
#         print("my age is",self.b)
# obj=Python('bharath',24)
# obj.greet()

# class Student:
#     def greet(self):
#         a=9
#         b=7
#         print(a+b)
#     def greet(self):

# class Student:
#     def greet(self,a,b):
#         return(a+b)
#     def greet(self,a,b,c=9):
#         return (a+b+c)
# obj=Student()
# print(obj.greet(3,6))

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
#         print(f"my salary is {self.salary} and my dept is {self.dept}")
        
# obj=Person('bharath',25,25000,'cs')

# class A:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(f"my name is {self.name} and my age is {self.age}")
# class B(A):
#     def __init__(self,name,age,salary,employee):
#         super().__init__(name,age)
#         self.salary=salary
#         self.employee=employee
#         print(f"my salary is {self.salary} and iam {self.employee}")
        

# obj = B('bharath',24,25000,'engineer')

# def function(input):
#     return (input[::-1])
# res=function('bharath')
# print(res)

# def greet(input):
#     return (input==input[::-1])
# res=(greet('madam'))
# print(res)

# s=[1,2,3,4,5,6]
# res=list(map(lambda x:x*x,s))
# print(res)

# s=[1,2,3,4,5,6,7,8,9,11,33,44,66,55,57,59,13,16,15,17]
# res=list(filter(lambda x:x%2==0,s))
# print(res)

# s=lambda x,y:x+y
# res=(s(2,8))
# print(res)

# s=lambda x:x*x
# res=(s(7))
# print(res)

# s=[1,2,3,4,5,6,7,8]
# res=[x for x in s if x%2==0 ]
# print(res)

# a='bharath'
# rev=""
# for i,c in enumerate(a):
#     rev=c+rev
# print(rev)

# str='bharath'
# a=[]
# for i,c in enumerate(str):
#     if i%2==0:
#         a.append(c.lower())
#     else:
#         a.append(c.upper())
# res="".join(a)
# print(res)

# str='bharath'
# res=(str[:3].upper()+str[3:])
# print(res)


    

