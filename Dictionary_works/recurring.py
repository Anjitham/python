# print max recurring element
# text="pneumonoultramicroscopicsilicovolcanoconiosis"
text="goodmorning"
chara_count={}

for ch in text:
    if ch in chara_count:
        chara_count[ch]+=1
    else:
        chara_count[ch]=1

print(chara_count)




