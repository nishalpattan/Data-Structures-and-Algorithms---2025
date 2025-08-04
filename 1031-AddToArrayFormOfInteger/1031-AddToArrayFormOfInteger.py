# Last updated: 8/3/2025, 9:02:32 PM
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A[-1] += K
        carry = 0
        for i in range(len(A)-1, -1, -1):
            carry = A[i] // 10
            rem = A[i] % 10
            A[i] = rem
            if i:
                A[i-1] += carry
        while carry != 0:
            A.insert(0,carry % 10)
            carry = carry // 10
        return A