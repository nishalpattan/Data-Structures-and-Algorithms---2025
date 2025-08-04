# Last updated: 8/3/2025, 9:02:12 PM
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)
        stack = list()
        for idx in range(len(heights)-1, -1, -1):
            while stack and heights[idx] > stack[-1]:
                stack.pop()
                ans[idx] += 1

            if stack:
                ans[idx] += 1

            stack.append(heights[idx])
        return ans
