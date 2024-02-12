

def amstrong(number):
    dig_count=len(number)
    num=int(number)
    sum=0
    og_num=num
    while(num!=0):
        digit=num%10
        exp=digit**dig_count
        sum+=exp
        num=num//10
    res=True if sum==og_num else False
    return res

print(amstrong("153"))




