items=["bat","ball","stumps","helmet","arc","cricketball"]

long_word=max(items,key=lambda w:len(w))
print(f"longest word={long_word}")

short_word=min(items,key=lambda w:len(w))
print(f"shortest word={short_word}")


# sum=0
# for i in range (0,len(items)):
#     # print(items[i])
#     sum+=len(items[i])
# print(sum)

# # maxz
# # min0

max_word=items[0]
for i in range(0,len(items)):
    current_word=items[i]
    if len(current_word)>len(max_word):
        max_word=current_word
print(max_word)

# min_word=items[0]
# for i in range(0,len(items)):
#     current_word=items[i]
#     if len(current_word)<len(min_word):
#         min_word=current_word
# print(min_word)