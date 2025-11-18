# coding part

# print("hello world,3+4")

# s = 'bharath' 
# reverse =(s[::-1])
# print (reverse)

# num = [1,2,3,4,5,6]
# for num in num:
#     if num%2==0:
#         print(num)


# class Bharath:
#     print('this is class')
#     def display(self):
#         a=30
#         b=20
#         print(a,b)
# obj = Bharath()
# obj.display()

# def add(a,b):
#     return (a+b)
# print (add (2,3))

# class School:
#     print('go to school')
#     def display(self):
#         a= 56
#         b=60
#         print(a+b)
# obj = School()
# obj.display()

# num = [1,2,3,4,5,6,7,8,9]
# for num in num:
#     if num%2==0:
#         print(num)

# # single inheritance
# class Parent:
#     def fun1(self):
#         print('this is parent class')
# class Child(Parent):
#     def fun2(self):
#         print('this is child class')
# obj = Child()
# obj.fun2()
# obj.fun1()

# class method.// oops concept
# class Student:
#     print('this is class')
#     def display(self):
#         a=3
#         b=50
#         print(a*b)
# obj = Student()
# obj.display()

# class Student:
#     def __init__(b,rollno,name,age):
#         b.rollno=rollno
#         # self.name=name
#         # self.age=age
#     def display(b):
#         print("rollno:",b.rollno)
#         # print("name:",self.name)
#         # print("age:",self.age)
# obj = Student("102","bharath","24")
# obj.display()

# class Student:
#     print('this is class')
#     def display(self):
#         a=40
#         b=50
#         print(a+b)
# obj = Student()
# obj.display()

# class College:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("name:",self.name)
#         print("age:",self.age)
#         print("--------------")
# obj=College('bharath',24)
# obj.display()
# obj2 = College("ravi",25)
# obj2.display()

# # single inheritance
# class Parent:
#     def fun(self):
#         print('this is parent class')
# class Child(Parent):
#     def fun1(self):
#         print('this is child class')
# obj = Child()
# obj.fun1()
# obj.fun()

# # multilevel inheritance
# class Parent:
#     def fun(self):
#         print('this is parent class')
# class Child(Parent):
#     def fun1(self):
#         print("this is child")
# class GrandChild(Child):
#     def fun2(self):
#         print("this is grand child")
# obj =GrandChild()
# obj.fun()
# obj.fun1()
# obj.fun2()

# #hirarchial inheritance
# class Parent:
#     def fun(self):
#         print('this is parent class')
# class Child1(Parent):
#     def fun1(self):
#         print("this is child1")
# class Child2(Parent):
#     def fun2(self):
#         print("this is child2")
# obj =Child2()
# obj.fun()
# obj.fun2()


# #multiple inheritance
# class Father:
#     def fun(self):
#         print('this is father class')
# class Mother:
#     def fun1(self):
#         print("this is mother")
# class Child(Father,Mother):
#     def fun2(self):
#         print("this is child")
# obj =Child()
# obj.fun()
# obj.fun1()
# obj.fun2()

# # super keyword
# class A:
#     def __init__(self):
#         print('this is class a')
 
#     def fun1(self):
#         print('this is  class')
# class B(A):
#     def __init__(self):
#         print("this is class b")
#         super().__init__()
#     def fun2(self):
#         print('this is class ')
# obj = B()



# class A:
#     def sum (self,a,b,c=4):
#         return(a+b+c)
#     # def sum(self,a,b):
#     #     return(a+b)
# obj = A() 
# print (obj.sum(3,4,5))

# x= input("enter the value of x:")
# y=input("enter the value of y:")
# z=x
# x=y
# y=z
# print('the value of x after swapping:{}'.format(x))
# print('the value of y after swapping:{}'.format(y))
# print(z)

# a=input("enter the word:")
# if a==a[::-1]:
#     print("it is a palindrome")
# else:
#     print('it is not a palindrome')

# def sum_list(numbers):
#     return sum(numbers)
# my_list=[150,3,56,78]
# print(sum_list(my_list))

# def maximum_num(numbers):
#     return max(numbers)
# maximum_numbers=[1,2,3,45,4,5,6]
# print(maximum_num(maximum_numbers))

# def minimum_num(numbers):
#     return min(numbers)
# minimum_numbers=(1,89,76,45,50)
# print(minimum_num(minimum_numbers))

# def reverse_string(input):
#     return (input[::-1])
# result='bharath'
# print(reverse_string(result))

# def prime_number(num):
#     if num <= 1:
#         return False
#     for i in range(2,num):
#         if num%2==0:
#             return True


# prime_num=(2,45,56,78,89,99,97,63)
# for num in prime_num: 
#     if num%2==0:
#         print(f'{num} :prime_number')
#     else:
#         print(f'{num} :it is not a prime number')

# list=[1,2,3,4,5,6,7,8,7,6,5,4,3,2]
# s=len(list)
# print(s)


# # even and odd numbers.
# def even(n):
#     return n%2==0
# print (even(4))
# print (even(5))

# def maximum(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# print (maximum(5,7))

# def min_num(numbers):
#     return min(numbers)
# minimum_num = (1,2,3,4,5,6)
# print ((min_num)minimum_num)
 

# list = [1,2,3,4,5,6,7,8,9]
# for i in list:
#     if i%2==0:
#         print (i)

# list = [1,2,3,4,5,6,7,8,9,0]
# for i in list:
#     if i%2!=0:
#         print(i)

# num = int(input("enter the digit"))
# if num%2==0:
#     print("even number")
# else:
#     print("odd number")

# def check_odd_even(num):
#     if num%2==0:
#         return("even number")
#     else:
#         return ("odd number")
# result = check_odd_even(67)
# print (result)

# def even_num(n):
#     for i in range(1,10):
#         if i %2==0:
#             print(i)
# result = even_num(10)
# print(result)

# list = [1,2,3,4,5,6,7,8,9]
# for i in list:
#     if i%2!=0:
#         print(i)

# def reverse_str(input):
#     return (input[::-1])
# result = reverse_str("bharath")
# print(result)

# def is_palindrome(input):
#     return (input==input[::-1])
# result = is_palindrome("madam")
# result1=is_palindrome("bharath")
# print(result)
# print(result1)


# a = input("enter the word:")
# if a==a[::-1]:
#     print("it is palindrome")
# else:
#     print("it is not a palindrome")



# for i in range(1,10):
#     print(i)

# i=20
# while i<=26:
#     print(i)
#     i+=1

# for i in range(20,27):
#     print(i)

# class Student:
#     print("this is class")
#     def display(a):
#         a=5
#         b=6
#         print(a+b)
# obj = Student()
# obj.display()


# num = int(input("enter the number"))
# if num>1:
#     for i in range (2,num):
#         if (num%i)==0:
#             print(num,"it is not a prime number")
#         break
#     else:
#         print(num,"it is a prime number")
# else:
#         print(num,"it is not a prime number")


# class Student:
#     print("this is class")

# a=input("enter the word:")
# if a==a[::-1]:
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")

# a=[89,67,90,87,88,76,66]
# for i in a:
#     if i%2==0:
#         print(i)

# s=lambda x:x+10
# print (s(3))  

# add=lambda x,y:x+y
# print(add(3,6))

# def bharath(a,b):
#     return (a+b)
# print (bharath(3,8))

# class Student:
#     print("this is class")
#     def display(self):
#         a=8
#         b=9
#         print(a+b)
# obj=Student()
# obj.display()

# list =[1,2,3,4,5,67,78]
# result = min(list)
# print(result)

# class Parent:
#     def fun(self):
#         print("this is parent class")
# class Child(Parent):
#     def fun1(self):
#         print("this is child class")
# obj=Child()
# obj.fun1()
# obj.fun()

# num=7 
# f=1
# for i in range(1,num+1):
#     f*=i
# print(num,"factorial")

# import math
# print (math.factorial(input()))

# def factorial(n): 
#     return 1 if n == 0 else n * factorial(n - 1)
# num = int(input("Enter a number: "))
# print(f"The factorial of {num} is {factorial(num)}")
 

# below statement will print something
# print ("hello world!")

# rows = int(input("enter the rows:"))
# for i in range(rows):
#     for j in range(i+1):            
#         print(" ",end="")
    
#         print("*",end=" ")
#     print()

# rows = int(input("enter the rows:"))
# for i in range(rows):
#     for j in range(rows-i):
#         print(" ",end="")
    
#         print("*",end=" ")
#     print()

# rows = int(input("enter the rows:"))
# for i in range(rows):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(rows-i):
#         print("*",end=" ")
#     print()

# rows = int(input("enter the rows:"))
# for i in range(rows):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(rows):
#         print("*",end=" ")
#     print()


# for i in range (1,20,2):
#     print(i)

# list=[1,2,3,'bharath','raju' ,4,56,6,7,8]
# names=[]
# numbers=[]
# for i in list:
#     if type(i)==str:
#         names.append(i)
#     if type(i)==int:
#         numbers.append()
# print("separation of names are:"names, separation of numbers are:", {numbers})