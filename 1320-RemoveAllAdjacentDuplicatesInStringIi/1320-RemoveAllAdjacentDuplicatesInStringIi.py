# Last updated: 8/3/2025, 9:02:11 PM
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) == 0: return ""
        if k == 0: return s

        stack = list()
        res = ""
        for char in s:
            if stack and char == stack[-1][0] and stack[-1][1] + 1 == k:
                 stack.pop()
            else:
                if stack and stack[-1][0] == char:
                    stack[-1][1] += 1
                else:
                    stack.append([char, 1])
        for item in stack:
            char, freq = item[0], item[1]
            res += char * freq
        return res

        