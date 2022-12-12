a=[34,5,63,36,4
   ]
b=[55,12,63,78,1]
if(len(a)==len(b)):
    print("the length of the list are same")
else:
    printf("length of the list are not same")
sum=0
sam=0

for i in range(0,len(a)):
    
    sum=sum+a[i]
print("sum is",sum)
for i in range(0,len(b)):
     sam=sam+b[i]
print("sum is",sam)
if(sum==sam):
    print("The sum of list is equal")
else:
    print("not equal")
