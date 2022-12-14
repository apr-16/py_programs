import calculator
print("1.Addition\n2.Difference\n3.Product\n4.Division\n")
choice=int(input("Select your choice\n"))
a=int(input("enter first number\n"))
b=int(input("enter second number\n"))
if(choice==1):
    print(a,"+",b,"=",calculator.add(a,b))
elif(choice==2):
    print(a,"-",b,"=",calculator.sub(a,b))
elif(choice==3):
    print(a,"*",b,"=",calculator.pro(a,b))
elif(choice==4):
    print(a,"/",b,"=",calculator.div(a,b))

