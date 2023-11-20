input()
sequence = list(map(int, input().split()))
advantage = sum(sequence)
prev = 0
for i in range(len(sequence)):
    advantage = advantage - (sequence[i] - prev) * (len(sequence) - 2 * i)
    prev = sequence[i]
    print(advantage, end=' ')
print()
