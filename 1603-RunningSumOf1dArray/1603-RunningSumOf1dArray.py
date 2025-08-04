# Last updated: 8/3/2025, 9:01:56 PM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr_sum = nums[0]
        for idx in range(1, len(nums)):
            curr_sum += nums[idx] 
            nums[idx] = curr_sum
        return nums