A=[1,2,3,4,5,6,7,8]
even=[]
for i in range(1,len(A),2):
    even.append(A[i])
even.reverse()
# print(even)

i=1
for num in even:
    A[i]=num
    i+=2
print(A)



# A[1],A[3],A[5],A[7]=A[7],A[5],A[3],A[1]
# print(A)