# Last updated: 8/3/2025, 9:02:18 PM
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        r_max = arr[-1]
        for i in range(len(arr)-2,-1,-1):
            temp = arr[i]
            arr[i] = r_max
            if r_max < temp:
                r_max = temp
        arr[-1] = -1
        return arr
                