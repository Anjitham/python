from re import*
year=input("Enter a year:")

# rule="((19)[0-9]{2}|(20)[0-9]{2})"
rule="((19|20)[0-9]{2})"
rule="(+91)[5-9]{10}"

matcher=fullmatch(rule,year)

print("Valid" if matcher!=None else "Invalid")