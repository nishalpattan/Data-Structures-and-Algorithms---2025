# Last updated: 8/3/2025, 9:02:42 PM
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        missing = 0
        open = 0
        for i in S:
            if i == '(':
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    missing += 1
                
        return missing + open