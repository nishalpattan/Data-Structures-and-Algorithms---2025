# Last updated: 8/11/2025, 6:28:16 AM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
          # Intuition: Fixed window sliding window pattern
          # just like how char arrays are build for anagrams
        # build char array using ascii val for string p
        # keep start and end ptrs to keep track of the window
        # expand the window and build char array for s
        # when the window size is equal to the len(p) then stop expanding window
        # compare the char arrays of s and p and store the start index in the result array
        # shrink the window by decrementing the char array of s[start] and start + 1
        # return result
        char_array_s1 = [0] * 26
        char_array_s2 = [0] * 26
        start = 0
        res = list()
        for char in s1:
            char_array_s1[ord(char) - ord('a')] += 1
        for end in range(len(s2)):
            char = s2[end]
            char_array_s2[ord(char) - ord('a')] += 1
            if end - start + 1 == len(s1):
                if char_array_s2 == char_array_s1:
                    return True
                char_at_start = s2[start]
                char_array_s2[ord(char_at_start) - ord('a')] -= 1
                start += 1
        return False
