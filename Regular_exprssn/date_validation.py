from re import*

day=input("Enter a day(dd-mm-yyyy):")

# rule="(0[1-9]|[12][0-9]|3[0-1])-(0[1-9]|[12][0-9]||3[01])-((19|20)[0-9]{2})"
rule="(0[1-9]|[12][0-9]|3[0-1])-(0[1-9]|1[0-2])-((19|20)[0-9]{2})"
rule="([0-2][0-9]|3[0-1])-(0[1-9]|1[0-2])-((19|20)[0-9]{2})"

matcher=fullmatch(rule,day)
print("Valid" if matcher!=None else "Invalid" )
