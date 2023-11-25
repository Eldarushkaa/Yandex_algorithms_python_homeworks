def permutation(length, prev=0, *args):
    global best
    if len(args) == 0:
        if matrix[prev][0]:
            return length + matrix[prev][0]
        return best
    for i in range(len(args)):
        if not matrix[prev][args[i]]:
            continue
        if length + matrix[prev][args[i]] < best:
            best = min(best, permutation(length + matrix[prev][args[i]], args[i], *args[:i], *args[i+1:]))
    return best


matrix = [list(map(int, input().split())) for i in range(int(input()))]
best = float('inf')
if len(matrix) < 2:
    print(0)
else:
    permutation(0, 0, *range(1, len(matrix)))
    if best == float('inf'):
        print(-1)
    else:
        print(best)
