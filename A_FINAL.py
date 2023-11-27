def a():
    i = 1
    while 1:
        yield i**2
        i += 1


def b():
    i = 1
    while 1:
        yield i ** 3
        i += 1


A = a()
B = b()
prev_a = next(A)
prev_b = next(B)
x = int(input())
for i in range(x - 1):
    if prev_a == prev_b:
        prev_a = next(A)
        prev_b = next(B)
    elif prev_a < prev_b:
        prev_a = next(A)
    else:
        prev_b = next(B)
print(min(prev_a, prev_b))
