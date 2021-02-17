num=int(input("enter a number :"))
b=num
a=1
sum=0
while a<num:
    if num%a==0:
        sum=sum+a
    a+=1
if sum==b:
    print(b,"is perfect number")
else:
    print(b,"is not perfect number")    