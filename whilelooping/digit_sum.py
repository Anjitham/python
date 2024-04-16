num=123
sum=0
# print(type(num))

while(num!=0):
    last_dig=num%10
    sum+=last_dig
    num=num//10
print(sum)