# METHODS=append,count,index,pop,insert,remove,copy



orders=["friedrice","gheeroast","vb","cb","bb","vb","cb","vb","cb"] #list supports +ve and -ve indexing
        # 0 	        1          2    3   4   5     6     7   8   
        #  -8           -7         -6   -5  -4  -3     -2   -1  -1

orders.append("tea")              #to add objects
print(orders)

orders.insert(1,"chilligobi")      #insert obj @ index position 1
print(orders)

print(orders.count("vb"))         #to count no of occurances

print(orders.index("gheeroast"))  #to know the index of object

print(orders.pop())               #to remove last obj
print(orders.pop(1))               
print(orders)

orders.remove("vb")                #remove object at the first occurance
print(orders)

cp_orders=orders.copy()            #copy items from a list
cp_orders.remove("friedrice")
cp_orders.reverse()
print(cp_orders)
# print(orders)

cp_orders.sort()                   #sort list obj 
print(cp_orders)

cp_orders.sort(reverse=True)       #sort list obj in reverse order
print(cp_orders)