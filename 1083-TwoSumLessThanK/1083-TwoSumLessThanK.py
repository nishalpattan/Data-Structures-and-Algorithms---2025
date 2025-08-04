# Last updated: 8/3/2025, 9:02:28 PM
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0 
        end = len(nums)-1
        max_sum = -1
        while start < end:
            curr_sum = nums[start] + nums[end]
            if curr_sum < k:
                max_sum = max(curr_sum, max_sum)
            if curr_sum >= k:
                end -=1
            else:
                start += 1
        
        return max_sum
             