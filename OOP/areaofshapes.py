class Shape:
    name:str

    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name
    
class Rectangle(Shape):
    l:int
    b:int

    def __init__(self, name,l,b):
        super().__init__(name)
        self.l=l
        self.b=b

    def area(self):
        res=self.l*self.b
        print(res)

class Circle(Shape):
    r:int

    def __init__(self, name,r):
        super().__init__(name)
        self.r=r


    def area(self):
        res=3.14*self.r**2
        print(res)

c_obj=Circle("Circle",5)
c_obj.area()

r_obj=Rectangle("Rectangle",4,2)
r_obj.area()