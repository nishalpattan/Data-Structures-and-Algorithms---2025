# Last updated: 8/3/2025, 9:02:16 PM
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = list()
        for i in range(1, len(nums),2):
            res += [nums[i]] * nums[i-1]
        return res