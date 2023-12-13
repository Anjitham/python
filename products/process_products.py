from json import load
f=open("C:\\Users\\User\\Desktop\\Python works\\products\\items.json",encoding="utf-8")
data=load(f)
print(len(data))

all_category={p.get("category") for p in data}
print(all_category)

ele_products=[p for p in data if p.get("category")=="electronics"]
print(len(ele_products))

jwlry_products=[p for p in data if p.get("category")=="jewelery"]
print(len(jwlry_products))

costly_prdct=max(data,key=lambda d:d.get("price"))
costly_name=costly_prdct.get("title")
print(costly_name)