num=int(input("enter a number :"))
row=1
while row<num:
    col=1
    while col<num:
        print("*",end="")
        col+=1
    print()
    row+=1