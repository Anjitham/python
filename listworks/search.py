# LINEAR SEARCH
# lst=[10,2,11,5,7,20]
# element=int(input("Enter an element:"))
# i=0
# is_present=False
# while(i<len(lst)):
#     curnt_elemnt=lst[i]
#     if curnt_elemnt==element:
#         is_present=True
#         # print(lst.index(element))
#         break
#     i+=1
# print(is_present)

# BINARY SEARCH
lst=[10,12,4,8,2,9]
element=int(input("Enter an element:"))
lst.sort()
low=0
upp=len(lst)-1
is_present=False
while(low<=upp):
    mid=(low+upp)//2

    if element==lst[mid]:
        is_present=True
        break
    elif element<lst[mid]:
        upp=mid-1
    elif element>lst[mid]:
        low=mid+1
print(is_present)
