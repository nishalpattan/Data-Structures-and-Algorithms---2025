# Last updated: 8/8/2025, 9:40:49 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _max_len = 0
        n = len(s)
        _map = defaultdict(int)
        start = 0
        for end in range(n):
            _map[s[end]] += 1
            while _map[s[end]] > 1:
                _map[s[start]] -= 1
                if _map[s[start]] == 0:
                    del _map[s[start]]
                start += 1
            _max_len = max(_max_len, end-start+1)
        return _max_len