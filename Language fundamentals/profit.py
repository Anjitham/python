selling_price=int(input("Enter price"))
cost_price=int(input("Enter price"))

profit=selling_price-cost_price
print(f"profit is{profit}")

profit_in_percent=(profit/cost_price)*100
print(f"profit in percent is {profit} and {profit_in_percent}")
