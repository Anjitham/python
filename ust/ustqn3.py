lst=[8,6,7]
lst.sort()
n=len(lst)
M=lst[n-1]-lst[0]
m=lst[1]-lst[0]
res=M+5*m
print(res)
