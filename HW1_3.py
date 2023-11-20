def merge(a, b):
    c = [0] * (len(a) + len(b))
    l = 0
    r = 0
    while l < len(a) and r < len(b):
        if a[l] <= b[r]:
            c[l + r] = a[l]
            l += 1
        else:
            c[l + r] = b[r]
            r += 1
    c[l+r:] = a[l:] + b[r:]
    return c


input()
a = list(map(int, input().split()))
input()
b = list(map(int, input().split()))
print(*merge(a, b))
