
# Inverted right triangle
# ****
# ***
# **
# *
num=int(input("enter the star :"))
colum=1
while colum<=num:
    row=num
    while row>=colum:
        print("*",end="")
        row=row-1
    print()
    colum+=1
