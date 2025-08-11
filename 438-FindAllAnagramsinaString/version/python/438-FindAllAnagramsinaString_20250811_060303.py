# Last updated: 8/11/2025, 6:03:03 AM
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Intuition: Fixed window sliding window pattern
        # build char array using ascii val for string p
        # keep start and end ptrs to keep track of the window
        # expand the window and build char array for s
        # when the window size is equal to the len(p) then stop expanding window
        # compare the char arrays of s and p and store the start index in the result array
        # shrink the window by decrementing the char array of s[start] and start + 1
        # return result
        char_array_s = [0] * 26
        char_array_p = [0] * 26
        start = 0
        res = list()
        for char in p:
            char_array_p[ord(char) - ord('a')] += 1
        for end in range(len(s)):
            char = s[end]
            char_array_s[ord(char) - ord('a')] += 1
            if end - start + 1 == len(p):
                if char_array_s == char_array_p:
                    res.append(start)
                char_at_start = s[start]
                char_array_s[ord(char_at_start) - ord('a')] -= 1
                start += 1
        return res
