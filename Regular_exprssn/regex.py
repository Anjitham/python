from re import *

text="cat-fat-run-fast-catch"
pattern="at"

matcher=finditer(pattern,text) #(0,at)

count=0
for obj in matcher:
    print(obj.start(),obj.group())
    count+=1
print(count)

