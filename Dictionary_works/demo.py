# methods
# keys(),values(),items(),update(),pop(),get()


# keys() ----return all keys
product={"code":1001,"name":"Orange","price":35}
# print(product["name"])   #can not be used in every situations

# for k in product.keys():
#     print(k)

# for v in product.values():
#     print(v)

for k,v in product.items():
    print(k,v)

# print(product.get("code"))


# product["price"]=75
# print(product)
# # or/ add new dictionary
# product.update({"code":1})
# print(product)

# product.update({"name":"oranges"})
# product["name"]="oranges"
# print(product)
 
print(product.pop("code"))
# # print(product)

