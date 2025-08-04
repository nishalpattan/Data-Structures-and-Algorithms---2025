# Last updated: 8/3/2025, 9:02:09 PM
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = list()
        to_remove = set()

        for idx, char in enumerate(s):
            if char == '(':
                stack.append(idx)
            elif char == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    to_remove.add(idx)
        
        to_remove.update(set(stack))

        output = list()

        for idx, char in enumerate(s):
            if idx not in to_remove:
                output.append(char)
        return "".join(output)
        