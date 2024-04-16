lst=[1,2,3,4]
lst2=[6,8,9,]
str_lst=[str(i) for i in lst]
str_lst2=[str(i) for i in lst2]

small=min(len(str_lst),len(str_lst2))
# print(small)

res=""
i=0
for i in range(0,small):
    out=str_lst[i]+str_lst2[i]
    res+=out

if len(str_lst)>len(str_lst2):
    rem=str_lst2[small:]
    res+=rem
print(res)

