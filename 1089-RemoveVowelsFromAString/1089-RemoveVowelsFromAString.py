# Last updated: 8/3/2025, 9:02:27 PM
class Solution:
    def removeVowels(self, S: str) -> str:
        stack = list()
        vowel_set = {"a","e","i","o","u"}
        for char in S:
            if char.lower() not in vowel_set:
                stack.append(char)
        return "".join(stack)