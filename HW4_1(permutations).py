def permutation(*args):
    if len(args) == 1:
        yield args[0]
    else:
        for i in range(len(args)):
            for seq in permutation(*args[:i], *args[i+1:]):
                yield args[i] + seq


for row in permutation(*(str(i + 1) for i in range(int(input())))):
    print(row)
