# num=int(input("enter the number:"))
# a,b=0,1
# for i in range(0,num):
#     if i<=0:
#         print(i)
#     else:
#         res=a+b
#         a=b
#         b=res
#         print(res)


num=int(input("enter the number:"))
a,b=0,1
for i in  range(0,num):
    if i<=0:
        print(i)
    else:
        res=a+b
        a=b
        b=res
        print(res)

'''python program to solve the fibonacci sequence using recursion'''
# def fib(n):
#     if n==1 or n==2:
#         return 1   # fibonacci formula (n-1)+(n-2)
#     else:
#         return(fib(n-1)+fib(n-2))
# print(fib(9))

'''create empty list and separate the names and numbers'''
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

'''Merge two dictionaries into one.'''
# dict1={'name':'bharath','age':24,'ravi':30}
# dict2={'name':'ashok','age':56}
# merged_dict=dict1.copy()
# merged_dict.update(dict2)
# print("merged dictionary:",merged_dict)

'''swapping of two numbers'''
# x=input("enter value of x:")
# y=input("enter the value of y:")
# temp=x
# x=y
# y=temp
# print("after swapping x:{}".format(x))
# print("after swapping y:{}".format(y))

'''check the name in list'''
# list=['bharath','ravi','raju','ramu']
# name='bharath'
# if name in list:
#     print("it is in list")
# else:
#     print("it is not in list")

'''Use list comprehension to create a list of squares of even numbers from 1 to 20.'''
# squares=[x**2 for x in range(1,21) if x%2==0]
# print(squares)

'''Use a lambda function to sort a list of tuples based on the second element.'''
# data=[('apple',3),('banana',2),('orange',1)]
# sorted_data=sorted(data,key=lambda x:x[1])
# print(sorted_data)

# data=[('apple',1),('orange',3),('cherry',2)]
# sorted_data=sorted(data,key=lambda x:x[1])
# print(sorted_data)

# list=[(3,4),(4,5),(2,7)]
# sorted_list=sorted(list[1])
# print(sorted_list)

'''Handle exceptions when dividing by zero or converting strings to integers.'''
# try:
#     num1=int(input("enter numerator"))
#     num2=int(input("enter denominator"))

#     result=num1/num2
#     print("result:",result) 

# except ValueError:
#     print("Error:please enter valid integers only")
# except ZeroDivisionError:
#     print("Error:cannot divide by zero")
# except Exception as e:
#     print("")
# finally:
#     print("always runs")

# def fibonacci(input):
#     if input<=0:
#         return []
#     if input==1:
#         return [0]
#     if input==2:
#         return[0,1]
#     seq=fibonacci(input-1)
#     seq.append(seq[-1]+seq[-2])
#     return seq
# res=fibonacci(2)
# print(res)

# num=int(input("enter the number: "))
# a,b=0,1
# for i in range(0,num):
#     if i<=1:
#         print(i)
#     else:
#         res=a+b
#         a=b
#         b=res
# print(res)

# num=int(input("enter the number:"))
# a,b=0,1
# for i in range(0,num):
#     if i<=0:
#         print(i)
#     else:
#         res=a+b
#         a=b
#         b=res
#         print(res)

# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print(f"factorial cannot be negative")
# elif num==0:
#     print(f"factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print(f"factorial of the number is",factorial)


# num=int(input ("enter the number:"))
# for i in range(2,num):
#     if (num%i)==0:
#         print(f"it is not a prime num")
#         break
# else:
#     print("it is a prime num")

# a="bharath"
# print (a[::-1])

# s="bharath"
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)

# num=int(input("enter the number:"))
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")

# for i in range(0,11):
#     if i==4:
#         break
#     print(i)

# for i in range(1,11):
#     if i==6:
#         continue
#     print(i)

# x=10
# y=3.5
# result=(x+y)
# print(result)

# num_str="124"
# num_str=int(num_str)
# print(num_str)

# rows=int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(rows-i):
#         print("*",end="")
#     print()

# rows=int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(i+1):
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
#         print("",end=" ")
#     for k in range(2*(i)-1):
#         print("*",end="")
#     print()

# a=input("enter the word:")
# result=(a[::-1])
# print(result)

# s=input("enter the word:")
# if (s[::-1]):
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")

# a=str(input("enter the string:"))
# vowels="aeiouAEIOU"
# count=0
# for char in a:
#     if char in vowels:
#         count+=1
# print(f"count of vowels",count)

# list=[1,"bharath","naveen",7,9,10,"ravi"]
# names=[]
# numbers=[]
# for i in list:
#     if type(i)==str:
#         names.append(i)
#     if type(i)==int:
#         numbers.append(i)
#     print(f"separated names are",names)
#     print(f"separated numbers are",numbers)

# s=str(input("enter the string:"))
# vowels="aeiouAEIOU"
# count=0
# for char in s:
#     if char in vowels:
#         count+=1
# print(f"count of vowels are",count)
# print(f"vowels are",vowels)

# num=int(input("enter the number"))
# if num%2==0:
#     print(f"it is even num")
# else:
#     print(f"it is an odd num")

