n, m = map(int, input().split())
sequence = list(map(int, input().split()))
for i in range(m):
    l, r = map(int, input().split())
    if min(sequence[l:r+1]) == max(sequence[l:r+1]):
        print("NOT FOUND")
    else:
        print(max(sequence[l:r+1]))
