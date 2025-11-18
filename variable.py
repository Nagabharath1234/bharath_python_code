'''variables are used to store the values it acts like a container'''


# variable = values
# a=10
# print(a)

# a,b,c=1,4,6
# print(a,b,c)

# a=1,2,3,4,5,6
# print(a)

# a=v=b=22
# print(a,v,b)

# a=4
# print(id(a)) 

# python = 1
# PYTHON = 23
# print(PYTHON)

# a=8
# b=3j
# print(a+b)
# print(type(b))

# a="bharath"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)

# s="bharath"
# g=[]
# for i,c in enumerate(s):
#     if i%2==0:
#         g.append (c.lower())
#     else:
#         g.append(c.upper())
# print("".join(g))

# list=[1,2,2,3,3,4,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,9]
# f={}
# for i in list:
#     if i in f:
#         f[i]+=1
#     else:
#         f[i]=1
# print(f"the frequency of the list is",f)

# list=[1,2,3,4,5,'bharath','naveen',77,88]
# names=[]
# numbers=[]
# for i in list:
#     if type(i)==str:
#         names.append(i)
#     if type(i)==int:
#         numbers.append(i)
# print(f"separated names are {names} and separeted numbers are {numbers}")

# a="bharath"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)

# a="santosh"
# print(a[::-1])

# list=["bharath",1,2,3,"naveen",34,56,78,"ravi"]
# names=[]
# numbers=[]
# for i in list:
#     if type(i)==str:
#         names.append(i)
#     if type(i)==int:
#         numbers.append(i)
# print(f"separated names are {names} and separated numbers are {numbers}")

# list=[12,34,56,55,66,77,98,97,75]
# for i in list:
#     if i%2==0:
#         print(i)

# num=int(input("enter the number:"))
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")

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

# num=int(input("enter the number:"))
# for i in range(2,num):
#     if num%i==0:
#         print(f"it is not a prime num")
#         break
# else:
#     print(f"it is a prime num")

# num=int(input("enter the number:"))
# a,b=0,1
# for i in range(0,num):
#     if i<=0:
#         print(i)
#     else:
#         res=a+b
#         a=b
#         b=res
#     print(res)

# a="bharath"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)

# a="bharath"
# print(a[::-1])

# num=int(input("enter the number:"))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print(f"factorial cannot be negative")
# elif num==0:
#     print(f"factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
# print(f"factorial of the number is",factorial)

# num=int(input("enter the number:"))
# for i in range(2,num):
#     if (num%i)==0:
#         print(f"it is a not prime num")
#         break
# else:
#     print(f"it is a prime num")

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

# list=[1,2,3,3,3,4,4,5,5,6,6,7,7,8,8,8,8,9,9,9]
# frequency={}
# for i in list:
#     if i in frequency:
#         frequency[i]+=1
#     else:
#         frequency[i]=1
# print(f"the frequency of the list is",frequency)
    
# list=[1,'naveen','ravi','prakask',33,44,55]
# names=[]
# numbers=[]
# for i in list:
#     if type(i)==str:
#         names.append(i)
#     if type(i)==int:
#         numbers.append(i)
# print(f"the separated names are",names)
# print(f"the separated numbers are",numbers)

# def calculator(a,b,operator):
#     if operator=="+":
#         return(a+b)
#     elif operator=="-":
#         return(a-b)
#     elif operator=="*":
#         return(a*b)
#     elif operator=="/":
#         return(a/b)
#     else:
#         print("invalid input")
# res=calculator(3,4,'*')
# print(res)

# a=int(input("enter the number:"))
# factorial=1
# if a<0:
#     print(f"the factorial cannot be negative")
# elif a==0:
#     print(f"the factorial of 0 is 1")
# else:
#     for i in range(1,a+1):
#         factorial=factorial*i
# print(f"the factorial of the number is",factorial)

# num=int(input("enter the number:"))
# for i in range(2,num):
#     if num%i==0:
#         print(f"it is not a prime num")
#         break
# else:
#     print(f"it is a prime num")

# num=int(input("enter the number:"))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

# a="bharath"
# print(a[::-1])

# s="bharath"
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)

def calculator(a,b,operator):
    if operator=="+":
        print(a+b)
    elif operator=="-":
        print(a-b)
    elif operator=="*":
        print(a*b)
    elif operator=="/":
        print(a/b)
    else:
        print("invalid input!")
print(calculator(2,3,"*"))
