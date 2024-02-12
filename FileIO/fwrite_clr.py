path="C:\\Users\\User\\Desktop\\Py-Dj\\Python works\\FileIO\\colours.txt"
f=open(path,"w")

colors=["red","green","blue"]
for c in colors:
    f.write(c+"\n")   