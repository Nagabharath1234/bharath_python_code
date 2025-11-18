#string: it is a collection of characters.
# a='python'
# b="python"
# c='''python'''
# print(type(a))
# print(type(b))
# print(type(c))

'''
lower
upper
endswith
startswith
replace
find
index
count
split
strip
lstrip
rstrip
'''

# pythonmodel = "please subscribe"
# print(pythonmodel.lower())
# print(pythonmodel.upper())
 
# python = "python language"
# print(python.endswith("l"))
# print(python.startswith("l"))

# python = "python language"
# print(python.replace("language","programming"))

# python = "python language"
# print(python.index('bharath'))
# print(python.find('bharath'))

# python = "python language"
# print(python.count('g'))

# python = "python language"
# print(print.removeprefix("python"))
# print(python.removesuffix("language"))

# python = "python language"
# print(python.split())

# python = "   python language   "
# print(python)
# print(len(python))
# a=python.strip()
# print(len(a))
# a=python.lstrip()
# print(len(a))

#list:list is a datatype, it is used with [].
# a=[1,2,3,'bharath',3.6]
# print(a)

# #positive index
# a=[1,2,3,'bharath',3.6]
# print(a[2])
# print(a[0:4:2])
# print(a[-1])

'''
append
extend
count
insert
pop
remove
index
'''
# a=[1,2,3,'bharath',3.6]
# # a.append('python')
# a.extend([3,4,5,6,7,777,88])
# print(a.count(1))
# a.remove('bharath')
# a.pop(2)
# print(a.index(3))
# a.insert(4,24)
# print(a)

# list=[1,2,3,4,5,6,7,7.8]
# print(list.index(4))


# a=[1,2,3,'bharath',3.6]
# a.remove('bharath')
# a.pop(2)

# tuple is a one of the data type in python, it is immutable datatype.

'''
concatenation
membership
identity
min()
max()
len()
'''
# a=(1,2,3,44)
# print(min(a))
# print(max(a))
# print(len(a))
# t1=(1,2,3)
# t2=(4,5,6)
# print(t1+t2)

# a=(1,2,3,44,5,566,778,90)
# print(a*2)

# a=(1,2,3,44)
# print (44 not in a)

# print (t1 is t2)

# dictionary: is a key-value pair,key is immutable

'''
get()
update()
values()
keys()
items()
'''
# d={"name":"bharath","age":24,}
# print(d["name"])
# print(d['age'])

d={"name":"bharath","age":24,}
# print(d.get("name"))
# print(d.keys())
# print(d.values())
# print(d.items())
d.update({111:222,555:333})
print(d)

# for i,j in {"name":"bharath","age":24,}.items():
#     print(i,j)

# set : it is a data type, it didn't allow duplicates.
'''
add()
update()
pop()
remove()
'''

# s={1,1,2,2,3,44,55,66,'bharath'}
# print(s)

# s={1,1,2,2,3,44,55,66}
# s.add(123)
# s.update({15,23,35,41})
# s.pop()
# s.remove(55)
# print(s)

'''
union()
intersection()
difference
issubset
issuperset
'''
# set1={1,2,3,4,5,6}
# set2={4,5,6}
# print(set1.union(set2))         # union is nothing but it prints all elements in aset1 and set2
# print(set1.intersection(set2))  # intersection is it prints common elements in set1 and set2.
# print(set1.difference(set2))    # difference is it prints the set1 elements only and it will delete common elements.
# print(set1.issuperset(set2))    # superset is in set1 and set2 elements are same then it is true nor false.
# print(set2.issubset(set2))      # subset means which are the elements are in set2 same as in set1 is called subset.

# for i in {1,2,3,4}:
#     print(i)

# class Father:
#     def display(self):
#         print("this is father class")
# class Mother:
#     def display1(self):
#         print("this is mother class")
# class Child(Father,Mother):
#     def display2(self):
#         print("this is child class")
        
# obj=Child()
# obj.display2()
# obj.display1()
# obj.display()

# def even_odd (input):
#     if input%2==0:
#         return ("even num")
#     else:
#         return ("odd num")
# result=even_odd(7)
# print(result)

# def is_prime(input):
#     for i in range(2,input):
#         if input%i==0:
#             return ("it is not prime number")
#         else:
#             return("it is a prime number")
# num=int(input ("enter the number :"))
# result=is_prime(num)
# print(result)

# def factorial(num):
#     factorial=1
#     if num<0:
#         return ("factorial cannot be 0")
#     elif num==0:
#         return ("factorial of 0 is 1")
#     else:
#         for i in range(1,num+1):
#             factorial=factorial*i
#         return("factorial of the number is:",factorial)
# num=int(input("enterr the number"))
# result=factorial(num)
# print(result)

# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print("factorial cannot be zero")
# elif num==0:
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
# print("the factorial of the number is",factorial)

# num =int(input("enter the number:"))
# for i in range(2,num):
#     if (num%i)==0:
#         print("it is not a prime num")
#         break
# else:
#     print("it is prime number")

# rows=int(input("enter the number of rows:"))
# for i in range (1,rows+1):
#     for j in range(rows-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end=" ")
#     print()

a="bharath"
rev=""
for i in a:
    rev=i+rev
print(rev)




