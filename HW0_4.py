from collections import defaultdict


def prog(word1, word2):
    if len(word1) > len(word2):
        word1, word2 = word2, word1

    book = defaultdict(lambda: 0)
    for letter in word2:
        book[letter] += 1
    for letter in word1:
        if book[letter] < 1:
            return 'NO'
        book[letter] -= 1
    return 'YES'


print(prog(input(), input()))
