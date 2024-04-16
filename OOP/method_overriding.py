# polymorphism

class Parent:
    def mobile(self):
        print("redmi note 12")
    def vehicle(self):
        print("Audi")

class Child(Parent):
    # pass
    def mobile(self):
        print("i Phone 15")

ch=Child()
ch.mobile()
ch.vehicle()

# here mobile is overrided