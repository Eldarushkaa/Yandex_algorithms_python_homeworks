def works(target):
    deep = [{1}]
    shortest_time = [float('inf')] + [0] + [float('inf')] * (len(cities) - 2)
    while deep[-1]:
        deep.append(set())
        for start in deep[-2]:
            for dest in cities[start]:
                if cities[start][dest][1] >= target and shortest_time[start] + cities[start][dest][0] < shortest_time[dest] and shortest_time[start] + cities[start][dest][0] <= 1440:
                    shortest_time[dest] = shortest_time[start] + cities[start][dest][0]
                    deep[-1].add(dest)
        deep.pop(0)
    if shortest_time[-1] > 1440:
        return False
    return True


n, m = map(int, input().split())
cities = [dict() for i in range(n + 1)]
for i in range(m):
    a, b, t, w = map(int, input().split())
    cities[a][b] = (t, w)
    cities[b][a] = (t, w)
l, r = 3000000, 1000000000
while l < r:
    c = (l + r) // 2
    if works(c) and not works(c + 1):
        l = r = c
    elif works(c + 1):
        l, r = c + 2, r
    else:
        l, r = l, c - 1
if r < 3000000:
    print(0)
elif n == 1:
    print(10000000)
else:
    print((r - 3000000) // 100)
