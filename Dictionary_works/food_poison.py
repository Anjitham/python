sh_death={"tsr":2,"kkd":4,"ekm":5,"tvm":3}

# sh_sort=sorted(sh_death)
# print(sh_sort)              sorting using key


sh_sort=sorted(sh_death,key=lambda k:sh_death.get(k),reverse=True)
print(sh_sort)