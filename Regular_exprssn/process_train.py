from re import*
f=open("C:\\Users\\User\\Desktop\\Python works\\Regular_exprssn\\train.txt","r")

rule="[1][0-9]{4}"
# for line in  f:
#     num_train=line.rstrip("\n").split(" ")
#     for d in num_train:
#         matcher=fullmatch(rule,d)
#         if matcher!=None:
#             print(d)

# OR
rule="[0-9]{5}"
for line in  f:
    num_train=line.rstrip("\n")
    matcher=finditer(rule,num_train)
    for m in matcher:
        print(m.group())


    
     

        
