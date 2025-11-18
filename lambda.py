'''a company decided to give bonus of 5% to employee if his year of service is 5 years. 
ask user for salary and year of service and print the net bonus amount'''
# salary=int(input("enter the salary:"))
# year_of_service=float(input("enter the year o f service:"))
# if year_of_service>=7:
#     bonus=salary*0.05
#     print("you are eligible for bonus amount")
#     print("bonus amount is ",bonus)
# else:
#     print("you are not eligible for bonus")

'''write a python code to print all negative elements in a list'''
# list=[1,2,-3,-4,-56,-67,89,67,78,67,56,45]
# for i in list:
#     if i<0:
#         print(i)

'''write a python to find sum of all elements in a list'''
# list=[1,2,-3,-4,-56,-67,89,67,78,67,56,45]
# sum=0
# for i in list:
#     sum=sum+i
#     print(sum)


'''write a python code to find minimum and maximum element in a list''' 
# list=[1,2,-3,-4,-56,-67,89,67,78,67,56,45]
# a=(max(list))
# print(a)

# list=[1,2,-3,-4,-56,-67,89,67,78,67,56,45]
# a=(min(list))
# print(a)

'''write a python code to find second largest element in a list'''
# list=[1,2,-3,-4,-56,-67,89,67,78,67,56,45]
# list.sort(reverse=True)
# print(list[1])

'''write a python code to count total number of even and odd elements in a list'''
# list=[1,2,-3,-4,-56,-67,89,67,78,67,56,45]
# even=0
# odd=0
# for i in list:
#     if i %2==0:
#         even=even+1
#     else:
#         odd=odd+1
# print(even)
# print(odd)

'''write the python code to get the frequency of the elements in a list'''
# list=[1,2,-3,-4,-56,-67,89,67,78,67,56,45]
# a={}
# for i in list:
#     if i in a:
#         a[i]+1
#     else:
#         a[i]=1
# print("frequency in a list",a)

'''give the example of a lambda function to do addition'''
# s=lambda x,y:x+y
# print (s(1,2))

# a=lambda a,b:a*b
# print(a(3,4))

'''Remove Duplicates from a List'''
# def remove(input_list):
#     return list(set(input_list))
# input_list=[1,2,2,3,3,4,5,6,6,7,7,8]
# result=remove(input_list)
# print(result)

# list=[1,2,2,3,3,4,4,5,6,7,7,8,8,9]
# print(set(list))


'''Intersection of Two Lists
Given two lists, return a list of elements common to both.'''
# list1=[1,2,3,4,5,6]
# list2=[7,8,9,2,3]
# print (set(list1)&(set(list2)))

# def common(list1,list2):
#     return list(set(list1)&set(list2))
# list1=[1,2,3,4,5,6,7]
# list2=[5,6,7,8,9]
# result=common(list1,list2)
# print(result)

'''Sort a List of Numbers
Use Python’s built-in sorted() or implement your own sorting logic. '''
# my_list=[1,5,4,7,8,2,4,3,6]
# sorted_list=(sorted(my_list))
# print(sorted_list)

# def sorted_list(input_list):
#     return sorted(input_list)
# list=[2,5,4,6,9,8,7,1]
# a=sorted_list(list)
# print(a)

'''Sum of Digits of a Number
Calculate the sum of all digits in a given integer.''' 
# int=1,2,3,4,5
# print(sum(int))

# def sum_of_all(input_list):
#     return sum(input_list)
# input_list=[1,2,3,4,5,6]
# result=sum_of_all(input_list)
# print(result)

'''prime number'''
# def prime(input):
#     if input<=1:
#         return False
#     for i in range(2,input(input**0.5)+1):
#         if (input%i)==0:
#             return True
# num=34
# print(f"is_prime:,{(num)}")



'''List reversal — reverse a list without slicing.'''
# list=[1,2,3,4,5,6,7,8,9]
# list.reverse()
# print(list)
    
'''List reversal — reverse a list without slicing.'''
# list=[1,2,3,4,5,6,7]
# reversed=[]
# for i in list:
#     reversed.insert(0,i)
# print(reversed)

'''Find second largest number — handle duplicates.'''
# list=[1,2,3,4,5,5,6,7,8,9]
# result=(list.sort(reverse=True))
# print(list[1])

'''remove duplicates in a list'''
# def remove(input_list):
#     return list(set(input_list))
# input_list=[1,2,3,4,5,5,6,7]
# a=remove(input_list)
# print(a)

# list=[1,2,3,3,4,4,5,6]
# a=(set(list))
# print(a)

'''Count frequency of elements in a list.'''
# my_list=[1,1,1,2,2,2,3,3,4,4,5,5,6,6,6,7,7,7,8,8,9,9,9]
# frequency={}
# for item in my_list:
#     if item in frequency:
#          frequency[item]+=1
#     else:
#          frequency[item]=1
# print (frequency)

'''Merge two lists and remove duplicates.'''
# list1=[1,2,3,4,5,6]
# list2=[5,6,7,8,9,3]
# merged_list=list(set(list1+list2))
# print (merged_list)

'''Check if two strings are anagrams.'''
# str1='listen'
# str2='silent'
# str1=str1.replace(" ","").lower()
# str2=str2.replace(" ","").lower()
# sorted_str1=sorted(str1)
# sorted_str2=sorted(str2)
# if sorted_str1==sorted_str2:
#     print(f"'{str1}'and '{str2}' are anagrams")
# else:
#     print(f"'{str1}'and '{str2}' are anagrams")

'''Remove vowels from a string — custom function '''
# string_input='bharath'
# vowels="aeiouAEIOU"
# result=""
# for char in string_input:
#     if char not in vowels:
#         result+=char
# print(f"original string is:",string_input)
# print(f"string without vowels:",result)

'''Reverse a list with slicing and manual.'''
# list=[1,2,3,4,5,6,7,8,9]
# reversed_list=list[::-1]
# print(f"original list is:",list)
# print(f"reversed from slicing is :",reversed_list)
        
'''Sort a list of tuples by second element — via sorted() + lambda '''
# list=[(1,4),(3,1),(5,2),(2,6),(5,7),(9,8)]
# sorted_list=sorted(list,key=lambda x:x[1])
# print(f"original list is:",list)
# print(f"sorted list of tuples:",sorted_list)

'''List comprehension — generate even numbers between 1 and 10 .'''
# even_numbers=[num for num in range(1,11)if num%2==0]
# print(even_numbers)
    
'''Merge two dictionaries — using update() or {**dict1, **dict2} '''
# dict1={'bharath':24,'ravi':30}
# dict2={'raju':35}
# dict1.update(dict2)
# print(dict1)

'''Check key existence in dict — using in.'''
# dict={'bharath':24,'ravi':27,'raju':30}
# name='ramu'
# if name in dict:
#     print("it is present in dict")
# else:
#     print("it is not present in dict")

'''Map & filter usage — use map() to double values, filter() for >10.'''
# numbers=[1,2,3,4,5,6,7]
# listed_values=map(lambda x:x*2,numbers)
# filtered_values=filter(lambda x:x>10,listed_values)
# print(list(filtered_values))

'''Lambda sort — sort list via key= lambda.'''
# list=[(1,3),(3,4),(7,6),(6,9),(9,8),(10,9)]
# sorted_list=sorted(list,key=lambda x:x[1])
# print(sorted_list)

'''Use of nonlocal inside nested functions '''
# def outer():
#     x = 10
#     def inner():
#         x=+1 
#         print("Inner x:", x)
#     inner()
#     print("Outer x:", x)

# outer()

'''Dictionary comprehension — invert a dictionary.'''
# dict={'a':1,'b':5,'c':4}
# inverted_dict={value:key for key,value in dict.items()}
# print(inverted_dict)

'''Exception handling — catch zero division or conversion errors.'''
# try:
#     num=int(input("enter the number:"))
#     result=10/num
#     print("result:",result)
# except ZeroDivisionError:
#     print("Error:you can't divide by zero")
# except ValueError:
#     print("Error:invalid input")

'''Use of zip() — combine two lists element-wise '''
# list1=['a','b','c']
# list2=[1,2,3]
# combined=zip(list1,list2)
# print (list(combined))

'''given a list of integers, replace all even numbers with 0'''
# list=[12,5,8,3,7,6]
# result=[0 if i%2==0 else i for i in list ]
# print(result)
    
'''print only even numbers in list comprehension method'''
# list=[12,34,56,78,90,76,45]
# result=[x for x in list if x%2==0]
# print(result)

'''write a python code to print only odd numbers use list comprehension method'''
# list=[12,34,56,78,90,76,45]
# result=[x for x in list if x%2!=0]
# print(result)

# list=[12,34,56,78,90,76,45]
# result=[0 if i%2!=0 else i for i in list]
# print(result)

'''write a python code to print list of squares for even numbers only'''
# list=[2,3,4,5,6]
# result=[x**2 for x in list if x%2==0]
# print(result)

'''write a python code to print merge two lists and remove duplicates from the final lists'''
# list1=[1,2,3]
# list2=[3,4,5]
# final_list=list(set(list1+list2))
# print(final_list)

'''write a python code to print remove all the negative numbers in a list'''
# list=[-5,3,-2,8,0,-1,4]
# result=[x for x in list if x>=0]
# print(sorted(result))

'''write a python code to print second largest number in a list'''
# lists=[12,45,2,41,31,10]
# result=list(set(lists))
# result.sort(reverse=True)
# second_largest=(result[1])
# print(second_largest)

# lists=[12,45,2,41,31,10]
# numb=list(set(lists))
# numb.sort(reverse=True)
# result=numb[1]
# print(result)

# def greet(name,age):
#     return (f"hii {name}, you are {age} years old")
# print (greet('bharath',24))

'''count vowels in a string'''
# a="OpenAI"
# vowels="AEIOUaeiou"
# count=0
# for char in a:
#     if char in vowels:
#         count=count+1
# print("the vowels are :",count)

'''check if a string are palindrome'''
# a="madam"
# if (a==a[::-1]):
#     print("palindrome")
# else:
#     print("not palidrome")
    
'''convert string to upper case'''
# a="python"
# b=a.upper()
# print(b)

'''replace all spaces with hypens'''
# a="data science is fun"
# b=a.replace(" ","-")
# print(b)

'''remove all special character from a string'''
# a="he@ll#o! w$or^l*d*"
# b=""
# for i in a:
#     if i.isalnum() or i==" ":
#         b+=i
# print(b)

'''capitalize the first letter of each word in a string'''
# a="machine learning with python"
# b=a.title()
# print(b)

# a="helloworld"
# result=(a[:5].upper()+a[5:])
# print (result)

# str="bHaRatH"
# result=(str.upper())
# print(result)

# a="machine learning with python"
# b=a.capitalize()
# print(b)

# a,*b,c=[1,2,3,4,5]
# print(*b)

# list=[1,2,2,3,3,3,4,4,4]
# a={}
# for i in list:
#     if i in a:
#         a[i]+=1
#     else:
#         a[i]=1
# print(f"count of list is:",a)

