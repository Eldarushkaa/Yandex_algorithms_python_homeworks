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
    return e + 1


n = int(input())
answer = partition(list(map(int, input().split())), int(input()), 0)
print(answer, n - answer, sep='\n')
