num=int(input("enter a number :"))
sum=0
b=num
order=len(str(num))
while num>0:
    digit=num%10
    sum=sum+(digit**order)
    print(sum)
    num=num//10
if sum==b:
    print(b,'is armstrong number')
else:
    print(b,'is not armstrong number')