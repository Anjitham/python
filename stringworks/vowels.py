# consonants and vowels 

text="#@12pneumonoultramicroscopicsilicovolcanoconiosis"

v_count=0
c_count=0
vowels=["a","e","i","o","u"]  #["a","e","i","o","u"]      or    #ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":

for ch in text:
    if ch  not in vowels:   
        if ch.isalpha():
            c_count+=1
    else:
        v_count+=1
print(f"vowel count={v_count}")
print(f"consonat count={c_count}")
print(f"Total number of characters={len(text)}")

#consonants

# for ch in text:
#     if ch  not in vowels: 
#          c_count+=1
# print(f"consonat count={c_count}")


# vowels
# for ch in text:
#     if ch  in vowels: 
#          v_count+=1
# print(f"consonat count={v_count}")


# special characters
# for ch in text:
#     if ch  not in vowels:   
#         if ch.isalpha():
#             c_count+=1
