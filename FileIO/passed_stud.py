all_stud=open("C:\\Users\\User\\Desktop\\Python works\\FileIO\\students.txt","r")
failed_stud=open("C:\\Users\\User\\Desktop\\Python works\\FileIO\\failed_stud.txt","r")

all_stud_set={st.rstrip("\n") for st in all_stud}
failed_stud_set={fs.rstrip("\n") for fs in failed_stud}


passed_stud=all_stud_set-failed_stud_set
print(passed_stud)