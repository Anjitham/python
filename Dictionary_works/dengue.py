dengue_list=["ekm","ekm","tsr","tvm","tvm","ekm","tvm","idk","tvm"]

dist_cnt={}
for ch in dengue_list:
    if ch in dist_cnt:
        dist_cnt[ch]+=1
    else:
        dist_cnt[ch]=1
print(dist_cnt)
dist_cnt_sortd=sorted(dist_cnt,key=lambda k:dist_cnt.get(k),reverse=True)
print(dist_cnt_sortd)
print(dist_cnt_sortd[0])



