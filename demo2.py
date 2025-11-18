# class Person:
#     def func(self):
#         print("this is person class")
# class Student(Person):
#     def func(self):
#         print("this is student class")
#         # super().func()
# obj=Student()
# obj.func()

# def decorator(func):
#     def greet():
#         print("this is before execution")
#         func()
#         print("this is after execution")
#     return greet()
# @decorator
# def function():
#     print("Hello!")
# function

# list=[1,2,2,3,3,3,4,4,4]
# a={}
# for i in list:
#     if i in a:
#         a[i]+=1
#     else:
#         a[i]=1
# print(f"count of list is:",a)

# str="helloworld"
# result=(str.upper())
# print(result)   

# a,*b,c=[1,2,3,4]
# print(b) 

# a="bharath"
# result=(a.capitalize())
# print(result)

# a="helloworld"
# result=(a[:5].upper()+a[5:])
# print (result)

# str="bharath"
# for i in str:
#     if str%i==0:
#         print(i)

# num=int(input("enter the number :"))
# factorial=1
# if num<0:
#     print("the factorial cannot be negative")
# elif num==0:
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print("factorial of the number is:",factorial)

# num=int(input("enter  the number :"))
# for i in range(2,num):
#     if (num%i)==0:
#         print("it is not a prime num")
#         break
# else:
#     print("it is a prime num")

# a="bharath"
# s=[]
# for i,c in enumerate(a):
#     if i%2==0:
#         s.append (c.lower())
#     else:
#         s.append (c.upper())
# print("".join(s))

# num=int(input("enter the number:"))
# for i in range(1,11):
#     print(f"{num}x{i}={num*i}")

# a="bharath"
# b=""
# for i in a:
#     b=i+b
# print(b)

# list=[1,'bharath',2,'naveen',3,'ravi']
# names=[]
# numbers=[]
# for i in list:
#     if type(i) ==str:
#         names.append(i)
#     if type(i)==int:
#         numbers.append(i)
# print(f"separated names are:{names},separated numbers are:,{numbers}")

# num=int(input("enter the number:"))
# for i in range(2,num):
#     if (num%i)==0:
#         print("it is not a prime num")
#         break
# else:
#     print("it is a prime num")

# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print("the factorial cannot be negative")
# elif num==0:
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print("the factorial of the number is:",factorial)

# a=input("enter the word:")
# if (a==a[::-1]):
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")

# a="bharath"
# s=""
# for i in a:
#     s=i+s
# print(s)

# s="bharath"
# a=[]
# for i,c in enumerate(s):
#     if i%2==0:
#         a.append(c.lower())
#     else:
#         a.append(c.upper())
# print("".join(a))

# list=[1,2,2,3,3,34,4,4,4,5,5,56,6,6,7,7,9]
# s={}
# for i in list:
#     if i in s:
#         s[i]+=1
#     else:
#         s[i]=1
# print(f"the frequency of the list is:",s)

# def decorator(func):
#     def wrapper():
#         print("it is before execution")
#         func()
#         print("it is before execution")
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
# res=generator(2)
# print(next(res))
# print(next(res))

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

# rows =int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(rows-i):
#         print("*",end=" ")
#     print()

# rows=int(input("enter the number of rows:"))
# for i in range (1,rows+1):
#     for j in range(rows-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end=" ")
#     print()

# a="bharath"
# print(a[::-1])

# num=int(input("enter the number:"))
# if num%2==0:
#     print("even num")
# else:
#     print("odd num")

# list=[1,'bharath',2,3,4,'ravi',56,8,'ramu']
# names=[]
# numbers=[]
# for i in list:
#     if type(i)==str:
#         names.append(i)
#     if type(i)==int:
#         numbers.append(i)
# print(f"the separation of names{names} separation of numbers{numbers}")

# num=int(input("enter the number"))
# factorial=1
# if num<0:
#     print(f"factorial cannot be negative")
# elif num==0:
#     print(f"factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print(f"factorial of the number is", factorial)

# a="bharath"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)


# s="bharath"
# print(s[::-1])

# num=int(input("enter the number:"))
# for i in range(2,num):
#     if num%i==0:
#         print(f"it is not a prime num")
#         break
# else:
#     print(f"it is a prime num")

list=[1,"bharath",2,3,4,5,6,7,"naveen","ashok"]
names=[]
numbers=[]
for i in list:
 if type(i)==str:
  names.append(i)
 if type(i)==int:
   numbers.append(i)
print(f"the seperation of names are {names}")
print(f"the separation of numbers are {numbers}")