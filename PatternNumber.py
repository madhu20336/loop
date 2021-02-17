num=int(input("enter the number"))
row=0
while row<=num:
    col=row
    while col>0:
        print(col,end="")
        col-=1
    print()
    row+=1