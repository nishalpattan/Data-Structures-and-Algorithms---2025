# Last updated: 8/11/2025, 5:41:25 AM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # Intuition : use sliding window dynamic pattern
        # start representing the start of the window and end is ptr to exapnd the window
        # build running sum of the window as expanding
        # when is the constraint is satisfied, measure the length of window and compare to see if it is minimum length shrink the window size by taking the number at start index out of running sum and incrementing the start ptr
        # by the end return the min length
        # Time Complexity : O(n), Space Complexity : O(1)

        n = len(nums)
        start = 0
        curr_sum = 0
        min_len = float("inf")
        for end in range(n):
            curr_sum += nums[end]
            while curr_sum >= target:
                min_len = min(min_len, end-start+1)
                curr_sum -= nums[start]
                start += 1
        return min_len if min_len != float("inf") else 0
