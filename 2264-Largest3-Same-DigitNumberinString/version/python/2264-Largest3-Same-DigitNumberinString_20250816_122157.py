# Last updated: 8/16/2025, 12:21:57 PM
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_num = float("-inf")
        longest_num_string = ""
        for idx in range(len(num)-2):
            if num[idx] == num[idx+1] == num[idx+2]:
                if max_num < int(num[idx:idx+3]):
                    max_num = int(num[idx:idx+3])
                    longest_num_string = num[idx:idx+3]
        return longest_num_string