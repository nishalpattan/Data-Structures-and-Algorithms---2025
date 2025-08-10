# Last updated: 8/10/2025, 12:55:54 PM
class Solution:
    def reorganizeString(self, s: str) -> str:
        # Interleaving or choose alterante options pattern
        # so the idea is to keep the characters that are not same adjacently.
        # for this at any given position I have to pick a character in a smart way, i know
        # from the input there are duplicates which means each character has a frequency and if I want to choose
        # a character I can choose most frequent one and less frequent one, if I choose less frequent one I fill up the alternative spots
        # quickly and end up in a situation where I can't place the most frequent ones, what if I start with most frequent ones then I can 
        # fill up the lower frequent elements in between leaving more spaces to the most frequent ones.
        # for this to choose most frequent one I can use max heap and when I take out the most frequent one from max heap i can't keep it back
        # immediately, i can store it temporarily some where and pick the next frequent one to place the gaps
        counter = collections.Counter(s)
        max_heap = list()
        for char, freq in counter.items():
            heapq.heappush(max_heap, (-freq, char))
        res = list()
        n = len(s)
        prev = [0, '']
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            res.append(char)
            
            if prev[0] < 0:
                heapq.heappush(max_heap, (prev[0], prev[1]))
            
            prev = [freq + 1, char]
        if len(res) == n:
            return "".join(res)
        
        return ""