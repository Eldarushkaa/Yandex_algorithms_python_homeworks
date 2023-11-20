k = int(input())
n = int(input())
time = 0
cur_cap = 0
zeros = 0
for i in range(n):
    workers = int(input())
    if workers:
        zeros = 0
    else:
        zeros += 1
    cur_cap += workers
    time += (cur_cap // k) * (i + 1)
    cur_cap %= k
if cur_cap:
    time += n - zeros
print(time * 2)
