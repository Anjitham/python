source_word="myself"
target_word="self"

src_word_list=[ch for ch  in source_word]
trgt_word_list=[ch for ch in target_word]

for ch in trgt_word_list:
    if ch in src_word_list:
        src_word_list.remove(ch)
    else:
        print("not a kangaroo word")
        break
else:
    print("kangaroo word")
    