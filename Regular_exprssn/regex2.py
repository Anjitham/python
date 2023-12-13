from re import *

text="kaBczabc9@7c"
pattern="[^a-zA-Z0-9]" 

text="ab Cak7@#*"
pattern="\\d" #[0-9]

# "[ac]"-------------------- a or c
# "[a-z]" ------------------ all lower case a to z
# "[a-c]" -------------------from a to c
# "[A-Z]"--------------------upper case A to z
# "[a-zA-Z]"-----------------all lower and upper
# "[0-9]" or "\\d"  ---------check for all digitts
# "[a-zA-Z0-9]" or "\w"------alphanumeric characters
# "[^a-z]"-------------------exlcude a-z alphabets and print others
# "[^0-9]"==="\D"------------exclude digits
#  ? ------------------------optional
# ()-------------------------check for a digit eg:(mm)
# |--------------------------this or that 

matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())