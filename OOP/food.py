class Cuisine:
    name:str

    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name
    
class Dish(Cuisine):
    dish_name=str
    ingredients:str
    price:str

    def __init__(self, name,dish_name,ingredients,price):
        super().__init__(name)
        self.dish_name=dish_name
        self.ingredients=ingredients
        self.price=price

        
food=Dish("Chinese","Noodles","Wheat noodles",150)
print(food,end=",")
print(food.dish_name)