class Student():
    rollno:int
    name:str
    stream:str

#instance variable will have self infront of it 
# initializing instance variable--constructer
# java,c++ constructer name will be same as class,js--constructor()
# python __init__

    # def __init__
    def set_student(self,id,name,stream): #initializing instance variable
        self.rollno=id
        self.name=name
        self.stream=stream

    def display_student(self):
        print(self.rollno,self.name,self.stream)
# automatically invokes while object creation
stu1=Student()
stu1.set_student(1,"Anu","CS")
stu2=Student()
stu2.set_student(2,"bini","EC")

stu1.display_student()
stu2.display_student()

print("my name is {}".format(stu1.name))

