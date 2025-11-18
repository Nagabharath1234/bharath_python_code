'''type conversion: is used to convert one data type to another is known as type conversion
in these two types
implicit type casting: it is automatically converts one data type to another datatype
explicit type casting : it is used to convert explicitly from the user'''

#type conversions.
# a=4
# print(float(a))

# b=5.8
# print(int(b))

# c= 567
# print(str(c))

'''Type Conversion'''
'''Convert a string representing a number into an integer and a float.'''

''' Convert a list of numbers into a tuple.'''
# list=[1,2,3,4,5,6]
# number=tuple(list)
# print(number)


# ''' Convert a tuple into a set.'''
# tup=(1,'bharath',3,4,5)
# result=set(tup)
# print(result)

''' Convert a set into a list.'''
# set={1,2,3,4,5,6}
# result=list(set)
# print(result)

# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print("factorial cannot be negative")
# elif num==0:
#     print("factorial of 0 is 1")
# for i in range(1,num+1):
#     factorial=factorial*i
# print(f"the factorial of the number is",factorial)

# num=int(input("enter the  number:"))
# for i in range(2,num):
#     if num%i==0:
#         print(f"it is not a prime num")
#         break
# else:
#     print(f"it is a prime num")

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
        
# list=[1,1,1,2,2,2,3,3,3,44,4,5,5,6,6,7,7,7,7,8,8,8]
# frequency={}
# for i in list:
#     if i in frequency:
#         frequency[i]+=1
#     else:
#         frequency[i]=1
# print(f"the frequency of the number is",frequency) 

# list=[1,2,3,4,'bharath','ravi','naveen',33,44,55]
# names=[]
# numbers=[]
# for i in list:
#     if type(i)==str:
#         names.append(i)
#     if type(i)==int:
#         numbers.append(i)
# print(f"separated names are{names} and separated numbers are{numbers}")

# class Student:
#     def greet(self):
#         print("this is student class")
# class Person(Student):
#     def greet1(self):
#         print("this is person class")
# obj=Person()
# obj.greet()
# obj.greet1()

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    print(f"my name is {self.name} and my age is {self.age}")
class Person(Student):
    def __int__(self,salary,dept,name,age):
        super().__init__(name,age)
        self.salary=salary
        self,dept=dept
    print(f"my salary is {self.salary} and my department is {self.dept}")
obj=Person('bharath',24,25000,'cse')
