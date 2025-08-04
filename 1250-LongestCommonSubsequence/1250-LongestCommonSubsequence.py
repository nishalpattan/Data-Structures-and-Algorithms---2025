# Last updated: 8/3/2025, 9:02:15 PM
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            text1, text2 = text2, text1
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n+1) for _ in range(m + 1)]
        
        for i,a in enumerate(text1):
            for j,b in enumerate(text2):
                if a == b:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[m][n]