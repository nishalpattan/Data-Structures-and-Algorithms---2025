# Last updated: 8/3/2025, 9:02:29 PM
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hash_map = dict()
        res = list()
        for item in items:
            if item[0] in hash_map:
                hash_map[item[0]].append(item[1])
            else:
                hash_map[item[0]] = [item[1]]
        for item in hash_map:
            hash_map[item] = sorted(hash_map[item],reverse=True)[:5]
            total_sum = sum(hash_map[item])
            res.append([item,total_sum // 5])
        return res
            