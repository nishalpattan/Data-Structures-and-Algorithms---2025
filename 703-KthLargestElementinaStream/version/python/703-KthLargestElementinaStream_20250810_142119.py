# Last updated: 8/10/2025, 2:21:19 PM
import heapq
class KthLargest:
    """
    instead of addind the element to the stream, I can first create the min heap from the available elements as the stream keeps growing but the min heap is of fixed length, when adding new element I can just add it to the min heap and if the length of min heap exceeds k I can just pop the 0th element from the minheap which is O(log K ) operation only and adding to heap as well O(log K)
    """

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
        if len(self._min_heap) > self.size:
            heapq.heappop(self._min_heap)
        return self._min_heap[0]
       

        




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)