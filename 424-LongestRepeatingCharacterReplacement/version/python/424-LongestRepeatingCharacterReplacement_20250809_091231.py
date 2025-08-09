# Last updated: 8/9/2025, 9:12:31 AM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        hash_map = defaultdict(int)
        start = 0
        n = len(s)
        for end in range(n):
            hash_map[s[end]] += 1
            while end - start + 1 - max(hash_map.values()) > k: # how do I know that my window is a valid one 
                hash_map[s[start]] -= 1
                if hash_map[s[start]] == 0:
                    del hash_map[s[start]]
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len