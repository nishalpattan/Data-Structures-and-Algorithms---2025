# Last updated: 8/3/2025, 9:02:03 PM
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # One Pass approach, TC : O(n); SC: O(n)
        hash_set = set()
        for num in arr:
            if ((2 * num in hash_set) or (num % 2 == 0 and num // 2 in hash_set)):
                return True
            hash_set.add(num)
        return False
        # Two Pass Approach, TC: O(n); SC : O(n)
        # hash_set = set()
        # _sum = sum(arr)
        # if _sum == 0:
        #     return True
        # for i in arr:
        #     hash_set.add(i)
        # for num in hash_set:
        #     if num !=0 and 2*num in hash_set:
        #         return True
        # return False