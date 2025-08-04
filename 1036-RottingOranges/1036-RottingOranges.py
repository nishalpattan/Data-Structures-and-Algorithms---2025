# Last updated: 8/3/2025, 9:02:31 PM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        time_to_rot = 0
        fresh_oranges = 0
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                else:
                    if grid[i][j] == 1:
                        fresh_oranges += 1
        while queue and fresh_oranges > 0:
            _len = len(queue)
            for _ in range(_len):
                curr_row, curr_col = queue.popleft()
                directions = [(-1,0), (0,-1), (1,0), (0,1)]
                for dir_row, dir_col in directions:
                    new_row, new_col = dir_row + curr_row, dir_col + curr_col
                    if 0 <= new_row <= len(grid) - 1 and 0<= new_col <= len(grid[0])- 1 and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        fresh_oranges -= 1
                        queue.append((new_row, new_col))
            time_to_rot += 1

        if fresh_oranges == 0:
            return time_to_rot
        else:
            return -1

