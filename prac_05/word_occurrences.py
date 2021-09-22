words_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    frequency = words_to_count.get(word, 0)
    words_to_count[word] = frequency + 1

words = list(words_to_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, words_to_count[word]))
