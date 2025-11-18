# control statements are three types
#1.conditional statements
#if,elif,else,nested if.
'''if condition is used to execute the code based on the condition
elif condition is used to execute the multiple conditions
else condition is used to none of the condition is met'''

# age =18
# if age > 18:
#     print("adult")
# elif age<18:
#     print("minor")
# else:
#     print("become adult")

# if False:
#     print("me if")
# elif True:
#     print("me elif")
# else:
#     print("me else")

# if False:
#     print("outer if")
#     if True:
#         print("inner if")
#     else:
#         print("outer else")
# else:
#     print("inner else")

# # conditional statements with logical operator.
# age =18
# if age>18 or age==18: 
#     print("you can vote")
# else:
#     print("wait")



#2.looping statements
#for, while, nestedloop
'''for loop is used to iterate over the sequence
while loop is used to repeats the code as long as the specified condition is true
nested loop is used to write loop in loop '''

# rows=int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# for i in range (0,10,2):
#     print(i)

# rows=int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(rows-i):
#         print("*",end="")
#     print()

# rows=int(input("enter the number of rows:"))
# for i in range(rows):
#     for j in range(i):
#         print(" ",end="")
#     for  k in range(2*(rows-i)-1):
#         print("*",end="")
#     print()

rows=int(input("enter the number of rows:"))
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    print()

# a=[4,55,666,778,90]
# for i in a:
#     print(i)

# a= "bharath"
# for i in a:
#     print(i)

# while True:
#     print('hi')

# bharath=5
# while bharath<10:
#     print("hi",bharath)
#     bharath+=1

# k=10 
# while k<20:
#     print(k)
#     k+=1

# The code `for i in range(0,10):` is creating a loop that iterates over the range of numbers from 0
# to 9. For each value of `i` in this range, the inner loop `for j in range(0,100):` is executed. This
# inner loop iterates over the range of numbers from 0 to 99.
# for i in range(0,10): # i=0
#     for j in range(0,100): #j=100
#         print(i+j)


#3.jumping statements
#break,continue,pass

'''break is used to terminates from the iteration
continue is used to skips the current iteration from the loop
pass it ignores'''

#break : it is used to terminate the iteration of a loop.
# for i in "python":
#     if i == 'h':
#         break
#     print(i)

#continue: it is used to skips the current iteration from the loop.
# The code `for i in "python": if i == 'y': continue print(i)` is iterating over each character in the
# string "python". If the character is 'y', it will skip that iteration using the `continue`
# statement. For all other characters, it will print the character.
# for i in "python":
#     if i == 'y':
#         continue
#     print(i)

#pass: it ignores the loop of iteration.
# if True:
#     pass