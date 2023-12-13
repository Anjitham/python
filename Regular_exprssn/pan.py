from re import*
number=input("ENter the PAN Number:")
rule="[A-Z]{3}[PCAFHT]{1}[A-Z][0-9]{4}[A-Z]"


matcher=fullmatch(rule,number)
print("Invalid" if matcher==None else "Valid")