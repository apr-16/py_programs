class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def peri(self):
        return 2*(self.length+self.breadth)
    def area(self):
        return self.length*self.breadth
    def com(self,obj2):
        try:
            if obj1.area()>obj2.area():
                print("Area of first rectangle is large")
            elif obj1.area()<obj2.area():
                print("Area of second rectangle is large")
            else:
                obj1.area()==obj2.area()
                print("Area is equal")
        except:
            print("use valid measurements")

    

l1=int(input("enter the length of first rectangle"))
b1=int(input("enter the breadth of first rectangle"))
l2=int(input("enter the length of second rectangle"))
b2=int(input("enter the breadth of second rectangle"))
obj1=rectangle(l1,b1)
obj2=rectangle(l2,b2)
print("Area of first rectangle",obj1.area())
print("Area of second rectangle",obj2.area())
obj1.com(obj2)

