def choose_equal(a1, a2):
    # using dynamic programing firstly find LCS, O(n*m) time and space complexity, where n = len(a1) and m = len(a2)
    def longest_common_subsequence(text1, text2):
        def filling(mat, x, y):
            for i in range(x, len(text2)):
                mat[i + 1][y] = mat[i][y]
            for j in range(y, len(text1)):
                mat[x][j + 1] = mat[x][j]
        table = [[0] * (len(text1) + 1) for i in range(len(text2) + 1)]
        mask = [[0] * (len(text1) + 1) for i in range(len(text2) + 1)]
        for i in range(len(text2) - 1):
            for j in range(len(text1) - 1):
                if text2[i] == text1[j] and not mask[i][j]:
                    table[i + 1][j + 1] = table[i][j] + 1
                    if text2[i + 1] != text1[j + 1]:
                        mask[i + 1][j + 1] = 1
                        filling(mask, i + 1, j + 1)
                    else:
                        mask[i + 1][j + 1] = 0
                        filling(mask, i + 1, j + 1)
                else:
                    table[i + 1][j + 1] = max(table[i + 1][j], table[i][j + 1])
        common_seq = []
        i, j = len(text2) - 1, len(text1) - 1
        while i > 0 and j > 0:
            if table[i][j] == table[i - 1][j]:
                i -= 1
            elif table[i][j] == table[i][j - 1]:
                j -= 1
            else:
                common_seq.append(text2[i - 1])
                i -= 1
                j -= 1
        return list(reversed(common_seq)) + [text1[-1]]
    a_common = longest_common_subsequence(a1, a2)
    # print(a_common)
    # now we find the entrances of a_common to a1 and a2
    equal_a1 = []
    equal_a2 = []
    ia1 = ia2 = 0
    for x in a_common:
        while a1[ia1] != x: ia1 += 1
        equal_a1.append(ia1)
        while a2[ia2] != x: ia2 += 1
        equal_a2.append(ia2)
    return equal_a1, equal_a2


seq_origin = [0, 29, 6, 7, 13, 29, 4, 6, 4, 29, 77]
seq_tokenized = [0, 34, 7, 29, 4, 33, 45, 4, 4, 6, 7, 4, 29, 77]

for row in choose_equal(seq_origin, seq_tokenized):
    print(row)

seq_origin = [1, 3, 6, 4]
seq_tokenized = [1, 2, 3, 4]

for row in choose_equal(seq_origin, seq_tokenized):
    print(row)
