for i in range(int(input())):
    n, a, b = map(int, input().split())
    if (n % a) <= (n // a) * (b - a):
        print('YES')
    else:
        print('NO')
