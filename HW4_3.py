graph = [list(map(int, input().split())) for i in range(int(input()))]
max_way = [max(graph[i]) for i in range(len(graph))]
best_weight = 0
best_division = ''
prev = '0' * len(graph)
prev_weight = 0
for i in range(1, 2**(len(graph) - 1)):
    diversion = format(i, 'b')
    diversion = '0' * (len(graph) - len(diversion)) + diversion
    weight = prev_weight
    zeros = len(list(filter(lambda x: x == '0', diversion)))
    # ones = len(graph) - zeros
    if zeros > (len(graph) + 1) // 2:
        continue
    # approx_weight = 0
    # for j in range(len(graph)):
    #     if diversion[j] == '0':
    #         approx_weight += max_way[j] * ones
    #     else:
    #         approx_weight += max_way[j] * zeros
    # br = False
    for j in range(len(graph)):
        if prev[j] != diversion[j]:
            for l in range(len(graph)):
                if prev[l] != prev[j]:
                    weight -= graph[l][j]
                if diversion[j] != diversion[l]:
                    weight += graph[l][j]
    # for j in range(len(graph) - 1):
    #     for l in range(j + 1, len(graph)):
    #         if diversion[j] != diversion[l]:
    #             weight += graph[j][l]
    #             if weight + approx_weight < best_weight:
    #                 br = True
    #                 break
    #     if br:
    #         break
    #     if diversion[j] == '0':
    #         approx_weight -= max_way[j] * ones
    #     else:
    #         approx_weight -= max_way[j] * zeros
    if weight >= best_weight:
        best_weight = weight
        best_division = diversion
print(best_weight)
print(*map(lambda x: int(x) + 1, best_division))
