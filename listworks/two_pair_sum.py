arr=[3,4,5,2,6]
sum=int(input("enter a value for sum:"))
arr.sort()
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        cur_sum=arr[i]+arr[j]
        if sum==cur_sum:
            print(arr[i],arr[j])
            break




# OR 
# arr=[3,4,5,2,6]
# sum=int(input("enter a value for sum:"))
# arr.sort()
# low=0
# upp=len(arr)-1
# count=0
# while(low<upp):
#     curr_sum=arr[low]+arr[upp]
#     if curr_sum==sum:
#         print(arr[low],arr[upp])
#         low+=1
#         upp-=1
#     elif curr_sum<sum:
#         low+=1
#     elif curr_sum>sum:
#         upp-=1

# OR


arr=[3,4,5,2,6]
sum=int(input("enter a value for sum:"))
arr.sort()
i=0
while(i<len(arr)):
    ith_elmnt=arr[i]
    jth_elmnt=sum-ith_elmnt
    if jth_elmnt in arr[i+1:]:
        print(ith_elmnt,jth_elmnt)
    i+=1


    


















