objects = dict(map(lambda x: [x[0], [int(x[1]), dict()]], (input().split(',') for i in range(int(input())))))
for _ in range(int(input())):
    c, q, r, p = input().split(',')
    objects[q][1][c] = (int(r), int(p))
winners = set()
for competition in objects:
    winners.update(sorted(objects[competition][1], key=lambda x: (-objects[competition][1][x][0], objects[competition][1][x][1]))[:objects[competition][0]])
print(*sorted(winners), sep='\n')
