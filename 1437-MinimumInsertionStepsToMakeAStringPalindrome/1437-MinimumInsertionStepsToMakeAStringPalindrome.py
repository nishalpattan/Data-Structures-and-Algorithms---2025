# Last updated: 8/3/2025, 9:02:04 PM
class Solution:
    def minInsertions(self, s: str) -> int:
        # Dynamic Programming; TC : O(n^2); SC : O(n^2) using Longest Common SubSequence
        # https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/discuss/470709/JavaPython-3-DP-longest-common-subsequence-w-brief-explanation-and-analysis.
        return len(s) - self.lcs(s, s[::-1])
    
    def lcs(self, s, r):
        m = len(s) + 1
        n = len(r) + 1
        dp = [[0] * n for _ in range(m)]
        
        for i,a in enumerate(s): 
            for j,b in enumerate(r):
                if a == b:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[m-1][n-1]
                
        