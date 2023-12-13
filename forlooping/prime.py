num=int(input("Enter a number:"))

is_prime=True #prime
for i in range(2,num,1):
    if (num%i==0):
        is_prime=False #not prime
        break
print(is_prime)
