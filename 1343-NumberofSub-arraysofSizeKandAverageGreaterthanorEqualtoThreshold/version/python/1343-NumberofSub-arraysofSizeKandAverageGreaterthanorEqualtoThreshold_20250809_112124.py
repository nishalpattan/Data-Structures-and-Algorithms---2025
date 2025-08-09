# Last updated: 8/9/2025, 11:21:24 AM
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) == 0:
            return 0
        _max_avg = 0
        _sum = 0
        count = 0
        start = 0
        n = len(arr)
        for end in range(n):
            _sum += arr[end]
            curr_avg = _sum // (end - start + 1)
            if end - start + 1 == k:
                if curr_avg >= threshold:
                    count += 1
                _sum -= arr[start]
                start += 1
        return count 
