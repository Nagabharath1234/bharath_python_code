# def greet(**a):
#     return a
# res=greet(name='bharath',age=24)
# print(res)

# s=[1,2,3]
# res=list(map(lambda x:x*x,s))
# print(res)


# s=[1,2,3,4,5,6]
# res=list(filter(lambda x: x%2==0,s))
# print(res)

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"my name is {self.name} and my age is {self.age}")
class Person(Student):
    def __init__(self,name,age,salary,employee):
        super().__init__(name,age)
        self.salary=salary
        self.employee=employee
        print(f"my salary  is {self.salary} and iam {self.employee}")
        
obj=Person('bharath',24,25000,'engineer')

# str="abc"
# rev=" "
# for c in str:
#     rev=c+rev
# print(rev)