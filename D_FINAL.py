def permutation(target, current_sum, *args):
    global shortest_path
    prediction = 0
    predict_sum = current_sum
    while predict_sum < target:
        predict_sum += args[prediction]
        prediction += 1
    for i in range(len(args)):
        if current_sum + args[i] == target and len(lengths) - len(args) + 1 < shortest_path:
            shortest_path = len(lengths) - len(args) + 1
            yield str(args[i])
        elif len(lengths) - len(args) + prediction - 1 > shortest_path:
            break
        elif current_sum + args[i] < target:
            for seq in permutation(target, current_sum + args[i], *args[:i], *args[i+1:]):
                yield str(args[i]) + ' ' + seq


n, m = map(int, input().split())
lengths = list(map(int, input().split()))
lengths = sorted(lengths + lengths)
shortest_path = len(lengths) + 1
if sum(lengths) < n:
    print(-1)
else:
    option = ''
    for row in permutation(n, 0, *lengths):
        option = row

    if shortest_path == len(lengths) + 1:
        print(0)
    else:
        print(shortest_path)
        print(option)
