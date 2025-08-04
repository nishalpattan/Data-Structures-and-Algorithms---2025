# Last updated: 8/3/2025, 9:02:57 PM
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) == 0 and len(B) == 0:
            return True
        elif len(A) == 0 or len(B) == 0:
            return False
        for i in range(len(A)):
            temp = A[i+1:] + A[:i+1]
            if temp == B:
                return True
        return False