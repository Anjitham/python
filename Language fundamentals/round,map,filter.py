# num=123.456789
# print(round(num,2))


# ----map()
num=[5,6,7,8,9,10,11,12]

def squares(num):
    return num**2
sq=tuple(map(squares,num))
print(sq)

squares=list(map(lambda n:n**2,num))
print(squares)

sq=[n**2 for n in num]
print(sq)


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

num=[5,6,7,8,9,10,11,12]

def squares(num):
    return num**2
sq=list(map(squares,num))
print(sq)


# -----filter

numbers=[5,6,7,8,9,10]
odds=list(filter(lambda num:num%2!=0 ,numbers))
print(odds)

names=["python","pylance","pytz","django","rest","angular"]
name_filter=list(filter(lambda w:w.startswith("py"),names))
print(name_filter)

names=["devika","nirupama","anjitha","roshith"]
lst=list(filter(lambda w:len(w)>6,names))
print(lst)