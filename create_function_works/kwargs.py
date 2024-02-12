# def add_employee(**kwargs):
#     print(kwargs.get("name"))
#     print(kwargs.get("salary"))

# add_employee(id=10,name="anu",n_place="ekm",w_place="tvm",salary=25000)

# def last_dig_sort(*args,**kwargs):
#     dig=[n%10 for n in args]
#     value=kwargs.get("reversed")
#     if value==True:
#         dig.sort(reverse=True)
#     else:
#         dig.sort()
#     return dig
# print(last_dig_sort(17,14,12,13,11,reversed=True)) 


# last_dig_calculator(432,234,123,453,567,op) op=+ - *
def last_dig_calculator(*args,**kwargs):
    res=0
    mult=0
    value=kwargs.get("op")
    # op=input("Enter operator:")
    for i in args:
        dig=i%10
        if value=="+":
           res+=dig
        elif value=="*":
            mult*=dig
            res=mult
        elif value=="-":
            res-=dig
        return res
print(last_dig_calculator(432,234,123,453,567,op="+"))

