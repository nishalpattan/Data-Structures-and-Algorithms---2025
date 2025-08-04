# Last updated: 8/3/2025, 9:02:25 PM
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = list()
        for char in S:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
                