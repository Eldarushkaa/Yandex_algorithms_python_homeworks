def gcd(x, y):
    if x == y:
        return x
    d = min(x, y)
    while x % d != 0 or y % d != 0:
        d -= 1
    return d


a, b, c, d = map(int, input().split())

g = gcd(b, d)
p = a * (d // g) + c * (b // g)
q = b * d // g
g = gcd(p, q)
p //= g
q //= g
print(p, q)
