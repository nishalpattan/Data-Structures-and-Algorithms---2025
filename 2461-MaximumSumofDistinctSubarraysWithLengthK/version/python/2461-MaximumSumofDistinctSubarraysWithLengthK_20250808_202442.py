# Last updated: 8/8/2025, 8:24:42 PM
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
             return 0
        _sum = 0
        _map = defaultdict(int)
        _max_sum = 0
        start = 0
        n = len(nums)
        for end in range(n):
            _sum += nums[end]
            _map[nums[end]] += 1

            if end - start + 1 == k:
                if len(_map) == k:
                    _max_sum = max(_sum, _max_sum)
                _sum -= nums[start]
                _map[nums[start]] -= 1
                if _map[nums[start]] == 0:
                    del _map[nums[start]]
                start += 1
        return _max_sum
