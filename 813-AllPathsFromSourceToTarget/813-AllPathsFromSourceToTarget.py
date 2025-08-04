# Last updated: 8/3/2025, 9:02:56 PM
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        BackTracking :
        TC : O(N * 2 ^ N)
        SC : O(N * 2 ^ N)
        """
        res = list()
        self.back_track(0, [0], res, graph)
        return res
    def back_track(self, start_idx, temp, res, graph):
        if start_idx == len(graph) - 1:
            res.append(temp[:])
        
        for idx in graph[start_idx]:
            temp.append(idx)
            self.back_track(idx, temp, res, graph)
            temp.pop()