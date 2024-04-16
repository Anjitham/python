f=open("C:\\Users\\HP\\Desktop\\Py-Dj\\Python works\\FileIO\\data2.txt","r")

wc={}
for line in f:
    words=line.rstrip("\n").split(" ")
    # print(words)
    for w in words:
        if w in wc:
            wc[w]+=1
        else:
            wc[w]=1
print(wc)
        