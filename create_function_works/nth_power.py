# power of number

def nth_power(num,n=2):
    res=num**n
    return res
print(nth_power(5,3))
print(nth_power(4))

# find the num having smallest number at ones place
def oneth_digit_smallest_num(num1,num2):
    res=num1 if num1%10<num2%10 else num2
    return res
print(oneth_digit_smallest_num(21,10))


# ----->to print the smallest digit at ones place
# def oneth_digit_smallest_num(num1,num2):
#     n1=num1%10
#     n2=num2%10
#     res=n1 if n1<n2 else n2
#     return res
# print(oneth_digit_smallest_num(12,10))

