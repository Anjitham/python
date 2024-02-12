# slicing
name="TECHNOLAB"

# #------ Positive indexing
# # [start:stop:step],step can be upto -1
# print(name[2:4]) #CH
# print(name[:7]) #start=1,stop=7
# print(name[2:]) #start=2,stop=length of string

# ------Negative indexing
print(name[-1:-4:-1])
print(name[:-5:-1]) #BALO

rev=name[::-1]
print(rev)

# palindrome

word="madam"
rev_word=word[::-1]
print("palindrome" if word==rev_word else "not palindrome")

# slicing @ particular length

str1="Haii"
str2="Goodmorning"

length=len(str1)
rem=str2[length:]
print(rem)