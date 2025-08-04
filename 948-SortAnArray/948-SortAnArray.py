# Last updated: 8/3/2025, 9:02:42 PM
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Approach : Quick Sort, TC : O(n logn)
        self.quick_sort(0, len(nums)-1, nums)
        return nums
    
        # Approach : Bubble Sort, TC: O(n^2), SC:O(1)
        # is_sorted = False
        # n = len(nums) - 1
        # while not is_sorted:
        #     is_sorted = True
        #     for idx in range(n):
        #         if nums[idx] > nums[idx+1]:
        #             nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
        #             is_sorted = False
        #     n-=1
        # return nums
    def quick_sort(self, left, right, nums):
        if left >= right:
            return
        pivot = nums[(left+right) // 2]
        partition_idx = self.partition(left, right, pivot, nums)
        self.quick_sort(left, partition_idx-1, nums)
        self.quick_sort(partition_idx, right, nums)
        
    def partition(self, left, right, pivot, nums):
        while left <= right:
            while nums[left] < pivot:
                left += 1
            while nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right] , nums[left]
                left += 1
                right -= 1
        return left