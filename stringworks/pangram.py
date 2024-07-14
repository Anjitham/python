def check_all_in_alpha(sentence, alphabet):
    sentence = sentence.lower()
    alphabet = alphabet.lower()
    for char in sentence:
        if char.isalpha() and char not in alphabet:
            return False
    return True


sentence = "The quick brown fox jumps over the lazy dog"
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = check_all_in_alpha(sentence, alphabet)
print("Are all characters in the sentence present in the alphabet?", result)
