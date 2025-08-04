# Last updated: 8/3/2025, 9:02:23 PM
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        """
        Using Max Heap, 
        TC : O(N *logN) ; SC : O(N)
        
        """
        
        hash_map = dict()
        heap = list()
        result = [0] * len(barcodes)
        index = 0
        
        for code in barcodes:
            hash_map[code] = hash_map.get(code, 0 ) + 1
        
        for code, freq in hash_map.items():
            heapq.heappush(heap, (-freq, code) )
        
        while heap:
            freq, code = heapq.heappop(heap)
            freq = abs(freq)
            
            while freq > 0:
                if index >= len(barcodes):
                    index = 1
                result[index] = code
                index += 2
                freq -= 1
        return result