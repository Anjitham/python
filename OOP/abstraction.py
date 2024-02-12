from abc import ABC,abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def jump(self):
        pass

class Lion(Animal):
    def sound(self):
        print("Lion roars")

    def run(self):
        print ("Lion ran")

    def jump(self):
        print("Lion jumps")


class Dog(Animal):
    def sound(self):
        print("dog bark")

    def run(self):
        print ("dog ran")

    def jump(self):
        print ("dog jumps")

obj=Lion()
obj.sound()