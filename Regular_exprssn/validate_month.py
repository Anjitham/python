## MONTH VALIDATION

from re import*
month=input("Enter month(mm): ")

rule="0[1-9]|1[0-2]"

matcher=fullmatch(rule,month)

print("Valid" if matcher!=None else "Invalid")

## DATE VALIDATION

# from re import*

# date=input("Enter a date(dd):")

# rule="(0[1-9]|[12][0-9]||3[01])"   # or (0[1-9]|1[0-9]|2[0-9]|3[01])
# matcher=fullmatch(rule,date)

# print("Valid" if matcher!=None else "Invalid")