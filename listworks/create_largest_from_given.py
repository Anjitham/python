arr=[23,12,78,9]
str_arr=[str(n) for n in arr]
print(str_arr)
str_arr.sort(reverse=True)
print(str_arr)

i=0
res=0
# print(type(str_arr[1]))
while(i<len(str_arr)):
    curr=str_arr[i]
    res=int(str(res)+curr)
    i+=1
print(res)





# while(i<len(arr)):
    
#     cur_max=max(arr)
#     max_val=int(str(max_val)+str(cur_max))
#     arr.remove(cur_max)
# print(max_val)
