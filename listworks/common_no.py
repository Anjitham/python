lst1=[9,4,3,10,15]
lst2=[5,4,2,3,20]
lst1.sort()
lst2.sort()
# for num in lst1:
#     if num in lst2:
#         print(num)



p1=p2=0
while(p1<len(lst1) and p2<len(lst2)):
    if lst1[p1]==lst2[p2]:
        print(lst1[p1])
        p1+=1
        p2+=1
    elif(lst1[p1]>lst2[p2]):
        p2+=1
    elif(lst1[p1]<lst2[p2]):
        p1+=1
