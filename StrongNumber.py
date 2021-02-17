num=int(input("enter the number :"))
sum=0
digit=num
a=0
while num>0:
    a=num%10
    i=1
    b=1
    while i<=a:
        b=i*b
        i+=1
    sum=sum+b
    num=num//10
if digit==sum:
    print(digit,"is strong number")
else:
    print(digit,"is not strong number")    