import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    contains_all = True
    for letter in alphabet:
        if str1.find(letter) == -1:
            contains_all = False

    return contains_all

print(ispangram("The quick brown fox jumps over the lazy dog"))