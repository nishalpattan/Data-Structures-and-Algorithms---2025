# Last updated: 8/3/2025, 9:02:07 PM
class Solution:
    def countElements(self, arr: List[int]) -> int:
        hash_set = set()
        count = 0
        hash_set = set(arr)
        for num in arr:
            if num + 1 in hash_set:
                count += 1
        return count