# Last updated: 8/3/2025, 9:02:31 PM
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        min_steps = 0
        while Y > X:
            if Y % 2 != 0:
                Y += 1
            else:
                Y //= 2
            min_steps += 1
        return min_steps + (X - Y)