# Last updated: 8/14/2025, 2:24:18 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        char_array = [0] * 26

        for idx in range(n):
            char_s = s[idx]
            char_t = t[idx]
            char_array[ord(char_s) - ord('a')] += 1
            char_array[ord(char_t) - ord('a')] -= 1
        for val in char_array:
            if val != 0:
                return False
        return True
            