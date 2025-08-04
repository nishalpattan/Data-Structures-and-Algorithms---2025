# Last updated: 8/3/2025, 9:02:43 PM
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        start = 0
        end = len(A) -1 
        while start < end:
            if A[start] % 2 != 0 and A[end] % 2 == 0:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
            elif A[start] % 2 == 0:
                start += 1
            elif A[end] % 2 != 0:
                end -= 1
        return A