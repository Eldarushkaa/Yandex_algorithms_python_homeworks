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
for i in range(1, len(s) - 1):
    for l in range(min(i, len(s) - 1 - i), 0, -1):
        a, b = i - l, len(s) - i - l - 1
        if (h[a + l] + hr[b] * xn[l]) % p == (hr[b + l] + h[a] * xn[l]) % p:
            amount_of_palindromes += l
            break
for i in range(len(s) - 1):
    for l in range(min(i, len(s) - 2 - i) + 1, 0, -1):
        a, b = i - l + 1, len(s) - i - l - 1
        if (h[a + l] + hr[b] * xn[l]) % p == (hr[b + l] + h[a] * xn[l]) % p:
            amount_of_palindromes += l
            break
print(amount_of_palindromes)
