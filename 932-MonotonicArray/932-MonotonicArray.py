# Last updated: 8/3/2025, 9:02:44 PM
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc_flag = True
        dec_flag = True
        # Approach : One Pass
        for i in range(len(A)-1):
            if not(A[i+1] >= A[i]):
                inc_flag = False
            if not(A[i+1] <= A[i]):
                dec_flag = False
        return inc_flag or dec_flag
        # Approach : two pass
        # for i in range(len(A)-1):
        #     if not(A[i+1] >= A[i]):
        #         inc_flag = False
        #         break
        # for i in range(len(A)-1):
        #     if not(A[i+1] <= A[i]):
        #         dec_flag = False
        #         break
        # return inc_flag or dec_flag