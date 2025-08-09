# Last updated: 8/8/2025, 7:53:36 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 0: return 0
        n = len(nums)
        _sum = 0
        _max_avg = float("-inf")
        start = 0
        for end in range(len(nums)):
            _sum += nums[end]
            _avg = _sum / (end -start + 1)
            if end - start + 1 == k:
                if _avg >= _max_avg:
                    _max_avg = _avg
                _sum -= nums[start]
                start += 1
        return _max_avg
