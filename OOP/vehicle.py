class  Parent:

    def properties(self):
        self.vehicles=["Audi","BMW"]
        return self.vehicles
    
class Child(Parent):
    def properties(self):
        self.context=super().properties()
        self.context.append("Porche")
        return self.context
c=Child()
print(c.properties())
