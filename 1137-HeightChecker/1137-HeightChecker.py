# Last updated: 8/3/2025, 9:02:24 PM
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Approach : O(nlogn)
        sorted_heights = sorted(heights)
        count = 0
        for idx,val in enumerate(heights):
            if val != sorted_heights[idx]:
                count += 1
        return count