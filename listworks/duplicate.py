arr=[4,9,5,6,9,5,4]

arr.sort()
print(arr)
i=0
# count=0
# for i in range(0,len(arr)-1):
#     for j in range(i+1,len(arr)):
#         ith_element=arr[i]
#         jth_element=arr[j]
#         diff=jth_element-ith_element
#         if diff==0:
#             print(ith_element)
#             break
# #         count+=1
# # print(count)


# OR

while(i<len(arr)-1):
    j=i+1
    ith_element=arr[i]
    jth_element=arr[j]
    diff=jth_element-ith_element
    if diff==0:
        print(ith_element)
        # i=j
    i+=1


