class Mobile:
    name:str
    brand:str
    display:str
    price:int

    def __init__(self,name,brand,display,price):
        self.name=name
        self.brand=brand
        self.display=display
        self.price=price

    def display_mobile(self):
        print(self.name,self.brand,self.display,self.price)

    def __str__(self): #for string representation of object
        return self.name


obj=Mobile("13","I Phone",6,56000)
obj.display_mobile()
print(obj)