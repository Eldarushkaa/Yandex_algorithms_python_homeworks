from random import randint
from copy import deepcopy
from LCSM import choose_equal as fucker
from time import time


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


def generate_a1(l):
    l = randint(7, 10)
    a1 = [0] + [randint(1, 2) for _ in range(l)] + [1000]
    return a1


def generate_a2(a1):
    j = 0
    a2 = deepcopy(a1)
    while True:
        w = randint(1, 3)
        step = randint(1, 10)
        if j + step + w >= len(a2):
            break
        w_new = randint(1, 3)
        a2 = a2[:j + step] + [randint(1, 300) for _ in range(w_new)] + a2[j + step + w:]
        j = j + step + w
    return a2


def check(a1, a2, r1, r2):
    if len(r1) != len(r2):
        return False
    for i in range(len(r1)):
        if a1[r1[i]] != a2[r2[i]]:
            return False
    return True


NUMBER_OF_TESTS = 1000000
cube = 0
square = 0
pat = 0
total_time = 0
total_time_s = 0
for i in range(NUMBER_OF_TESTS):
    a1 = generate_a1(7)
    a2 = generate_a2(a1)
    total_time -= time()
    r1, r2 = choose_equal(a1, a2)
    total_time += time()
    total_time_s -= time()
    r1_s, r2_s = fucker(a1, a2)
    total_time_s += time()
    r_cor = check(a1, a2, r1, r2)
    r_cor_s = check(a1, a2, r1_s, r2_s)
    if len(r1) > len(r1_s):
        cube += 1
    elif len(r1) == len(r1_s):
        pat += 1
    else:
        square += 1
    if not r_cor or not r_cor_s or len(r1) > len(r1_s):
        print(a1, a2)
        print(r1, r2, len(r1))
        print(r1_s, r2_s, len(r1_s))
        print(r_cor, r_cor_s)
        break
    if (i + 1) % (NUMBER_OF_TESTS // 10) == 0:
        print(f'{NUMBER_OF_TESTS // (i + 1)}th part of 10 is done')
        print(f'Percentage of cases where square fucked cube: {100 * square / NUMBER_OF_TESTS}')
        print(f'Percentage of cases where answers has the same length: {100 * pat / NUMBER_OF_TESTS}')
        print(f'Percentage of cases where cube fucked square: {100 * cube / NUMBER_OF_TESTS}')
        print(f'Total time spent is {total_time + total_time_s}s, where square took {int(100 * total_time_s / (total_time + total_time_s))}% and cube {int(100 * total_time / (total_time + total_time_s))}%')
print(f'Testing is finished\nAmount of tests: {NUMBER_OF_TESTS}. Length is distributed between 50 and 500')
print(f'Percentage of cases where square fucked cube: {100 * square / NUMBER_OF_TESTS}')
print(f'Percentage of cases where answers has the same length: {100 * pat / NUMBER_OF_TESTS}')
print(f'Percentage of cases where cube fucked square: {100 * cube / NUMBER_OF_TESTS}')
print(f'Total time spent is {total_time + total_time_s}s, where square took {int(100 * total_time_s / (total_time + total_time_s))}% and cube {int(100 * total_time / (total_time + total_time_s))}%')
