data = [input() for i in range(int(input()))]
print('Initial array:\n', ', '.join(data), '\n**********', sep='')
for i in range(len(data[0]) - 1, -1, -1):
    print('Phase', len(data[0]) - i)
    bucket = [0] * 10
    for j in range(len(data)):
        bucket[int(data[j][i])] += 1
    starts = [0] * 10
    for j in range(9):
        starts[j + 1] = starts[j] + bucket[j]
    new_data = [''] * len(data)
    for j in range(len(data)):
        new_data[starts[int(data[j][i])]] = data[j]
        starts[int(data[j][i])] += 1
    data = new_data
    print('Bucket 0: ', end='')
    if starts[0]:
        print(', '.join(data[:starts[0]]))
    else:
        print('empty')
    for j in range(1, 10):
        print(f'Bucket {j}: ', end='')
        if starts[j] - starts[j - 1]:
            print(', '.join(data[starts[j - 1]:starts[j]]))
        else:
            print('empty')
    print('**********')
print('Sorted array:\n', ', '.join(data), sep='')
