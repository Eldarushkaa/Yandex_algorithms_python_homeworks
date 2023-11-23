from functools import partial


s = input()
h = [0] * (len(s) + 1)
xn = [1] * (len(s) + 1)
p = 10**9 + 7
x = 257
for i in range(len(s)):
    h[i + 1] = (h[i] * x + ord(s[i])) % p
    xn[i + 1] = xn[i] * x % p


def no_pls(a, b, l):
    return (h[a + l] + h[b] * xn[l]) % p == (h[b + l] + h[a] * xn[l]) % p


print(end='0 ')
for i in range(1, len(s)):
    t, r = 0, len(s) - i
    a, b = 0, i
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
