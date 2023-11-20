from random import randrange


def partition(src, x, l, r=0):
    if not r:
        r = len(src) - 1
    e = g = l - 1
    for n in range(l, r + 1):
        if src[n] < x:
            e += 1
            g += 1
            if e == g or n == g:
                src[e], src[n] = src[n], src[e]
            else:
                src[e], src[g], src[n] = src[n], src[e], src[g]
        elif src[n] == x:
            g += 1
            src[g], src[n] = src[n], src[g]
    return e, g


def quicksort(src, l, r):
    me = [src[randrange(l, r + 1)] for i in range(3)]
    e, g = partition(src, sum(me) // 3, l, r)
    if e > l:
        quicksort(src, l, e)
    if r > g + 1:
        quicksort(src, g + 1, r)


n = int(input())
if n:
    sequence = list(map(int, input().split()))
    quicksort(sequence, 0, n - 1)
    print(*sequence)
else:
    print()
