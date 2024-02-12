# def addition(*args):  # add many numbers
#     return sum(args)
# print(addition(10,20))

# def product(*args):
#     res=0
#     for n in args:
#         res*=n
#     return res
# print(product(10,20))

# def last_dig_sum(*args):
#     # res=0
#     # for n in args:
#     #     last_dig=n%10
#     #     res=res+last_dig
#     # return res
#     return sum(n%10 for n in args)
# print(last_dig_sum(12,13,14,))

def max_last_dig(*args):
    return max(n%10 for n in args)
print(max_last_dig(12,13,19,))