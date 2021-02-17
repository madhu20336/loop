num1=int(input("Enter the 1st number :"))
num2=int(input("Enter the 2nd number : "))
if num1>num2:
    max=num1
    print("the maximum num",max)
else :
    max=num2
    print("the maximum num",max)
if num1<num2:
    min=num1
    print("the minimum num",min)
else :
    min=num2
    print("the minimum num",min)
while max%min!=0:
    rem=max%min
    max=min
    min=rem
print("HCf is",min)