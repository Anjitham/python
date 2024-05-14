# text="ABCDCDC"
# check="CDC"
# p1=0
# p2=0
# res=""
# cnt=0
# print(check[p1])
# for i in range(0,len(text)):
#     if text[p2]==check[p1]:
#         res+=text[p2]
#         cnt+=1
#         p1+=1
#         p2+=1
#     elif text[p2]!=check[p1]:
#         p2+=1
# print(res)
# print(cnt)


text = "ABCDCDC"
check = "CDC"
p1 = 0
p2 = 0
res = ""
cnt = 0

while p2 < len(text):
    if text[p2] == check[p1]:
        res += text[p2]
        p1 += 1
        if p1 == len(check):
            cnt += 1
            p1 = 0
        p2 += 1
    else:
        p1 = 0
        p2 += 1

print(res)
print(cnt)
