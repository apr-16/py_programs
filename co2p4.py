from math import sqrt
n=int(input("enetr a number"))
if n<1000:
    print("invalid")
else:
    for i in range(1000,n):
        if sqrt(i)==int(sqrt(i)) and i%2==0:
            print(i)