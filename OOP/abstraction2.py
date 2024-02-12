from abc import ABC,abstractmethod

class Car(ABC):

    @abstractmethod
    def __init__(self,name,brand,model):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Audi(Car):
    def __init__(self, name, brand, model):
        self.name=name
        self.brand=brand
        self.model=model

    def start(self):
        print("Audi start")

    def accelerate(self):
        print("Audi accelerates")

    def stop(self):
        print("Audi stops")


obj=Audi("Q3","Audi","2021")
obj.start()
