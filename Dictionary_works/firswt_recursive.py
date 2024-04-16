text="ABCABBDE"

# cc={}
# for ch in text:
#     if ch in cc:
#         print("first recursive chara is",cc)
#         break
#     else:
#         cc[ch]=1

# non repeating chara

# cc={}
# for ch in text:
#     if ch in cc:
#         cc[ch]+=1
#     else:
#         cc[ch]=1
# print(cc)
# for k,v in cc.items():
#     if(v==1):
#         print(k)
   
# second recursive character
cc={}
dup_chara=[]
for ch in text:
    if ch in cc:
        cc[ch]+=1
        dup_chara.append(ch)
    else:
        cc[ch]=1
print(dup_chara[1])
