# Last updated: 8/9/2025, 8:49:01 PM
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = list()
        counter = collections.Counter(nums)
        for num, freq in counter.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [num for freq, num in min_heap]