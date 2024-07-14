# print("My name is Anjitha M M from calicut.I'm graduated in B-Tech in CSE from Government Engineering College Wayanad")
# n=30
# for i in range(10,n):
#     for j in range(2,i):
#         if i%j!=0:
#             print(i,end=" ")
#         break



n=10
count=0


for i in range(0,n):
    for j in range(2,i):
        if i%j!=0 and count<=10:
            print(i,end=" ")
        break
    count+=1


# print("{:.2f}".format(10/2))
# print(10/2)