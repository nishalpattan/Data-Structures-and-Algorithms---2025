# Last updated: 8/10/2025, 1:47:40 PM
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self._min_heap = self._create_min_heap_k_size(nums)
    
    def _create_min_heap_k_size(self, stream):
        min_heap = list()
        for num in stream:
            heapq.heappush(min_heap, num)

            if len(min_heap) > self.size:
                heapq.heappop(min_heap)
        return min_heap
        

    def add(self, val: int) -> int:
        heapq.heappush(self._min_heap, val)
        while len(self._min_heap) > self.size:
            heapq.heappop(self._min_heap)
        return self._min_heap[0]
       

        




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)