current_reading=int(input("Enter current units consumed:"))
last_reading=int(input("Enter last units:"))

unit_rate=int(input("Enter unit rate:"))
consumed_units=current_reading-last_reading

bill=consumed_units*unit_rate
print(f"electricity bill is{bill}")


