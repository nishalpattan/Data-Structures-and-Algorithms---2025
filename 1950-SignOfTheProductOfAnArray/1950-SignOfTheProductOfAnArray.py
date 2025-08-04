# Last updated: 8/3/2025, 9:01:53 PM
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            product = num * product
        return self.signFunc(product)
    def signFunc(self, product):
        if product < 0:
            return -1
        elif product == 0:
            return 0
        else:
            return 1
        