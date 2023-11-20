n, m = map(int, input().split())
square = [list(map(int, input().split())) for i in range(n)]
answer = 0
for i in range(1, n):
    for j in range(1, m):
        if square[i - 1][j] and square[i - 1][j - 1] and square[i][j - 1] and square[i][j]:
            square[i][j] = min(square[i - 1][j - 1], square[i - 1][j], square[i][j - 1]) + 1
            answer = max(answer, square[i][j])
print(answer)
