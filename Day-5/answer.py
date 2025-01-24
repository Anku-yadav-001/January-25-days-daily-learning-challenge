def longest_common_subsequence(str1, str2):
    n, m = len(str1), len(str2)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:  
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[n][m]

virat_text = input().strip()
rohit_text = input().strip()

lcs_length = longest_common_subsequence(virat_text, rohit_text)
print(lcs_length)
