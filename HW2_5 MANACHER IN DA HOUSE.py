def longest_palindrome(s):
    manacher = '|' + '|'.join(s) + '|'
    palindromes = [0] * len(manacher)

    center = 0
    radius = 0

    while center < len(manacher):
        while center - radius - 1 >= 0 and center + radius + 1 < len(manacher) and manacher[center - radius - 1] == \
                manacher[center + radius + 1]:
            radius += 1

        palindromes[center] = radius

        old_center = center
        old_radius = radius

        center += 1
        radius = 0
        while center <= old_center + old_radius:
            mirrored_center = old_center - (center - old_center)
            max_mirrored_radius = old_center - center + old_radius
            if palindromes[mirrored_center] < max_mirrored_radius:
                palindromes[center] = palindromes[mirrored_center]
            elif palindromes[mirrored_center] > max_mirrored_radius:
                palindromes[center] = max_mirrored_radius
            else:
                radius = max_mirrored_radius
                break
            center += 1
    center = 0
    radius = palindromes[0]
    for i in range(len(palindromes)):
        if palindromes[i] > radius:
            center = i
            radius = palindromes[i]
    # print(center, radius, manacher, palindromes)
    center -= 1
    if radius % 2:
        start = center // 2 - radius // 2
        end = center // 2 + radius // 2 + 1
    else:
        start = center // 2 - radius // 2 + 1
        end = center // 2 + radius // 2 + 1
    return palindromes


print(sum(map(lambda x: (x + 1) // 2, longest_palindrome(input()))))
