''' polymorphism. many forms means it is defined as one method with many behaviour is known as polymorphism.
 method overloading : same class with same method name with diff parameters'''
# class A:
#     def sum(self,a,b):
#         return a+b
#     def sum(self,a,b,c=2):
#         return a+b+c
# obj = A()
# print (obj.sum(3,5,5))

'''method overriding : method overriding occurs when it subclass provides the specific implementation 
of the method to its defined superclass is known as method overriding'''
# class A:
#     def bharath(name):
#         print("this is class A")
# class B(A):
#     def bharath(name):
#         print('this is class b')
#         super().bharath()
# obj = B()
# obj.bharath()

'''operator overloading : it is performing beyond on its predefined capabilities is known as operator overloading'''
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __gt__(self,other):
#         if self.age>other.age:
#             return True
#         else:
#             return False
# p1=Person('ram',32)
# p2=Person('raju',28)
# if p1>p2:
#     print(f"{p1.name} will pay the bill")
# else:
#     print(f"{p2.name} will pay the bill")

# class Student:
#     def greet(self,a,b):
#         return a+b
#     def func(self,a,b,c=9):
#         return a+b+c
# obj=Student()
# print(obj.greet(3,5))

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(f"my name is {self.name} and my age is {self.age}")
# class Student(Person):
#     def __init__(self,name,age,salary):
#         self.salary=salary
#         super().__init__(name,age)
#         print (f"my salary is {self.salary}")
        
# obj=Student('bharath',24,25000)

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
        
#         print(f"my salary is {self.salary} and iam {self.employee}")
        
# obj=Person('bharath',24,25000,'engineer')

# class Demo:
#     def greet(self):
#         print("this is demo class")
# class Var(Demo):
#     def greet1(self):
#         print("this var class")
# obj=Var()
# obj.greet1()
# obj.greet()

# s="bharath"
# rev=""
# for i in s:
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

# a="bharath"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)

# a=input("enter the word:")
# if a==a[::-1]:
#     print(f"yes it is a palindrome")
# else:
#     print(f"no it is not a palindrome")

# a="bharath"
# s=[]
# for i,c in enumerate(a):
#     if i%2==0:
#         s.append (c.upper())
#     else:
#         s.append (c.lower())
# print("".join(s))

# list=[1,1,2,2,3,3,4,4,5,5,5,5,6,6,6,6,7,7,7,9]
# f={}
# for i in list:
#     if i in f:
#         f[i]+=1
#     else:
#         f[i]=1
# print(f"the frequency of the list is",f)

# list=[1,2,3,'bharath','naveen','ravi',34,5]
# names=[]
# numbers=[]
# for i in list:
#     if type(i)==str:
#         names.append(i)
#     if type(i)==int:
#         numbers.append(i)
# print(f"separated names are {names} and separated numbers are {numbers}")

def decorator(func):
    def wrapper():
        print("this is before execution")
        func()
        print("this is after execution")
    return wrapper()
@decorator
def function():
    print("Hello!")
function


