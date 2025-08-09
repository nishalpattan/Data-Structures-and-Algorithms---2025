# Last updated: 8/9/2025, 5:44:54 AM
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # map to build window
        # calculate running sum and find max sum seen so far
        # when window becomes invalid map[s[end]] > 1 => shringk the window
        # return max_sum of unique values

        _sum = 0
        _max_sum = 0
        _map = defaultdict(int)
        start = 0
        n = len(nums)
        for end in range(n):
            _map[nums[end]] += 1
            _sum += nums[end]
            while _map[nums[end]] > 1:
                # shrink the window
                _map[nums[start]] -= 1
                _sum -= nums[start]
                if _map[nums[start]] == 0:
                    del _map[nums[start]]
                start += 1
            _max_sum = max(_max_sum, _sum)
        return _max_sum