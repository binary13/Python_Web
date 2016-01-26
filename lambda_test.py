def word_lengths(phrase):
    return list(map(lambda word: len(word), phrase.split()))

phrase = 'How long are the words in this phrase'

split_phrase = phrase.split()

print(split_phrase)

lengths = list(map(lambda word: len(word), split_phrase))

lengths_list = []
for word in phrase.split():
    lengths_list.append(len(word))


print("Using for loop:", lengths_list)

print("Using map:", lengths)

print("Using list:", word_lengths(phrase))

