def count_substrings(s):
    n = len(s)
    dp = [[False] * n for i in range(n)]
    for i in range(n):
        dp[i][i] = True
    for i in range(n - 1):
        dp[i][i + 1] = (s[i] == s[i + 1])
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            dp[i][i + length - 1] = dp[i + 1][i + length - 2] and (s[i] == s[i + length - 1])
    palindromes = 0
    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                palindromes += 1
    return palindromes


print(count_substrings(input()))
