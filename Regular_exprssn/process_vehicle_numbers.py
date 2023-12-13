from re import*

f=open("C:\\Users\\User\\Desktop\\Python works\\Regular_exprssn\\vehicle_numbers.txt","r")

rule="(KL|TN)-[0-9]{2}-[A-Z]{1,2}-[0-9]{4}"

for line in f:
    veh_num=line.rstrip("\n")
    # print(veh_num)
    matcher=fullmatch(rule,veh_num)
    print(veh_num if matcher!=None else "No match")
