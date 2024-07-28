arr=[1,4,3,5,6,7]

arr.sort()
print(arr)
k=0
# while(i<len(arr)-1):
for i in arr:
    # j=i+1
    ith_elmnt=i
    jth_elmnt=arr[k+1]
    diff=jth_elmnt-ith_elmnt
    if diff!=1:
        print(f"{ith_elmnt+1} is the missing element")
        break
        i=j
    i+=1