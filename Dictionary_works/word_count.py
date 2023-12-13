text="hello hai hello hai"



texts=text.split(" ")
print(texts)

word_count={}

for word in texts:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

print(word_count)
