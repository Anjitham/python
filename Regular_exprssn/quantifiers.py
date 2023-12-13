from re import*

text="aaabcaabbaaaabd"
pattern="a{2,4}" # min 2 a's and max 4 a's
#pattern-"a{2}"   #two a's
# pattern="a*" # any number of a including zero numbers [a-z* [0-9]



matcher=finditer(pattern,text)
count=0
for m in matcher:
    print(m.start(),m.group())
    count+=1
print(count)



# quantifiers are:
#  *--astric
# {}--curly braces