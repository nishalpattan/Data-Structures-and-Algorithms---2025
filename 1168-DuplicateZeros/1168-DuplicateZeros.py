# Last updated: 8/3/2025, 9:02:22 PM
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr_copy = []
        for i in arr:
            if i == 0:
                arr_copy.append(0)
                arr_copy.append(0)
            else:
                arr_copy.append(i)
        arr[:] = arr_copy[0:len(arr)]