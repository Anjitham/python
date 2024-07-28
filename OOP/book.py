class Book:
    name:str
    author:str
    pages:int
    price:int

    def __init__(self,name,author,pages,price):
        self.name=name
        self.author=author
        self.pages=pages
        self.price=price

    def display_book(self):
        print(self.name,self.author)

    def __str__(self): #for string representation of object
        return self.name


obj=Book("The kite runner","Khaled Hosseini",700,500)
obj.display_book()
# print(obj)