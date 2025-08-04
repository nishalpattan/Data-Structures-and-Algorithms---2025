# Last updated: 8/3/2025, 9:01:55 PM
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        if len(heights) ==0: return []
        output = list()
        max_height_seen_so_far = float("-inf")
        for i in range(len(heights)-1, -1, -1):
            curr_height = heights[i]
            if curr_height > max_height_seen_so_far:
                max_height_seen_so_far = curr_height
                output.append(i)
        return output[::-1]

        # check this link for meta variants https://leetcode.com/problems/buildings-with-an-ocean-view/solutions/6438919/meta-variants
        # variant 1.) traverse from only left side of the input list
        # variant 2.) what if the ocean is on both sides left, right