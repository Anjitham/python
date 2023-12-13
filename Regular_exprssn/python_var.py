from re import*

var_name=input("Enter the var name:")
rule="[a-zA-Z]{1}[a-zA-Z0-9_]"

matcher=fullmatch(rule,var_name)

print("Invalid" if matcher==None else "Valid" )