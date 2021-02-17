 num=int(input("enter the number :"))
 a=1
# while a<=num:
#     if num==1 or num%2==0 or num%3==0 or num%5==0:
#         print(num,"is not prime number")
#         break
#     elif num==2:
#         print(num,"is prime number")
#         break
#     else:
#         print(num,"is prime number ")
#         break
#     a+=1

b=0
while a<=num:
    if num%1==0:
        print(a)
        b+=1
if b==2:
    print("it is prime number")
else:
    print("it is not prime number")
a+=1
