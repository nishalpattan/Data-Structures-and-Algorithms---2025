# Last updated: 8/3/2025, 9:02:17 PM
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash_map =  collections.Counter(arr1)
        op = list()
        for j in arr2:
            op.extend([j] * hash_map[j])
            hash_map.pop(j)
        for left_elem in sorted(hash_map.keys()):
            op.extend([left_elem]*hash_map[left_elem])
        
        return op