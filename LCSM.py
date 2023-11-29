def choose_equal(a1, a2):
    # using dynamic programing firstly find LCS, O(n*m) time and space complexity, where n = len(a1) and m = len(a2)
    def filling(mat, x, y, limit=float('inf')):
        for i in range(x, len(a2)):
            if mat[i + 1][y] >= mat[i][y]:
                break
            mat[i + 1][y] = mat[i][y]
        for j in range(y, len(a1)):
            if mat[x][j + 1] >= mat[x][j]:
                break
            mat[x][j + 1] = mat[x][j]
    table = [[0] * (len(a1) + 1) for i in range(len(a2) + 1)]
    mask = [[0] * (len(a1) + 1) for i in range(len(a2) + 1)]
    for i in range(len(a2) - 1):
        if i == 4:
            print('Table:')
            for row in table:
                print(row)
            print('\nMask:')
            for row in mask:
                print(row)
            ...
        for j in range(len(a1) - 1):
            if a2[i] == a1[j] and (table[i][j] > mask[i][j] or not mask[i][j]):
                table[i + 1][j + 1] = table[i][j] + 1
                if a2[i + 1] != a1[j + 1]:
                    if table[i + 1][j + 1] > max(table[i + 1][j], table[i][j + 1]) and mask[i + 1][j + 1] < table[i + 1][j + 1]:
                        mask[i + 1][j + 1] = table[i + 1][j + 1]
                        filling(mask, i + 1, j + 1)
                else:
                    mask[i + 1][j + 1] = 0
                    filling(mask, i + 1, j + 1)
            else:
                table[i + 1][j + 1] = max(table[i + 1][j], table[i][j + 1])
                if mask[i + 1][j + 1] and (table[i + 1][j] >= table[i][j + 1] and not mask[i + 1][j] or table[i + 1][j] <= table[i][j + 1] and not mask[i][j + 1]):
                    mask[i + 1][j + 1] = 0
    print('Table:')
    for row in table:
        print(row)
    print('\nMask:')
    for row in mask:
        print(row)
    print(len(table), len(table[0]))
    ind_a1, ind_a2 = [], []
    i, j = len(a2) - 1, len(a1) - 1
    while i > 0 and j > 0:
        if table[i][j] == table[i - 1][j]:
            i -= 1
        elif table[i][j] == table[i][j - 1]:
            j -= 1
        else:
            ind_a2.append(i - 1)
            ind_a1.append(j - 1)
            i -= 1
            j -= 1
    equal_a1, equal_a2 = list(reversed(ind_a1)) + [len(a1) - 1], list(reversed(ind_a2)) + [len(a2) - 1]
    return equal_a1, equal_a2


# seq_origin = [0, 29, 6, 7, 13, 29, 4, 6, 4, 29, 77]
# seq_tokenized = [0, 34, 7, 29, 4, 33, 45, 4, 4, 6, 7, 4, 29, 77]
#
# for row in choose_equal(seq_origin, seq_tokenized):
#     print(row)
#
# seq_origin = [1, 3, 6, 4]
# seq_tokenized = [1, 2, 3, 4]
#
# for row in choose_equal(seq_origin, seq_tokenized):
#     print(row)


seq_origin = [0, 2, 1, 2, 1, 2, 1, 2, 2, 1, 1000]
seq_tokenized = [0, 288, 2, 1, 2, 2, 63, 2, 170, 1, 1000]

for row in choose_equal(seq_origin, seq_tokenized):
    print(row, len(row))
