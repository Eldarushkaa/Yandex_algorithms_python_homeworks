from functools import partial


input()
s = input()
sr = list(reversed(s))
h = [0] * (len(s) + 1)
hr = [0] * (len(s) + 1)
xn = [1] * (len(s) + 1)
p = 10**9 + 7
x = 257
for i in range(len(s)):
    h[i + 1] = (h[i] * x + ord(s[i])) % p
    hr[i + 1] = (hr[i] * x + ord(sr[i])) % p
    xn[i + 1] = xn[i] * x % p


def no_pls(a, b, l):
    return (h[a + l] + hr[b] * xn[l]) % p == (hr[b + l] + h[a] * xn[l]) % p


for i in range(0, len(s)):
    t, r = 0, i + 1
    a, b = 0, len(s) - i - 1
    pls = partial(no_pls, a, b)
    while t < r:
        l = (t + r) // 2
        if pls(l) and not pls(l + 1):
            t = r = l
        elif pls(l + 1):
            t, r = l + 1, r
        elif pls(l):
            t, r = l, r
        else:
            t, r = t, l - 1
    print(t, end=' ')
