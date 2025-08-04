# Last updated: 8/3/2025, 9:02:45 PM
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        # Space Optimized approach
        hash_map = dict()
        result = list()
        for word in A.split():
            hash_map[word] = hash_map.get(word, 0 ) + 1
        for word in B.split():
            hash_map[word] = hash_map.get(word, 0 ) + 1
        for word in hash_map:
            if hash_map.get(word, 0) == 1:
                result.append(word)
        return result
        
        # Brute Force, TC: O(N+M); SC : O(N+M)
        # hash_map_1 = collections.Counter(A.split())
        # hash_map_2 = collections.Counter(B.split())
        # result = list()
        # for word in A.split():
        #     if hash_map_1[word] == 1 and word not in hash_map_2:
        #         result.append(word)
        # for word in B.split():
        #     if hash_map_2[word] == 1 and word not in hash_map_1:
        #         result.append(word)
        # return result