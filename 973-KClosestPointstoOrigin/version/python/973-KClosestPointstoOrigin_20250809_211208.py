# Last updated: 8/9/2025, 9:12:08 PM
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # as the problem is asking k closest, not the farthest so Use max heap
        # to store the distance of points to the origin using formula sqrt(x^2 + y^2)
        # python only supports the min heap by default so to use it as max heap store the dist as -dist
        # if the length of max_heap is greater than k, technically we are popping farthest distance point only
        # as - 8(far from origin) is less than -1 ( close to origin )
        max_heap = list()
        for point in points:
            x_coord = point[0]
            y_coord = point[1] 
            dist =  x_coord ** 2 + y_coord ** 2
            heapq.heappush(max_heap, (-dist, x_coord, y_coord ))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return [[x,y] for _, x, y in max_heap]
         