number=input("Enter a number:")  # length of integer can't be taken
dig_count=len(number)
number=int(number)
sum=0
num=number

while(number!=0):
    digit=number%10
    exp=digit**dig_count
    sum+=exp
    number=number//10
print(sum)
print(f"Amstrong" if num==sum else "not")


# num=153
# sum=0

# while(num!=0):
#     last_dig=num%10
#     cube=last_dig**3
#     sum+=cube
#     num=num//10
# print(sum)