# num=int(input("Enter number:"))
num=123

while(num!=0):
    last_dig=num%10
    print(last_dig,end="")
    num=num//10
