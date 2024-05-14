# lst=[2,3,4]
# # lst=[n**2 for n in lst]
# # lst=list(map(lambda n:n**2,lst))
# print(lst)

# arr=[1,2,3]
# cube=list(map(lambda n:n**3,arr))
# print(cube)

# lst=[4,5,6,7,8]
# even=list(filter(lambda n:n%2==0,lst))
# print(even)

# --------filter

# names=["devika","nirupama","anjitha","roshith"]
# lst=list(filter(lambda w:len(w)>6,names))
# print(lst)


# ---palindrome
string="madam"
# list=list(string)
# print(list)
# list.reverse()
# rev=""
# for i in list:
#     rev=rev+i
# print(rev)
# print(True if rev==string else False)

rev=string[::-1]
print(True if rev==string else False)




# # ----map()
# num=[5,6,7,8,9,10,11,12]

# def squares(num):
#     return num**2
# sq=list(map(squares,num))
# print(sq)







