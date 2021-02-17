a=int(input("enter the number"))
b=int(input("enter the number"))
while a%b!=0:
    r=a%b
    a=b
    b=r
    print("HCF is",b)


# p = x = 20
# q = y = 24
# while x != y:
#   if x > y:
#     x = x - y
#   else:
#     y = y - x

# print("HCF of", p, "and", q, "is:", x)    