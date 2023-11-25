n = int(input())
cities = [[[0] * n, *map(int, input().split())] for i in range(n)]
for _ in range(n - 1):
    dest, start, dist = map(int, input().split())
    cities[start - 1][0][dest - 1] = dist
    cities[dest - 1][0][start - 1] = dist

for i in range(n):
    deep = [{*filter(lambda x: cities[i][0][x], range(n))}]
    while deep[-1]:
        deep.append(set())
        for start in deep[-2]:
            for j in range(n):
                if not cities[start][0][j]:
                    continue
                if j != i and not cities[i][0][j]:
                    cities[i][0][j] = cities[i][0][start] + cities[start][0][j]
                    cities[j][0][i] = cities[i][0][start] + cities[start][0][j]
                    deep[-1].add(j)
    deep.pop(0)

for row in cities:
    print(row[0])

deep = [{0}]
shortest_path_to_moscow = [0] + [-1] * (len(cities) - 1)
visited_from = [-1] * n
while deep[-1]:
    deep.append(set())
    for dest in deep[-2]:
        for start in range(n):
            if start == dest:
                continue
            path_to_moscow = shortest_path_to_moscow[dest] + cities[start][1] + cities[start][0][dest] / cities[start][2]
            if shortest_path_to_moscow[start] == -1 or shortest_path_to_moscow[start] > path_to_moscow:
                shortest_path_to_moscow[start] = path_to_moscow
                deep[-1].add(start)
                visited_from[start] = dest
    deep.pop(0)

last = shortest_path_to_moscow.index(max(shortest_path_to_moscow))
path = []
while last != -1:
    path.append(last + 1)
    last = visited_from[last]

print(max(shortest_path_to_moscow))
print(*path)
