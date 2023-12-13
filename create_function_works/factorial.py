def factorial(num):
    fact=1
    for i in range (1,num+1):
        fact=fact*i
        i+=1
    return fact
print(factorial(4))
