'''__init__(self,...) :-constructor method called automatically when an object is created'''
'''(constructor)'''
# class Person:
#     def __init__(self,name):
#         self.name=name
# p=Person("bharath")
# print(p.name)

'''__str__(self) :- it returns a user friendly string representation of the object (used by print)'''
'''(use friendly string)'''
# class Person:
#     def __str__(self):
#         return "this is person object"
# print(Person())

'''__repr__(self)  :- it returns a developer friendly string representation, often used in debugging or repr() '''
'''(developer friendly string)'''
# class Person:
#     def __repr__(self):
#         return "this is bharath's object"
# print(repr(Person()))


''' write a python code in oops concept use __init__,__str__,__len__,__del__'''
# class Book:
#     def __init__(self,title,author,pages):
#         print("a book is created")
#         self.title=title
#         self.author=author
#         self.pages=pages

#     def __str__(self):
#         return (f"{self.title} by {self.author} {self.pages} pages")

#     def __len__(self):
#         return self.pages

#     def __del__(self):
#         print("book is deleted")

# obj=Book('A bunch of roots','bharath',300)
# print (obj)
# print(len(obj))
# del obj

# class Student:
#     def __init__(self,rollno,name,age,):
#         print("this is student details")
#         self.rollno=rollno
#         self.name=name
#         self.age=age

#     def __str__(self):
#         return (f"{self.rollno} of {self.name} is {self.age} years old")
    
#     def __len__(self):
#         return self.age
    
#     def __del__(self):
#         print("student is deleted")

#     def __repr__(self):
#         print()

# obj=Student(102,'bharath',24)
# print(obj)
# print(len(obj))
# del obj

'''write a python code for bank account details iuse deposit and withdrawal method'''
# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         print(f"amount deposited:{amount} to your account |balance is:{self.balance}")
#     def withdraw(self,amount):
#         if amount>self.balance:
#             print(f"balance not enough!!")
#         else:
#             self.balance=self.balance-amount
#             print(f"amount withdrawal:{amount} from your account| balance is:{self.balance}")
#     def __str__(self):
#         return(f"your available balance is: {self.balance}")
# obj=BankAccount('bharath',10000)
# print(obj)
# obj.deposit(2000)
# obj.withdraw(5000)

'''write a python code for book use all magic methods in oops concept'''
# class Book:
#     def __init__(self,title,auther,pages,books,models,item):
#         self.title=title
#         self.auther=auther
#         self.pages=pages
#         self.books=books
#         self.models=models
#         self.item=item
#         print("this is Book details")
#     def __str__(self):
#         return(f"{self.title} by {self.auther} {self.pages} pages")
#     def __len__(self):
#         return(self.pages)
#     def __repr__(self):
#         return(f"this is bharath {self.books}")
#     def __setitem__(self,key,value):
#         print (f"setting {key} to this {value}")
#         setattr(self,key,value)
#     def __getitem__(self,key):
#         print (f"getting this is {key}")
#         return getattr(self,key)
#     def __del__(self):
#         print("Book deleted successfully")
# obj=Book('flying in air','bharath',300,'macbook','audi','mycar' )
# print(obj)
# print(len(obj))
# print(repr(obj))
# obj['models']='audi'
# print(obj['models'])


'''write a python code give example of __init__ and __str__ in magic method'''
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("this is Student class")
#     def __str__(self):
#         return(f"my name is :{self.name}, my age is :{self.age} ")
# obj=Student('bharath',24)
# print(obj)

'''write a python code give example of __len__ in magic method'''
# class Person:
#     def __init__(self,pages):
#         self.pages=pages
#         print("this is Person class")
#     def __len__(self):
#         return self.pages
# obj=Person(200)
# print(len(obj))

'''write a python code give example of __repr__ in magic method'''
# class Person:
#     def __init__(self,name):
#         self.name=name
#     def __repr__(self):
#         return(f"this is {self.name} class")
# obj=Person('bharath')
# print(repr(obj))

# class Student:     # here, we are creating a class with the name Student  
#     def __init__(self,name,grade):    
#          self.name = name    
#          self.grade = grade    
#     # @property    
#     def display(self):    
#          return self.name + " got grade " + self.grade    
    
# stu = Student("John","B")    
# print("Name of the student: ", stu.name)    
# print("Grade of the student: ", stu.grade)    
# print(stu.display)

# class Student:
#     def __init__(self,name,grade):
#         self.name=name
#         self.grade=grade
#     def display(self):
#         return (self.name + " "+ self.grade)
# obj=Student('bharath',"B")
# print(f"name of the student:{obj.name}")
# print(f"grade of the student:{obj.grade}")
# obj.display()

# class Car:
#     def __getitem__(self,key):
#         self.key=key
#         print("this is car")
#         return key
# obj=Car()
# print(obj['bmw'])

# class Car:
#     def __setitem__(self,key,value):
#         self.key=key
#         self.value=value
#         print("this is car")
# obj=Car()
# obj['audi:']=2025
# print(obj.key,obj.value)

# class Student:
#     def greet(self):
#         print("this is student class")
# class Person(Student):
#     def greet1(self):
#         print("this is person class")
# obj=Person()
# obj.greet()
# obj.greet1()

# class Father:
#     def greet(self,a,b):
#         return a+b
#     def greet(self,a,b,c=9):
#         return a+b+c
# obj=Father()
# print(obj.greet(2,3))

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

# list=[1,1,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,77,8,8,9,9,0,8]
# f={}
# for i in list:
#     if i in f:
#         f[i]+=1
#     else:
#         f[i]=1
# print(f"the frequency of the number is:",f)

# num=int(input("enter the number:"))
# if num%2==0:
#     print(f"even number")
# else:
#     print(f"odd number")
    
# list=[12,13,14,24,23,25,26,27,29,28,23,34,45,56,67,78]
# for i in list:
#     if i%2==0:
#         print(f"even numbers are:",i)

# def decorator(func):
#     def wrapper():
#         print("it is before execution")
#         func()
#         print(f"it is after execution")
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


# a=['apple','banana','orange']
# res=(iter(a))
# print(next(res))
# print(next(res))

# num=int(input("enter the num:"))
# a,b=0,1
# for i in range(0,num):
#     if num<=1:
#         print(i)
#     else:
#         res=a+b
#         a=b
#         b=res
#     print(res)

# num=int(input("enter the number:"))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

def calculator(operator,a,b):
    if operator == "+":
        return (a+b)
    elif operator == "-":
        return (a-b)
    elif operator == "*":
        return (a*b)
    elif operator == "/":
        return (a/b)
    else:
        return ("invalid input")
res=calculator("-",3,6)
print(res)


    