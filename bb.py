# a="bharath"
# print(a.upper())

# a="BHARATH"
# print(a.lower())/

# a="bharath"
# print(a.capitalize())

# a="bharath learning python"
# print(a.title())

# a="     bharath"
# print(a.lstrip())

# print(a.rstrip())

# a="bharath"
# print(a.split())

# a="naga bharath"
# print(a.removesuffix("bharath"))

# a="naga bharath"
# print(a.removeprefix("naga"))

# a="bharath"
# print(a.replace("a","o"))

# a="{} scored {} points"
# print(a.format("bharath",100))

# a="bharath..."
# print(a.rstrip("."))

# a="bharath"
# print(a[::-1])

# a="bharath"
# rev=""
# for i in a:
#     rev=i+rev
# print(rev)
    
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
for i in range(2,num):
    if (i%num)==0:
        print(f"it is  not prime num")
        break
else:
    print(f"it is a prime num")