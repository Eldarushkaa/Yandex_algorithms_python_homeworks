s = input()
h = [0] * (len(s) + 1)
xn = [1] * (len(s) + 1)
p = 10**9 + 7
x = 257
for i in range(len(s)):
    h[i + 1] = (h[i] * x + ord(s[i])) % p
    xn[i + 1] = xn[i] * x % p

for i in range(int(input())):
    l, a, b = map(int, input().split())
    if (h[a + l] + h[b] * xn[l]) % p == (h[b + l] + h[a] * xn[l]) % p:
        print('yes')
    else:
        print('no')
