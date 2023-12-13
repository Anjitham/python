# # print squares
lst=[2,4,5,6,7,8,9]
# squares=[]
# for num in lst:
#     sq=num**2
#     squares.append(sq)
# print(squares)

# # list of even numbers
# even=[]
# for num in lst:
#     if num%2==0:
#         even.append(num)
# print(even)

# # LIST COMPREHENSION
# # [return value for num in lst condition]

# squares=[num**2 for num in lst]
# print(squares)

# cubes=[num**3 for num in lst]
# print(cubes)

# even=[num for num in lst if num%2==0] 
# print(even)

odd=[num for num in lst if num%2!=0]
print(odd)

# c4=["apple","orange","mango","milk","pomegranete"]
# upper_names=[name.upper() for name in c4 ]
# print(upper_names)
# name_gt_5=[name for name in c4 if len(name)>=5]
# print(name_gt_5)

lst=["red","green","blue","white","black","apple","ignore","under"]
# print words starting with vowels
# print words starting with consonants
vowel=["a","e","i","o","u"]
vowel_elmnt=[word for word in lst if word[0] in vowel]
# vowel_elmnt=[word for word in lst if word[0] in ["a","e","i","o","u"]]
print(vowel_elmnt)


cons_elmnt=[word for word in lst if word[0] not in vowel]
print(cons_elmnt)

nums=[12,67,5,8]
str_nums=[str(n) for n in nums]
print(str_nums)