def choose_equal(a1, a2):
    equal_a1, equal_a2 = [], []
    i, j = 0, 0
    while j < len(a2):
        if a1[i] == a2[j]:
            equal_a1.append(i)
            equal_a2.append(j)
            i += 1
            j += 1
            continue
        else:
            i += 1
            j += 1
        best_rest, best_k, best_l = 10**20, -1, -1
        for l in range(j, len(a2)):
            rest = 10**20
            for k in range(i, len(a1)):
                if a1[k] == a2[l]:
                    rest = l - i + k - j
                    break
            if rest < best_rest:
                best_rest, best_k, best_l = rest, k, l
        if best_rest == 10**20:
            if len(a1) - 1 not in equal_a1:
                equal_a1.append(len(a1) - 1)
            if len(a2) - 1 not in equal_a2:
                equal_a2.append(len(a2) - 1)
            break
        equal_a1.append(best_k)
        equal_a2.append(best_l)
        i = best_k + 1
        j = best_l + 1
    return equal_a1, equal_a2


r1, r2 = choose_equal([0, 199, 180, 165, 232, 57, 68, 216, 1000], [0, 226, 201, 216, 1, 247, 232, 57, 257, 16, 236, 181, 289, 5, 216, 1000])
print(r1, r2)
