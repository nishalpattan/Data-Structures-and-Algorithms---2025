# Last updated: 8/3/2025, 9:02:47 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        start = 1
        end = max(piles)
        while start < end:
            mid = start + (end - start) // 2
            if self.can_eat(mid, piles, H):
                end = mid
            else:
                start = mid + 1
        return start
    
    def can_eat(self,num_eats, piles, H):
        temp = list()
        for pile in piles:
            # temp.append(math.ceil(pile / num_eats))
            temp.append((pile -1) // num_eats + 1 )
        return sum(temp) <= H