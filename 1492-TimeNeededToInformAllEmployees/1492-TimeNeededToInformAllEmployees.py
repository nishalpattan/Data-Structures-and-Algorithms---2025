# Last updated: 8/3/2025, 9:01:59 PM
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """
        https://leetcode.com/problems/time-needed-to-inform-all-employees
        TC : O(N)
        SC : O(N)
        N --> number of employees
        """
        subs = [[] for i in range(n)]
        for i in range(n):
            if manager[i] >= 0:
                subs[manager[i]].append(i)
        return self.dfs(headID, subs, informTime)
    
    def dfs(self, id, subs, informTime):
        max_time = 0
        for sub_id in subs[id]:
            max_time = max(max_time, informTime[id] + self.dfs(sub_id, subs, informTime))
        return max_time