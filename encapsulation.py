'''
Encapsulation: Wrapping up of methods and variables in a single unit is called encapsulation.
public
private__
protected_
'''
# class Demo():
#     __a=2  #private double underscore
#     _b=4   # protected single underscore
#     print(__a)
#     print(_b)

# class Demo2(Demo):
#     print(_b)

# class Demo():
#     def __init__(self,a,b):
#         self.__a=a
#         self._b=b
# class Demo2(Demo):
#     def output(self):
#         print(self._b)
# d=Demo(3,4)
# d.output()

class Student:
    def __init__(self,a,b):
        self.__a=a
        self._b=b
class Person(Student):
    def greet(self):
        print(self._b)
obj=Person(3,5)
obj.greet()

# class Student:
#     def __init__(self,a,b):
#         self.__a=a
#         self._b=b
# class Student2(Student):
#     def output(self):
#         print(self._b)
# d=Student2(3,4)
# d.output()



# Data abstaraction : it is defined by hiding of information.
#  it hides the internal data and it shows only functionalities and hides implementation.

# list = [1,2,3,4,5]
# print(len(list))


        
    
