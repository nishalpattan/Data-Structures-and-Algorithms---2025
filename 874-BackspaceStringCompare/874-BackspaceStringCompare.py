# Last updated: 8/3/2025, 9:02:50 PM
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        str_S = self.build_string(S)
        str_T = self.build_string(T)
        return str_S == str_T
    
    def build_string(self,s):
        stack = list() 
        for char in s:
            if stack and char == "#":
                stack.pop()
            else:
                if char != "#":
                    stack.append(char)
        return "".join(stack)
        