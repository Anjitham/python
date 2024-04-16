# kkerala vehicle number-


from re import*
vehicle_numbers=input("Enter a vehicle number:")
rule="(KL)-?[0-9]{2}[A-Z]-?{1,2}[0-9]{4}"

matcher=fullmatch(rule,vehicle_numbers)
print("valid" if matcher!=None else "Invalid") 