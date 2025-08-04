# Last updated: 8/3/2025, 9:02:52 PM
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        # flip image horizantally
        for idx, row in enumerate(A):
            A[idx] = row[::-1]
        
        # invert binaries in each row
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] = int(not(A[i][j]))
        return A
            
        