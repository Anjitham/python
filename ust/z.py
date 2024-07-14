text="abcZd123@"
# ind=0
# s=[int(i) for i in text if i.isdigit()]
for i in text:
    if i.isupper():
        break
print(i)


import calendar 

yy = 2017
mm = 11
print(calendar.month(yy, mm)) 


print(calendar.isleap(2020))