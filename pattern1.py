#     *
#    * *
#   * * *
#  * * * *
# num=1
# colum=12
# while colum>num:
#     print(" "*colum ," * "*num)
#     num=num+1
#     colum=colum-1


# * * * *
#  * * *
#   * *
#    *

num=int(input("enter a number :"))
row=0
num1=num
while row<=num1:
    print(" "*row," * "*num)
    num-=1
    row+=1