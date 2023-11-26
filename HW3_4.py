from collections import defaultdict


n = int(input())
s, f = map(int, input().split())
k = int(input())
graph = [defaultdict(lambda: defaultdict(lambda: float('inf'))) for i in range(n + 1)]
for i in range(k):
    a, at, b, bt = map(int, input().split())
    graph[a][b][at] = min(graph[a][b][at], bt)

shortest_path = [float('inf')] * (n + 1)
shortest_path[s] = 0
deep = [{s}]
while deep[-1]:
    deep.append(set())
    for start in deep[-2]:
        for next_v in graph[start]:
            if len(list(filter(lambda x: x[0] >= shortest_path[start], graph[start][next_v].items()))):
                arrive = min(filter(lambda x: x[0] >= shortest_path[start], graph[start][next_v].items()), key=lambda x: x[1])[1]
                if arrive < shortest_path[next_v]:
                    shortest_path[next_v] = arrive
                    deep[-1].add(next_v)
        # for next_v, departure, arrive in map((lambda x: (x[0], *x[1])), graph[start].items()):
        #     if departure >= shortest_path[start] and arrive < shortest_path[next_v]:
        #         shortest_path[next_v] = arrive
        #         deep[-1].add(next_v)
    deep.pop(0)
if shortest_path[f] == float('inf'):
    shortest_path[f] = -1
print(shortest_path[f])
