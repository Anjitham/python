lst1=["a","b","c"]
lst2=["d","e","f","g","h"]
new=" "

for i in range(len(lst1)):
    ith=lst1[i]
    jth=lst2[i]
    
    new+=ith+jth
for k in range(3,len(lst2)):
    kth=lst2[k]
    new+=kth
print(new)


# str1="ABC"
# str2="PQR"

# res=" "
# for i in range(len(str1)):
#     out=str1[i]+str2[i]
#     res+=out

# print(res)


# string1=input("Enter a string:")
# string2=input("Enter a string:")

# small_len=min(len(string1),len(string2))

# result=" "

# for i in range(0,small_len):
#     out=string1[i]+string2[i]
#     result+=out

# if len(string1)>len(string2):
#     rem=string1[small_len:]
# else:
#     rem=string2[small_len:]

# result+=rem
# print(result)