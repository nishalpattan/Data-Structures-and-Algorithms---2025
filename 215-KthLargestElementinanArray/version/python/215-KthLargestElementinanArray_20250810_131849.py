# Last updated: 8/10/2025, 1:18:49 PM
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    # Intuition:
    # this can be solved using sorting the input array in acending order and return k-1 th element
    # but the catch is its time complexity is O(n logn)
    # this can be optimized further by using min heaps
    # heaps length can be restricted to K at all times and storing the element in a heap is always logK
    # so using heaps this  can be done in O(N logK)
    # ides is to go through the array and store the element in the min heap if the length of min heap is greater than K
    # pop the element out of it
    # by end return the 0th element of min heap
        min_heap = list()
        for num in nums:
            heapq.heappush(min_heap, num)

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
    




        