student={"Rollnumber":1,"name":"Anu","Branch":"CSE","College":"GECW"}
print(student)
print(student["Rollnumber"])
print(student.get("Rollnumber"))
print(student["College"])
student["Branch"]="ECE"
print(student)


num={"a":1,"b":9,"c":8,"d":2}
num_sorted=sorted(num,key=lambda v:num.get(v))
print(num_sorted)
