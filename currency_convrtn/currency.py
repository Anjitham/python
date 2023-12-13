from json import load
f=open("C:\\Users\\User\\Desktop\\Python works\\currency_convrtn\\data.json",encoding="utf-8")
data=load(f)


source_currency_code=input("Enter source currency code:")
target_currency_code=input("Enter destination target currency code:")

amount=int(input("Enter amount:"))

conversion_rates=data.get("conversion_rates")
# print(conversion_rates)

source_currency_code_rate=conversion_rates.get(source_currency_code)
destination_currency_code_rate=conversion_rates.get(target_currency_code)

print(source_currency_code_rate)
print(destination_currency_code_rate)

# print amount of conversion
res=(amount/source_currency_code_rate)*destination_currency_code_rate
print(res)
