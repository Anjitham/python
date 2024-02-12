

#Single level inheritance
# class Parent:
#     def mobile(self):
#         print("Redmi note 12")


# class Child(Parent):  #child inherit the properties from parent
#     pass


# ch=Child()
# ch.mobile()

#Multilevel inheritance

# class Parent1:
#     def m1(self):
#         print("inside parent m1 method")

# class Parent2(Parent1):
#     def m2(self):
#         print("inside parent 2 m2 method")

# class Child(Parent2):
#     def c(self):
#         print("inside child c method")

# ch=Child()
# ch.c()

# ch.m2()
# ch.m1()

## multiple level inheritance
class P1:
    def m1(self):
        print("Inside P1")

class P2:
    def m2(self):
        print("inside P2")

class child(P1,P2):
    pass

ch=child()
ch.m1()
ch.m2()

## multiple level inheritance---order of inheritance
class P1:
    def m1(self):
        print("Inside P1")

class P2:
    def m1(self):
        print("inside P2")

class child(P2,P1):
    pass

ch=child()
ch.m1()
