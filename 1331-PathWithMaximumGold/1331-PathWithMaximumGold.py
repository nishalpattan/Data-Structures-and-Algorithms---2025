# Last updated: 8/3/2025, 9:02:10 PM
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        visited = [[False for col in row] for row in grid]
        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0 :
                    curr_gold = self.dfs(i, j, 0, grid, visited)
                    max_gold = max(curr_gold, max_gold)
        return max_gold
    
    def dfs(self, i, j, gold, grid, visited):
        if i < 0 or j <0 or i >= len(grid) or j >= len(grid[0]) or visited[i][j] or grid[i][j] == 0:
            return gold
        
        gold += grid[i][j] 
        visited[i][j] = True
        top = self.dfs(i-1, j, gold, grid, visited)
        down = self.dfs(i+1, j, gold, grid, visited)
        left = self.dfs(i, j-1, gold, grid, visited)
        right = self.dfs(i, j+1, gold, grid, visited)
        visited[i][j] = False
        return max(top, down, right, left)
        
        
        
        