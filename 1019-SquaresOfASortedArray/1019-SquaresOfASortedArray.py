# Last updated: 8/3/2025, 9:02:35 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = list()

        negative_nums = list()
        positive_nums = list()
        for num in nums:
            if num < 0: negative_nums.append(num * num)
            else: positive_nums.append(num * num)
        
        negative_nums = negative_nums[::-1]
        positive_tracker = 0
        negative_tracker = 0

        while positive_tracker < len(positive_nums) and negative_tracker < len(negative_nums):
            if positive_nums[positive_tracker] <= negative_nums[negative_tracker]:
                result.append(positive_nums[positive_tracker])
                positive_tracker += 1
            elif positive_nums[positive_tracker] > negative_nums[negative_tracker]:
                result.append(negative_nums[negative_tracker])
                negative_tracker += 1
        
        if negative_tracker < len(negative_nums):
            while negative_tracker < len(negative_nums):
                result.append(negative_nums[negative_tracker])
                negative_tracker += 1
        
        if positive_tracker < len(positive_nums):
            while positive_tracker < len(positive_nums):
                result.append(positive_nums[positive_tracker])
                positive_tracker += 1
        
        return result
