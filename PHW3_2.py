n = int(input())
originals = dict()
for i in range(n):
    song = input().split(' | ')
    if song[0] in originals and song[2] < originals[song[0]][1] or song[0] not in originals:
        originals[song[0]] = song[1:]

for name in sorted(originals, key=lambda x: originals[x][0] + x):
    print(originals[name][0] + ' - ' + name)
