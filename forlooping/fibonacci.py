prev_num=0
curr_num=1

print(f"{prev_num},{curr_num}", end=",")



for i in range (1,11):
    next=prev_num+curr_num
    print(next,end=",")
    prev_num=curr_num
    curr_num=next
    



# end=","  ----> puts ,
# end="#" ------>puts #
# \n=newline