from collections import defaultdict


n, s, f = map(int, input().split())
graph = [dict() for i in range(n + 1)]
for i in range(1, n + 1):
    for j, dist in enumerate(map(int, input().split()), start=1):
        if dist != -1 and i != j:
            graph[i][j] = dist
visited_from = [-1] * (n + 1)
shortest_path = [float('inf')] * (n + 1)
shortest_path[s] = 0
deep = [{s}]
while deep[-1]:
    deep.append(set())
    for start in deep[-2]:
        for next_v, dist in graph[start].items():
            if dist + shortest_path[start] < shortest_path[next_v]:
                shortest_path[next_v] = shortest_path[start] + dist
                visited_from[next_v] = start
                deep[-1].add(next_v)
    deep.pop(0)
if shortest_path[f] == float('inf'):
    shortest_path[f] = -1
