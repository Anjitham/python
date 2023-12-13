students=[
    {"id":1,"name":"jhon","skills":["c","c++"],"exp":2,"qualification":"mca"},
    {"id":1,"name":"jain","skills":["python","js"],"exp":0,"qualification":"btec"},
    {"id":1,"name":"vijin","skills":["c","java","python"],"exp":4,"qualification":"mca"},
    {"id":1,"name":"tinu","skills":["r","java"],"exp":3,"qualification":"mtech"},
    {"id":1,"name":"roy","skills":["python","css","js"],"exp":0,"qualification":"bca"},
    {"id":1,"name":"vijil","skills":["js","r","css"],"exp":1,"qualification":"mtech"},
    {"id":1,"name":"ravi","skills":["java","python"],"exp":3,"qualification":"btec"},
    {"id":1,"name":"tom","skills":["java","css","r","sql"],"exp":4,"qualification":"bca"},
    {"id":1,"name":"ryan","skills":["c","css","python"],"exp":0,"qualification":"mca"},
]


# 1) total number of students
print("Total number of students:",len(students))

# 2) print name of all students

all_student_names=[stud.get("name") for stud in students]
print("name of students:",all_student_names)

# 3)print student name whose exp>1

student_name_expgt1=[stud.get("name") for stud in students if stud.get("exp")>1]
print("The name of students",student_name_expgt1)

# 4) print student name whose skills contain both java python
java_py_names=[stud.get("name") for stud in students if "java" in stud.get("skills") and "python" in stud.get("skills")] 
print(java_py_names)

# 5) print mca students names
mca_stud_names=[stud.get("name") for stud in students if stud.get("qualification")=="mca"]
print(mca_stud_names)

#  6) most experienced student
most_exp=max(students,key=lambda d:d.get("exp"))
high_exp=most_exp.get("exp")
most_exp_stud=[stud.get("name") for stud in students if stud.get("exp")==high_exp]
print(most_exp_stud)

# 7)print students name having skills>2

skill_gt2_name=[stud.get("name") for stud in students if len(stud.get("skills"))>2]
print(skill_gt2_name)
max_skill=max(students,key=lambda d:d.get("skills"))
print(max_skill)


# 8) print name starts with j

j_name=[ stud.get("name") for stud in students if stud.get("name").startswith("j")]
print(j_name)

# 9) most choosen skills
skill_cnt={}
for stud in students:
    skills=stud.get("skills")
    # print(skills)
    for sk in skills:
        if sk in skill_cnt:
            skill_cnt[sk]+=1
        else:
            skill_cnt[sk]=1
# print(skill_cnt)
value_key_pairs=[(v,k) for k,v in skill_cnt.items()]
print(max(value_key_pairs))
