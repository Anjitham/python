def is_prime(num):
    for i in range(2,num):
        res=False if num%2==0 else True
    return res
print(is_prime(7))