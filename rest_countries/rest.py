from json import load
f=open("C:\\Users\\User\\Desktop\\Python works\\rest_countries\\data.json",encoding="utf-8")
data=load(f)
# print length of data
print(len(data))

# # all_country name
# all_cntry_names=[c.get("name") for c in data]
# print(all_cntry_names)

# # print all independent countries
# independent_cntry=[c.get("name") for c in data if c.get("independent")==True]
# print(independent_cntry)

# # print all regions
# all_regions={c.get("region") for c in data}
# print(all_regions)

# # asian country names
# asian_cntry=[ c.get("name") for c in data if c.get("region")=="Asia"]
# print(asian_cntry)

# # capital of ukraine
# capital_ukraine=[c.get("capital") for c in data if c.get("name")=="Ukraine"]
# print(capital_ukraine)

# # cntry name &capital
# cntry_capital=[(c.get("name"),(c.get("capital"))) for c in data]
# print(cntry_capital)

# # print all country name and currency
# for c in data:
#     if "currencies" in c:
#         currency_data=c.get("currencies")[0]
#         print(c.get("name"),",",currency_data.get("name"))


# # name of cntries that share border with india
# india_borders=[c.get("borders") for c in data if c.get("name")=="India"][0]
# print(india_borders)
# india_border_name=[c.get("name") for c in data if c.get("alpha3Code") in india_borders]
# print(india_border_name)

# cntry having borders>4
# for c in data:                                ##brdr=[c.get("name") for c in data if "borders" in c and len(c.get("borders"))>4]
#     if "borders" in c:                        ##print(brdr)
#         if len(c.get("borders"))>4:
#             print(c.get("name"))
        
