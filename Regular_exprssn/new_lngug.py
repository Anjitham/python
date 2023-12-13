#  starting with k l m n
# second place must be a digit divisible by 3
# followed by any alphabets and numbers
from re import*

rule="[k-n][369][a-zA-z0-9]*"
var_name=input("Enter the variable name:")

matcher=fullmatch(rule,var_name)

print("invalid" if rule==None else "Valid")