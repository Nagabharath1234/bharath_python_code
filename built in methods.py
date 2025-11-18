# a=[1,2,3,4,5]
# del(a[3])
# print(a)

# a=[1,2,3,4,5]
# res=(a.pop(3))
# print(a)

# a="hello world"
# print(a.upper())

# a="HELLO WORLD"
# print(a.lower())

a="bharath learning python"
print(a.title())

# str="bharath"
# print(str.upper())

# str="BHARATH"
# print(str.lower())

# str="bharath"
# print(str.capitalize())

# str= "bharath learning python"
# print(str.title())

# str="BHarAtH"
# print(str.lower())

# str="bharath"
# print(str[:3].upper() + str[3:])

# str="bharath learning python"
# print(str.split())

# str="bharath"
# print(str.split())

# str="BHARATH"
# print(str.swapcase())

# str="Hello World"
# print(str.removeprefix("Hello"))

# str="naga bharath"
# print(str.removesuffix("bharath"))

# str="hello world"
# print(str.replace("world","bharath"))

# str='bharath'
# res=[]
# for i,c in enumerate (str):
#     if i%2==0: 
#         res.append (c.lower())
#     else:
#         res.append (c.upper())
# print("".join(res))

# str="  bharath   "
# print(str.strip())

# str="****bharath****"
# print(str.strip("*"))

# str="banana"
# print(str.replace("a","o"))

# str="apple"
# print(str.replace("a","i"))

# str="{} scored {} points"
# print(str.format("bharath",100))

# s="resto"
# s+="bar"
# print(s)

# a="hello"
# b="bharath"
# c=a+" "+b
# print(c)

# list=[0,1,2,3,4,5,6,7,8]
# print(sum(list))
# print(len(list))
# print(max(list))
# print(min(list))

# a="bharath"
# print(a.count("a"))

# python = "python language"
# print(python.endswith("l"))
# print(python.startswith("l"))

# python = "python language"
# print(python.index('language'))
# print(python.find('python'))

# python = "python language"
# print(python.count('g'))

# python = "python language"
# print(python.endswith("e"))

# python = "python language"
# print(python.startswith("p"))

'''list built in methods'''
# list=['bharath','ravi','ramu','raju']
# result=list.append("manoj")
# print(list)

# list=['bharath',1,2,3,'ravi']
# result=list.extend(['manoj','abhi','ashok'])
# print(list)

# list=['naveen',1,2,3,5,8]
# list.insert(4,'bharath')
# print(list)

# list=[1,2,3,4,5]
# a=list.index(2)
# list[a]='bharath'
# print(list)

# list=[1,2,3,5,6,7,8,9]
# list.remove(5)
# print(list)

# list=[1,3,3,4,5,6]
# list.pop(1)
# print(list)

# list=[1,2,3,4,5,6,7,8,9]
# del(list[2])
# print(list)

# list=['bharath',1,2,3,6,7,4,4,5,'naveen']
# result=list.index(7)
# list[result]='bharath'
# print(list)

# list=[1,2,3,4,5,6,7,8,9]
# result=list.count(7)
# # print(result)

# a='bharath'
# char=list(a)
# char.reverse()
# print(char)

# list=['banana','cherry','apple']
# list.sort()
# print(list)

'''dictionary builtin methods'''
# dict={'name':'bharath','age':24}
# dict.update({'city':'bangalore'})
# print(dict)

# dict={'name':'bharath','city':'bangalore'}
# dict.pop('city')
# print(dict) 

# dict1={1:'hello',2:'how',3:'are',4:'you'}
# res=dict1.get(3)
# print(res)

# dict1[6]='bharath'
# print(dict1)

# key1=3
# res=key1 in dict1
# print(res)

# dict1={1:'hello',2:'how',3:'are',4:'you'}
# key=9
# res=key in dict1
# print(res)

# dict1={1:'hello',2:'how',3:'are',4:'you'}
# key=9
# res=key not in dict1
# print(res)

# dict1={1:'hello',2:'how',3:'are',4:'you'}
# dict1[1]='hii'
# print(dict1)

# dict1={1:'hello',2:'how',3:'are',4:'you'}
# res=list(dict1.keys())
# print(res)

# dict1={1:'hello',2:'how',3:'are',4:'you'}
# res=list(dict1.values())
# print(res)

# dict1={1:'hello',2:'how',3:'are',4:'you'}
# res=dict1.values()
# print(res)

# dict1={1:'hello',2:'how',3:'are',4:'you'}
# del dict1[2]
# print(dict1)

# dict1={1:'hello',2:'how',3:'are',4:'you'}
# for key,value in dict1.items():
#     print(key,value)

# from collections import counter
# str='hello how are you'
# res=counter(str.split())
# print(res)

# str='hello how are you'
# res=str.split()
# print(res)

# str='hello how are you'
# res=str.count('h')
# print(res)

# str='bharath'
# res=set(str)
# dict1={}
# for i in res:
#     dict1[i]=str.count(i)    
# print(dict1)

# str="the cat and the dog"
# res=str.split()
# set=set(res)
# a={}
# for i in set:
#     a[i]=res.count(i)
# print(a)

# string1="hello how are you"
# list1=string1.split(" ")
# a={}
# for i in list1:
#     a[i]=i[0]+i[-1]
# print(a)

# dict1={'name':'bharath','age':24}
# dict2={}
# for key,value in dict1.items():
#     dict2[key.capitalize()]=value
# print(dict2)

# data={'item1':'ball','item2':'bat','item3':'cap'}
# result=[]
# for key in data:
#     value=data[key]
#     if 'a' in value:
#         result.append(key)
# print(result)

'''write the python code to print only end with the vowels is true if not false in the list'''
# list="hello how are you"
# s=tuple("aeiou")
# for i in list.split():
#     if i.lower().endswith(s):
#         print(i,"true")
#     else:
#         print(i,"false")

# list=[1,2,2,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9]
# freq={}
# for i in list:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print("the freq of list is :",freq)

# s="banana"
# freq={}
# for i in s:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print("the frequency of string is:",freq)

# s="education"
# vowels="aeiou"
# consonents=0
# count=0
# for i in s:
#     if i in vowels:
#         count=count+1
#     else:
#         consonents+=1
# print("the vowels are",count)
# print("the consonents are",consonents)

# a='bharath'
# vowels=('aeiou')
# consonents=0
# count=0
# for i in a:
#     if i in vowels:
#         count=count+1
#     else:
#         consonents+=1
# print(f"the vowels are:",count)
# print(f"the consonenets are:",consonents)

'''swap the dict '''
# dict={'1':'a','2':'b','3':'c','4':'d'}
# swaped={v:k for k, v in dict.items()}
# print(swaped)

# dict={'a':'bharath','b':'manoj','c':'rohit'}
# swaped={v:k for k,v in dict.items()}
# print(swaped)

'''extract the first repeating character with position'''

# str="bharath"
# a={}
# for i, char in enumerate(str):
#     if char in a:
#         print(f"first repeating character:'{char}'at the position")
#         break
#     a[char]=i
# else:
#     print(f"no repeating character:'{char}' at the position")

# str='balaji'
# a={}
# for i , char in enumerate(str):
#     if i in a:
#         print(f"repeating char is:'{char}' at the position")
#         break
#     a[char]=i
# else:
#     print(f"no repeating char,'{char}' at the position")
        

'''create a dict from two lists (keys:letters,values:words)'''
'''output ={'a':'apple','b':'banana','c':'orange'}'''

# letters=['a','b','c']
# words=['apple','banana','orange']
# result=dict(zip(letters,words))
# print(result)

# class Person:
#     def display(self):
#         print("it is person class")
# class Student(Person):
#     def func(self):
#         print("this is student")
# obj=Student()
# obj.func()
# obj.display()

# a="madam"
# if a==a[::-1]:
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome")

# num=5

# for i in range(2,num):
#     if (num%i)==0:
#         print("it is not a prime num")
#         break
# else:
#     print("it is a prime num")

# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print("factorial cannot be negative")
# elif num==0:
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
# print("factorial of the number is:",factorial)

# num=int(input("enter the number:"))
# if num%2==0:
#     print("it is even number")
# else:
#     print("it is odd num")

# list=[1,2,3,4,5,6,7,8,9,0]
# for i in list:
#     if i%2!=0:
#        print(i)

# list=[1,2,2,3,3,4,4,4,5,5,5,6,6,7,7,8,8,9,9,9]
# a={}
# for i in list:
#     if i in a:
#         a[i]+=1
#     else:
#         a[i]=1
# print("the frequency of the number is:",a)

# s="helloworld"
# print (s[:5].upper()+s[5:])

# a,*b,c=1,2,3,4,5,6,7
# print(*b)

# s=['apple','banana','cherry']
# res=iter(s)
# print(next(res))

# def decorator(func):
#     def wrapper():
#         print("it is before execution")
#         func()
#         print("it is after execution")
#     return wrapper()
# @decorator
# def function():
#     print("hello!")
# function
    
# def generator(a):
#     count=1
#     while count<a:
#         yield count
#         count=count+1
# res=generator(4)
# print(next(res))
# print(next(res))

# class Student:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def display(self):
#         print(self.a+self.b)
# obj=Student(3,5)
# obj.display()

# def funct(*a):
#     return tuple(x for sub in a for x in sub)
# print(funct((3,6),(5,6)))

# def display(**a):
#     return (a)
# print (display(name='bharath',age=24))

# s=lambda x,y: x*y
# print(s(3,7))

# num=[1,2,3,4,5,6,7]
# res=list(map(lambda x:x*2,num))
# print(res)

# num=[1,2,3,4,5]
# res=list(filter(lambda x:x%2==0,num))
# print(res)

# a="bharath" 
# res=" ".join(
#     c.lower() if i%2 else c.upper()
#     for i,c in enumerate(a)
# )
# print(res)

# a="bharath"
# result=" "
# for i,c in enumerate(a):
#     if i%2==0:
#         result+=c.upper()
#     else:
#         result+=c.lower()
# print(result)

# class Student:
#     def __init__(self,name,age,pages):
#         self.name=name
#         self.age=age
#         self.pages=pages
       
        
#     def __str__(self):
#         return(f"my name is {self.name} my age is {self.age}")
    
#     def __len__(self):
#         return self.pages
  
# obj=Student('bharath',24,300)
# print(obj)
# print(len(obj))

# a="bharath"
# res=" "
# for i,c in enumerate(a):
#     if i%2==0:
#         res+=c.upper()
#     else:
#         res+=c.lower()
# print(res)

# list1={1,4,7,0,3,6,8,2,6,9}
# list2={11,22,13}
# res=set(list1).union(list2)
# print(res)

# list1={1,2,3,4,5,7}
# list2={5,6,7,8,9,5}
# res=set(list1).intersection(list2)
# print(res)

# list1={1,2,3,4,5,6}
# list2={7,8,9,10}
# res=set(list1).difference(list2)
# print(res)

# list1={1,2,3,4,5}
# list2={1,2,3,4,5,6}
# res=set(list1).issubset(list2)
# print(res)

# list1={1,2,3,4,5,6,7}
# list2={1,2,3,4,5}
# res=set(list1).issuperset(list2)
# print(res)

# def fibonacci(input):
#     if input<=0:
#         return[]
#     if input==1:
#         return[0]
#     if input==2:
#         return[0,1]
#     seq=fibonacci(input-1)
#     seq.append(seq[-1]+seq[-2])
#     return seq
# res=fibonacci(8)
# print(res)
        
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
# res=fibonacci(12)
# print(res)
