def count_from_center(i, j, s):
    amount_of_pals = 0
    while 0 <= i and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
        amount_of_pals += 1
    return amount_of_pals


def count_palindromes(s):
    amount_of_all_palindromes = 0
    for i in range(len(s)):
        amount_of_all_palindromes += count_from_center(i, i, s)
    for i in range(len(s) - 1):
        amount_of_all_palindromes += count_from_center(i, i + 1, s)
    return amount_of_all_palindromes


print(count_palindromes(input()))
