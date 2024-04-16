class Calculator:
    def add(self,n1,n2):
        return n1+n2

    def add(self,n1,n2,n3):
        return n1+n2+n3

    def add(self,n1,n2,n3,n4):
        return n1+n2+n3+n4

op=Calculator()
print(op.add(1,2,3,4))

# no method overloading in python