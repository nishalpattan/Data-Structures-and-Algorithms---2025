# Last updated: 8/3/2025, 9:02:05 PM
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        #Approach 1 : using boundaries
        count = 0
        for num in nums:
            if ((num > 9 and num <= 99) or (num > 999 and num <= 9999) or (num == 10**5) ):
                count += 1
        return count
    # Approach 2 : len of str(int); TC : O(n); SC: O(1)
        # count = 0
        # for num in nums:
        #     if len(str(num)) % 2 ==0:
        #         count += 1
        # return count
    # approach 3 : counting nums; TC : O(n); SC:O(1)
    #     even_count = 0
    #     for i in nums:
    #         count = self.countOfInteger(i)
    #         if count % 2 == 0:
    #             even_count += 1
    #     return even_count
    # def countOfInteger(self, num: int) -> int:
    #     count = 1
    #     while num // 10 != 0:
    #         count += 1
    #         num = num //10
    #     return count