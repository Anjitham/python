order1={"cb","tikka","fisfry","friedrice","vb","gheerice"}
order2={"cb","friedrice","nan","upma","vegetables","idly"}

# inter_orders=order1.intersection(order2)
# print(inter_orders)
# uni_orders=order1.union(order2)
# uni_order_without=uni_orders.difference(inter_orders)
# print(uni_order_without)

uni_order_without=order1.symmetric_difference(order2)
print(uni_order_without)