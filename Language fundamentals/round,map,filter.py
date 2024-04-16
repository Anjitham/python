num=123.456789
print(round(num,2))


# ----map()
num=[5,6,7,8,9,10,11,12]

def squares(num):
    return num**2
sq=list(map(squares,num))
print(sq)


# or
squares=list(map(lambda n:n**2,num))
print(squares)
# or
sq=[n**2 for n in num]
print(sq)

# -----filter

numbers=[5,6,7,8,9,10]
odds=list(filter(lambda num:num%2!=0 ,numbers))
print(odds)

names=["python","pylance","pytz","django","rest","angular"]
name_filter=list(filter(lambda w:w.startswith("py"),names))
print(name_filter)