# Last updated: 8/10/2025, 10:49:24 AM
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # idea is to use max_heap to store the stones by weight
        # as python only supports min heap by default we store -weight to make it max heap
        # loop through the max heap get first and second heaviest weights
        # if stone weights are not equal take the difference and store it in the max heap

        if len(stones) == 0: return 0
        max_heap = list()
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) > 1:
            first = abs(heapq.heappop(max_heap))
            second = abs(heapq.heappop(max_heap))
            if first == second: continue
            new_stone = first - second
            heapq.heappush(max_heap, -new_stone)
        if len(max_heap) == 0:
            return 0
        return -max_heap[0]