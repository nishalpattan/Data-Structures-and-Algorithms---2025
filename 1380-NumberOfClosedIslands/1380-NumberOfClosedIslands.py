# Last updated: 8/3/2025, 9:02:08 PM
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for value in row] for row in grid]
        num_closed_islands = 0
        for i in range(len(grid)-1):
            for j in range(len(grid[i])-1):
                if grid[i][j] == 0 and not visited[i][j]:
                    if self.is_closed_island(grid,visited,i,j):
                        num_closed_islands += 1
        return num_closed_islands
    def is_closed_island(self,grid,visited,i,j):
        if  visited[i][j] or grid[i][j] == 1:
            return True
        if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[0])-1:
            return False
        
        visited[i][j] = True
        left = self.is_closed_island(grid,visited,i-1,j) 
        right = self.is_closed_island(grid,visited,i+1,j) 
        top = self.is_closed_island(grid,visited,i,j-1) 
        bottom = self.is_closed_island(grid,visited,i,j+1)
        return right and left and top and bottom