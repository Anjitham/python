class Employee:
    id=int
    name=str
    department=str
    salary=int

    def set_emp(self,id,name,dept,sal):
        self.id=id
        self.name=name
        self.department=dept
        self.salary=sal

    def display_emp(self):
        print(self.id,self.name,self.department,self.salary)

emp1=Employee()
emp1.set_emp(1234,"ram","hr",50000)

emp2=Employee()
emp2.set_emp(5678,"Anu","qa",55000)

emp1.display_emp()
emp2.display_emp()
