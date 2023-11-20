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


def part_sort(seq):
    left = seq[:len(seq) // 2]
    right = seq[len(seq) // 2:]
    if len(left) > 1:
        left = part_sort(left)
    if len(right) > 1:
        right = part_sort(right)
    return merge(left, right)


input()
sequence = list(map(int, input().split()))
print(*part_sort(sequence))
