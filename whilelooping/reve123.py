# num=int(input("Enter number:"))
# num=123
# res=0

# while(num!=0):
#     last_dig=num%10
#     res=res*10+last_dig
#     # print(last_dig,end="")
#     num=num//10
# print(res)



x=-123
while(x<0):
    x=abs(x)
    num=x%10
    print(-num,end="")
    x=x//10

while(x!=0):
    num=x%10
    print(num,end="")
    x=x//10