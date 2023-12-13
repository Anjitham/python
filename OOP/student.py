class Student():
    rollno:int
    name:str
    stream:str

    def set_student(self,id,name,stream):
        self.rollno=id
        self.name=name
        self.stream=stream

    def display_student(self):
        print(self.rollno,self.name,self.stream)

stu1=Student()
stu1.set_student(1,"Anu","CS")
stu2=Student()
stu2.set_student(2,"bini","EC")

stu1.display_student()
stu2.display_student()

print(stu1)

