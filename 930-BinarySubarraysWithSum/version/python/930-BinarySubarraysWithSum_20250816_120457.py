# Last updated: 8/16/2025, 12:04:57 PM
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        idx i, j=i+1
        nested loop: O(n^2)

        [1,0,1,0,1] # sum > target

        sliding window: O(n)

        exact sum =  < sum and < sum -1
        
        """

        def sliding_window_atmost_target(nums, target):

            start = 0
            n = len(nums) # 4
            _sum = 0 # [1,0,1,0,1] 2
            count = 0
            for end in range(n): # 0, 1
                _sum += nums[end] # 1
                while start <= end and _sum > target: # 1<2
                    _sum -= nums[start]
                    start += 1
                count += end - start + 1 # 3

            return count
        
        return sliding_window_atmost_target(nums, goal) - sliding_window_atmost_target(nums, goal - 1)
                
