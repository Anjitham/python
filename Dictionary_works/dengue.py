dengue_list=["ekm","ekm","tsr","tvm","tvm","ekm","tvm","idk","tvm"]

dist_cnt={}
for ch in dengue_list:
    if ch in dist_cnt:
        dist_cnt[ch]+=1
    else:
        dist_cnt[ch]=1
print(dist_cnt)
# dist_cnt_sortd=sorted(dist_cnt,key=lambda k:dist_cnt.get(k),reverse=True)
# print(dist_cnt_sortd)
# print(dist_cnt_sortd[0])
res=0
for k,v in dist_cnt.items():
    if v==1:
        res=k
        break
print(res)



# d={"a":4,"b":3,"c":6}
# # res=sorted(d,key=lambda n:d.get(n))
# # print(res)
# # ['b', 'a', 'c']


# # res={k:v for k,v in sorted(d.items(),key=lambda n :n[1])}
# # print(res)
# # # {'b': 3, 'a': 4, 'c': 6}

# res=sorted(d.items(),key=lambda n:n[1],reverse=True)
# print(res)
# # [('c', 6), ('a', 4), ('b', 3)]