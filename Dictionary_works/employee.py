employee={"id":1000,"name":"hari","department":"developer"}

employee.update({"department":"senior developer"})
print(employee)

print("salary" in employee)


if "salary" not in employee:
    # employee["salary"]=45000
    employee.update({"salary":45000})
else:
    employee["salary"]+=10000
print(employee)