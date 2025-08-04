# Last updated: 8/3/2025, 9:02:26 PM
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x : x[0] - x[1])
        threshold = len(costs) // 2
        total_cost = 0
        for idx,cost in enumerate(costs):
            if idx < threshold:
                total_cost += cost[0]
            else:
                total_cost += cost[1]
        return total_cost