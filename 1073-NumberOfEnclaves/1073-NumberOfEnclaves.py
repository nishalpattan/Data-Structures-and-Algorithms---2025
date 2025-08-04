# Last updated: 8/3/2025, 9:02:30 PM
class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        if A == []:
            return 0
        count = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i == 0 or j == 0 or i == len(A) - 1 or j == len(A[0]) - 1:
                    self.dfs(i, j, A)
    
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    count += 1
        
        return count
    def dfs(self, row, col, A):
        if row < 0 or col < 0 or row >= len(A) or col >= len(A[0]) or A[row][col] != 1:
            return
        A[row][col] = 0
        self.dfs(row-1, col, A)
        self.dfs(row+1, col, A)
        self.dfs(row, col-1, A)
        self.dfs(row, col+1, A)