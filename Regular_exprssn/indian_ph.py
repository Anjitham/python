from re import*

ph_number=input("Enter a phone number:")

rule="([+]91)?[5-9][0-9]{9}"
# rule=""

matcher=fullmatch(rule,ph_number)

print("Valid" if matcher!=None else "Invalid")