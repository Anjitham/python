# convert a string, comprising letters, digits, and symbols, into a valid mobile number by removing all non-digit characters, and ensuring that if the resulting number exceeds 10 digits, it is trimmed down to 10 digits

# password validation

from re import*
Pattern=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
pwd=input("enter pass:")

matcher=fullmatch(Pattern,pwd)
print(True if matcher!=None else False)

# ^  start of sring
# $  end of string
# ?=.* positive look ahead ensures exp has atleast 1 one specified character
# .* at somewhere in the string
# ?= bfr condition means its not optional
# ?. after means its optional

