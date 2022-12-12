a=int(input("enter a number"))
fact=1
i=1
for i in range(i,a+1):
    fact=fact*i
print("factorial is",fact)



import math
a=int(input("enter a number"))
print(math.factorial(a))


def calc_factorial(x):
    if x==1:
        return 1
    else:
        return(x*calc_factorial(x-1))
num=int(input("enter a number"))
print("the factorial is",calc_factorial(num))