# Last updated: 8/3/2025, 9:02:49 PM
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        
        # Binary Search
        start = 0 
        end = len(A) - 1
        while start < end:
            mid = start + (end-start) // 2
            if A[mid] > A[mid + 1]:
                end = mid
            else:
                start = mid + 1
        return start
        # BruteForce ; TC : O(n); SC:O(1)
        # for idx in range(1, len(A)-1):
        #     if A[idx-1] < A[idx] > A[idx+1]:
        #         return idx