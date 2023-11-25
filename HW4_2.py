def queens(n, column, *args):
    if column == n:
        return 1
    legit = [1] * n
    for i, queen in enumerate(args):
        legit[queen] = 0
        if 0 <= i + queen - column < n:
            legit[i + queen - column] = 0
        if 0 <= queen - i + column < n:
            legit[queen - i + column] = 0
    total_queens = 0
    for i in range(n):
        if legit[i]:
            total_queens += queens(n, column + 1, *args, i)
    return total_queens


print(queens(int(input()), 0))
