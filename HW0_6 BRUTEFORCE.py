def bruteforce(n, k, sequence):
    cur_cap = 0
    the_last_one = n
    total_time = 0
    for i in range(n - 1, -1, -1):
        if not cur_cap:
            the_last_one = i + 1
        cur_cap += sequence[i]
        if cur_cap >= k:
            total_time += the_last_one * 2
            cur_cap -= k
            the_last_one = i + 1
            total_time += (cur_cap // k) * the_last_one * 2
            cur_cap %= k
    if cur_cap:
        total_time += 2 * the_last_one
    return total_time


k = int(input())
n = int(input())
sequence = [int(input()) for i in range(n)]
print(bruteforce(n, k, sequence))
