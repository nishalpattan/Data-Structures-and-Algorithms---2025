# Last updated: 8/9/2025, 6:24:27 AM
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # dynamic sliding window pattern
        # build the window and keep adding the char to hash_map with its frequency
        # window is invliad when freq of char is greater than K
        # shrink the window when it becomes invalid, decrease freq in map
        # increment the start of window
        # calculate max len of substring end - start + 1
        n = len(s)
        max_len = 0
        start = 0
        hash_map = defaultdict(int)
        for end in range(n):
            hash_map[s[end]] += 1
            while len(hash_map) > k:
                hash_map[s[start]] -= 1
                if hash_map[s[start]] == 0:
                    del hash_map[s[start]]
                start += 1
            max_len = max(max_len, end-start+1)
        return max_len
