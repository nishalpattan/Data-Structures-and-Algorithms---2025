# Last updated: 8/9/2025, 9:36:15 AM
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        start = 0
        count_fruits = 0
        hash_map = defaultdict(int)
        n = len(fruits)
        for end in range(n):
            hash_map[fruits[end]] += 1
            count_fruits += 1
            while len(hash_map) > 2:
                hash_map[fruits[start]] -= 1
                if hash_map[fruits[start]] == 0:
                    del hash_map[fruits[start]]
                count_fruits -= 1
                start += 1
            max_fruits = max(max_fruits, count_fruits)
        return max_fruits