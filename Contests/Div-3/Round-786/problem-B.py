t = int(input())  # test cases

letters = 'abcdefghijklmnopqrstuvwxyz'

words = []

for i in range(len(letters)):
    for letter in letters:
        words.append(letter+letters[i])

all_words = sorted(words)

berland = []

for word in all_words:
    if word[0] != word[1]:
        berland.append(word)


for i in range(t):

    text = input()

    print(berland.index(text) + 1)