n = int(input())
cities = [[dict(), *map(int, input().split())] for i in range(n)]
matrix = [[0] * n for _ in range(n)]
for _ in range(n - 1):
    dest, start, dist = map(int, input().split())
    cities[start - 1][0][dest - 1] = dist
    cities[dest - 1][0][start - 1] = dist
    matrix[dest - 1][start - 1] = matrix[start - 1][dest - 1] = dist

for i in range(n):
    deep = [{i}]
    visited = [0] * n
    visited[i] = 1
    while deep[-1]:
        deep.append(set())
        for start in deep[-2]:
            for dest in filter(lambda x: not visited[x], cities[start][0]):
                matrix[dest][i] = matrix[i][dest] = matrix[i][start] + matrix[start][dest]
                visited[dest] = 1
                deep[-1].add(dest)
        deep.pop(0)

deep = [{0}]
shortest_path_to_moscow = [0] + [-1] * (len(cities) - 1)
visited_from = [-1] * n
while deep[-1]:
    deep.append(set())
    for dest in deep[-2]:
        for start in filter(lambda x: x != dest, range(n)):
            path_to_moscow = shortest_path_to_moscow[dest] + cities[start][1] + matrix[start][dest] / cities[start][2]
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
