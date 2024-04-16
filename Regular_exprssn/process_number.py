from re import*

# f=open("C:\\Users\\User\\Desktop\\Python works\\Regular_exprssn\\numbers.txt")
f=open("C:\\Users\\HP\\Desktop\\Py-Dj\\Python works\\Regular_exprssn\\numbers.txt")

rule="([+]91)?[0-9]{10}"

for line in f:
    numbers=line.rstrip("\n")
    # print(numbers)
    matcher=fullmatch(rule,numbers)
    if matcher!=None:
        print(numbers)