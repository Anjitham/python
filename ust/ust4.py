lst=[5,5]
# n=len(lst)
# sum=0
# res=0
# for i in range(0,n-1):
#     A=lst[i]
#     for j in range(A+1):
#         sum+=j
# i+=1
# res+=sum
# print(sum)

sum=0
for i in lst:
    for j in range(0,i+1):
        sum+=j
    i+=1
print(sum)