def anti_vowel(text):
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    for vowel in vowels:
        text = text.replace(vowel, "")
    return text

def anti_vowel2(text):
    newtext = text.strip("AaEeIiOoUu")
    return newtext

print(anti_vowel("Hey look, words!"))
print(anti_vowel2("Hey look, words!"))

def censor(text, word):
    rep_word = ""
    for n in word:
        rep_word += "*"

    text = text.replace(word, rep_word)
    return text

cs = censor("This hack is whack hack.", "hack")
print(cs)