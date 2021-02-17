num=int(input("enter a number :"))
reverse=0
while num>0:
    rem=num%10
    reverse=(reverse*10)+rem
    num=num//10
print(reverse)



#last digit is always zero

num=int(input("enter a number :"))
reverse=0
while num>1:
    rem=num%10
    reverse=(reverse*10)+rem
    num=num//10
print(reverse*10)


