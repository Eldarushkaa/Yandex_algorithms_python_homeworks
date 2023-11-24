s = input()
sr = list(reversed(s))
h = [0] * (len(s) + 1)
xn = [1] * (len(s) + 1)
hr = [0] * (len(s) + 1)
p = 10**9 + 7
x = 257
for i in range(len(s)):
    h[i + 1] = (h[i] * x + ord(s[i])) % p
    xn[i + 1] = xn[i] * x % p
    hr[i + 1] = (hr[i] * x + ord(sr[i])) % p

amount_of_palindromes = len(s)
for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
        l, a, b = (i + j) // 2 - i + 1, i, len(s) - j - 1
        if (h[a + l] + hr[b] * xn[l]) % p == (hr[b + l] + h[a] * xn[l]) % p:
            amount_of_palindromes += 1
print(amount_of_palindromes)
