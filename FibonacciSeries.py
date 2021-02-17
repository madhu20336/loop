num=int(input("enter a number :"))
a=0
b=1
sum=0
count=1
while count<=num:
    print(sum,'/n')
    count+=1
    a=b
    b=sum
    sum=a+b