# Last updated: 8/8/2025, 10:30:03 AM
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * (len(nums))

        def helper(idx):
            # base
            if idx == 0:
                return nums[0]
            if idx == 1:
                return max(nums[0], nums[1])
            
            # precompute check
            if dp[idx] != -1:
                return dp[idx]
            
            # take or not take
            take_idx = nums[idx] + helper(idx-2)
            not_take_idx = helper(idx-1)
            dp[idx] = max(take_idx, not_take_idx)

            return dp[idx]
        return helper(len(nums)-1)

