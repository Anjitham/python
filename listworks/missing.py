arr=[1,4,3,5,6,7]

arr.sort()
print(arr)
i=0
while(i<len(arr)-1):
    j=i+1
    ith_elmnt=arr[i]
    jth_elmnt=arr[j]
    diff=jth_elmnt-ith_elmnt
    if diff!=1:
        print(f"{ith_elmnt+1} is the missing element")
        break
        i=j
    i+=1