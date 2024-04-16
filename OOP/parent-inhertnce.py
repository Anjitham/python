class User:
    name:str
    age:str
    gender:str

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def __str__(self):
        return self.name

    
class Student(User):
    rollno:str
    course:str

    def __init__(self, name, age, gender,rollno,course):
        super().__init__(name, age, gender)
        self.rollno=rollno
        self.course=course
    
    # def __str__(self):
    #     return self.name
    

class Faculty(User):
    fac_id:str
    dept:str

    def __init__(self, name, age, gender,fac_id,dept):
        super().__init__(name, age, gender)
        self.fac_id=fac_id
        self.dept=dept

    # def __str__(self):
    #     return self.name,self.dept
    

stud=Student("Anu",23,"F",1,"CSE")
print(stud)

