def longestCommonSubsequence(text1: str, text2: str) -> int:
    l1, l2 = len(text1), len(text2)
    dp = [[0 for _ in range(l1)] for _ in range(l2)]
    for i in range(l1):
        if text2[0] in text1[:i+1]:
            dp[0][i] = 1
    for j in range(l2):
        if text1[0] in text2[:j+1]:
            dp[j][0] = 1
    
    for i in range(1, l2):
        for j in range(1, l1):
            if text2[i] == text1[j]:
                dp[i][j] =  dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[l2-1][l1-1] 
    
text1, text2 = "abcde", "ace"
print(longestCommonSubsequence(text1, text2))